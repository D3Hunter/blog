#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install requests xlwt beautifulsoup4 xlutils

import requests
from bs4 import BeautifulSoup
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
import time
import traceback
from random import random
from http.client import RemoteDisconnected
import re
from os import path

http_session = None

def get_soup(url):
    global http_session
    if http_session is None:
        http_session = requests.Session()
        http_session.headers['User-Agent'] = 'Chrome/63.0.3239.132'
    doc = http_session.get(url)
    return BeautifulSoup(doc.content, 'lxml')

def valid_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

class Company(object):
    # 来自创业公司的数据
    def __init__(self, row, token):
        #import pdb; pdb.set_trace()
        cells = row.find_all('td')
        self.name = cells[1].text.strip()
        self.city = ''
        self.last_financing_money = ''
        self.phase = cells[2].text.strip()
        self.last_financing_date = ''
        self.field = cells[3].text.strip()
        self.create_time = cells[4].text.strip()
        self.detail_url = cells[1].find('a')['href']
        self.detail = ''

        self.year = re.split('\.|-', self.create_time)[0]
        # 有些公司没有详细的信息，url为官网地址
        if not self.detail_url.endswith('html'):
            print("invalid detail_url {} for {}".format(self.detail_url, self.name))
            return
        # 页面上有的时间是字符串
        if u'尚未获投' not in self.phase and (not valid_int(self.year) or int(self.year) >= 2017):
            self._init_detail(token)

    # 来自融资动态
    def __init__(self, row):
        # import pdb; pdb.set_trace()
        cell = row.find('td').find_next_sibling()
        self.name = cell.find('a').text.strip()
        self.detail_url = cell.find('a')['href']
        self.city = ''
        cell = cell.find_next_sibling()
        self.last_financing_money = cell.find(attrs={'class': 'money'}).text.strip()
        cell = cell.find_next_sibling()
        self.phase = cell.text.strip()
        cell = cell.find_next_sibling().find_next_sibling()
        self.field = cell.text.strip()
        cell = cell.find_next_sibling()
        self.last_financing_date = cell.text.strip()
        self.create_time = ''
        self.detail = ''
        self.year = ''

        self._init_detail(None)

    def _init_detail(self, token):
        url = self.detail_url
        if token is not None:
            url = '{}?token={}'.format(self.detail_url, token)
        soup = get_soup(url)

        tags = soup.find(attrs={'class': "info-tag clearfix"}).find_all('li')
        self.create_time = tags[0].text
        self.city = tags[1].text
        detail = soup.find(attrs={'class': "info-box"})
        if detail.find('p') is not None:
            detail = detail.find('p')
        self.detail = detail.text.strip()
        # anti-anti-crawler
        time.sleep(2 + random())

    def write_to_sheet(self, sheet, row):
        items = [self.name, self.city, self.field, self.create_time,
            self.phase, self.last_financing_money, self.last_financing_date, self.detail]
        for col in range(len(items)):
            sheet.write(row, col, items[col])


class CompanyExtractor(object):
    def __init__(self, url, find_rows, should_stop):
        self.url = url
        self.find_rows = find_rows
        self.should_stop = should_stop
        self.companies = []

    def get_all_companies(self):
        return self.companies

    def extract(self, start_page=1, end_page=10000):
        page_num = start_page
        try:
            while page_num <= end_page:
                print('Crawling page {}'.format(page_num))
                soup = get_soup(self.url.format(page_num))
                stop = self._process_page(soup)
                if stop:
                    break
                page_num += 1
                # anti-anti-crawler
                time.sleep(2)
        except Exception as e:
            print("error on crawling page {}".format(page_num))
            traceback.print_exc()

    def _process_page(self, soup):
        table = soup.find('table')
        if table is None:
            return True
        token = None
        if soup.find('input', {'name': 'token'}) is not None:
            token = soup.find('input', {'name': 'token'})['value']
        return self._process_company_table(table, token)

    def _process_company_table(self, table, token):
        for row in self.find_rows(table):
            try:
                if token is None:
                    item = Company(row)
                else:
                    item = Company(row, token)
                print('   got {}'.format(item.name))
                if self.should_stop(item):
                    print('should stop return True, stop crawling')
                    return True
                self.companies.append(item)
            except RemoteDisconnected as e:
                print("remote server rejected our request")
                raise
            except:
                print("failed to process row {}".format(row))
                traceback.print_exc()
        return False


def open_excel_book(filename):
    if path.isfile(filename):
        book_ro = open_workbook(filename)
        return (True, copy(book_ro))  # creates a writeable copy
    else:
        return (False, xlwt.Workbook(encoding="utf-8"))

def write_to_excel(companies, filename):
    existed, book = open_excel_book(filename)
    sheet = None
    start_row = 0
    if existed:
        sheet = book.get_sheet(0)
        start_row = len(sheet.get_rows())
    else:
        sheet = book.add_sheet(u"Sheet 1")

    title = [u'名称', u'城市', u'领域', u'创建时间', u'融资阶段', u'融资金额', u'融资时间', u'详情']
    for col in range(len(title)):
        sheet.write(start_row, col, title[col])
    for r in range(len(companies)):
        companies[r].write_to_sheet(sheet, 1 + r + start_row)

    book.save(filename)


if __name__ == "__main__":
    startup_company = {
        'url': "http://www.cyzone.cn/vcompany/list-0-0-{}-2-3/0",
        'find_rows': lambda table: table.find_all('tr')[1:],
        'should_stop': lambda item: valid_int(item.year) and int(item.year) < 2017
    }

    cop_service_financing = {
        'url': "http://www.cyzone.cn/event/list-764-3495-{}-0-20170823-20180223-0/",
        'find_rows': lambda table: table.find_all('tr', {"class": "table-plate3"}),
        'should_stop': lambda item: False
    }

    extractor = CompanyExtractor(**cop_service_financing)
    extractor.extract()

    write_to_excel(extractor.get_all_companies(), "companies.xls")
