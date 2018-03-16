#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install requests xlsxwriter beautifulsoup4 xlutils

import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import traceback
from random import random
from http.client import RemoteDisconnected
import re
from os import path
from io import BytesIO

http_session = None

def get_http_content(url):
    global http_session
    if http_session is None:
        http_session = requests.Session()
        http_session.headers['User-Agent'] = 'Chrome/63.0.3239.132'
    doc = http_session.get(url)
    return doc.content

def get_soup(url):
    return BeautifulSoup(get_http_content(url), 'html.parser')

class Apartment(object):
    price = ''
    area = ''
    layout = ''
    floor = ''
    direction = ''
    subway = ''
    subdistrict = ''
    district = ''
    rent_method = ''
    payment = ''
    status = ''
    heating_method = ''
    layout_drawing_url = None
    layout_drawing = ''
    url = ''

    def write_to_sheet(self, sheet, row):
        items = [self.price, self.area, self.layout, self.floor, self.direction, self.subway, self.subdistrict,
            self.district, self.rent_method, self.payment, self.status, self.heating_method,
            self.url]
        for col in range(len(items)):
            sheet.write(row, col, items[col])
        if self.layout_drawing_url is not None:
            image_data = BytesIO(self.layout_drawing)
            sheet.insert_image(row, len(items), self.layout_drawing_url,
                {'image_data': image_data, 'positioning': 1, 'x_scale': 72/600, 'y_scale': 18/450})

def get_apartment_info(url):
    soup = get_soup(url)
    apartment = Apartment()
    apartment.url = url
    apartment.price = soup.find('span', attrs={'class': 'total'}).text.strip()

    layout_drawing = soup.find(attrs={'data-desc': "户型图"})
    if layout_drawing is not None:
        apartment.layout_drawing_url = layout_drawing.img['src']
        apartment.layout_drawing = get_http_content(apartment.layout_drawing_url)

    attrs = soup.find('div', attrs={'class': 'zf-room'}).find_all('p')
    name_list = ['area', 'layout', 'floor', 'direction', 'subway', 'subdistrict', 'district']
    for attr, name  in zip(attrs, name_list):
        label = attr.i.extract()
        if hasattr(apartment, name):
            setattr(apartment, name, attr.text.strip())

    attrs = soup.find('div', attrs={'class': 'introduction'}).find('div', attrs={'class': 'content'}).find_all('li')
    name_list = ['rent_method', 'payment', 'status', 'heating_method']
    for attr, name  in zip(attrs, name_list):
        attr.span.extract()
        if hasattr(apartment, name):
            setattr(apartment, name, attr.text.strip())

    return apartment

def write_to_excel(apartments, filename):
    book = xlsxwriter.Workbook(filename)
    sheet = book.add_worksheet()

    title = [u'价格', u'面积', u'户型', u'楼层', u'朝向', u'地铁', u'小区', u'区域',
            '租赁方式', u'付款方式', u'状态', u'供暖方式', u'url', u'户型图']
    for col in range(len(title)):
        sheet.write(0, col, title[col])
    for r in range(len(apartments)):
        apartments[r].write_to_sheet(sheet, 1 + r)

    book.close()

if __name__ == "__main__":
    interested_list= [
        'https://bj.lianjia.com/zufang/101102630521.html',
        'https://bj.lianjia.com/zufang/101102628250.html',
    ]
    apartments = []
    for url in interested_list:
        apartments.append(get_apartment_info(url))
        # anti-anti-crawler
        time.sleep(2)
    write_to_excel(apartments, 'apartments.xlsx')
