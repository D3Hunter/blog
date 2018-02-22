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
    return BeautifulSoup(doc.content, 'html.parser')

def valid_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

class Company(object):
    def __init__(self, row, token):
        #import pdb; pdb.set_trace()
        cells = row.find_all('td')
        self.name = cells[1].text.strip()
        self.phase = cells[2].text.strip()
        self.field = cells[3].text.strip()
        self.create_time = cells[4].text.strip()
        self.detail_url = cells[1].find('a')['href']
        self.tags = []
        self.detail = ''

        self.year = re.split('\.|-', self.create_time)[0]
        # 页面上有的时间是字符串
        if not valid_int(self.year) or int(self.year) >= 2017:
            self._init_detail(token)
    def _init_detail(self, token):
        # 有些公司没有详细的信息，url为官网地址
        if not self.detail_url.endswith('html'):
            print("invalid detail_url {} for {}".format(self.detail_url, self.name))
            return
        soup = get_soup('{}?token={}'.format(self.detail_url, token))
        tags = soup.find(attrs={'class': "info-tag clearfix"}).find_all('a')[3:]
        for tag in tags:
	        self.tags.append(tag)
        
        detail = soup.find(attrs={'class': "info-box"})
        if detail.find('p') is not None:
            detail = detail.find('p')
        self.detail = detail.text.strip()
        # anti-anti-crawler
        time.sleep(1.2 + random())


def process_company_table(companies, table, token):
    try:
        for row in table.find_all('tr')[1:]:
            item = Company(row, token)
            print('   got {}'.format(item.name))
            if valid_int(item.year) and int(item.year) < 2017:
                print('created time < 2017, stop crawling')
                return False
            companies.append(item)
    except RemoteDisconnected as e:
        print("remote server rejected our request")
        raise
    except:
        print("failed to process row {}".format(row))
        traceback.print_exc()
    return True

def get_all_companies(start_page=1):
    url_template = "http://www.cyzone.cn/vcompany/list-3495-0-{}-2-3/0"
    page_num = start_page
    companies = []
    try:
        while True:
            print('Crawling page {}'.format(page_num))
            soup = get_soup(url_template.format(page_num))
            table = soup.find('table')
            token = soup.find('input', {'name': 'token'})['value']
            if table is None or token is None:
                break
            move_on = process_company_table(companies, table, token)
            if not move_on:
                break
            page_num += 1
            # anti-anti-crawler
            time.sleep(2)
    except Exception as e:
        print("error on crawling page {}".format(page_num))
        traceback.print_exc()
    return companies

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
        sheet = book.add_sheet("Sheet 1")

    for r in range(len(companies)):
        company = companies[r]
        items = [company.name, company.phase, company.field, company.create_time, company.detail]
        for col in range(len(items)):
            sheet.write(r + start_row, col, items[col])

    book.save(filename)


if __name__ == "__main__":
    write_to_excel(get_all_companies(), "companies.xls")
