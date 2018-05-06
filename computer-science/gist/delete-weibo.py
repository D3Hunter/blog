#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import threading
import re
import time

REGEX = r' mid=\\"([0-9]+)\\" '
COOKIE="xxxxxxxxx"

class PostRequestThread (threading.Thread):
    def __init__(self, url, headers, payload):
        threading.Thread.__init__(self)
        self.url = url
        self.headers = headers;
        self.payload = payload
    def run(self):
        do_post(self.url, self.headers, self.payload)

def do_post(url, headers, payload, dump_content = True):
    respond = requests.post(url, headers=headers, data=payload)
    if dump_content:
        print respond.content

def submit_forms_multithread(url, referer, payloads, headers, wait_time=1):
    headers = headers.copy()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Referer"] = referer
    threads = []
    for payload in payloads:
        del_thread = PostRequestThread(url, headers, payload)
        del_thread.start()
        time.sleep(wait_time)
        threads.append(del_thread)
    for t in threads:
        t.join()

def generate_payloads(ids, name):
    payloads = []
    for id in ids:
        payloads.append({name : id})
    return payloads

def get_ids_from_page(url, headers, regex_str, dump_content = True):
    request = requests.get(url, headers=headers)
    if dump_content:
        with open('test.html', 'wb') as f:
            f.write(request.content)
    re_pattern = re.compile(regex_str)
    ids = []
    for match in re_pattern.finditer(request.content):
        ids.append(match.group(1))
    return ids

def unfollow_weibo_uids(ids, headers):
    url = "https://weibo.com/aj/f/unfollow?ajwvr=6"
    referer = "referers to unfollow uid"
    submit_forms_multithread(url, referer, generate_payloads(ids, "uid"), headers)

def remove_weibo_follows(headers):
    url = "url to get uids of follows"
    ids = get_ids_from_page(url, headers, r'uid=([0-9]+)')
    ids = list(set(ids))
    if not ids:
        return False
    unfollow_weibo_uids(ids, headers)
    print('Delete_uidd {} posts'.format(len(ids)))
    return True

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4,zh-CN;q=0.2',
        'cookie': COOKIE
    }
    for i in range(100):
        if not remove_weibo_follows(headers):
            print('got empty ids, wait')
            time.sleep(1)
        time.sleep(1.5)

if __name__ == '__main__':
    main()
