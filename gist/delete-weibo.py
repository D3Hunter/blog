#!/usr/bin/env python

import requests
import threading
import re
import time

REGEX = r' mid=\\"([0-9]+)\\" '
USER_ID="xxxxxxx"
COOKIE="xxxxxxx"

class myThread (threading.Thread):
    def __init__(self, headers, payload):
        threading.Thread.__init__(self)
        self.headers = headers;
        self.payload = payload
    def run(self):
        delopr(self.headers, self.payload)    

def delete(ids, headers):
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Referer"] = "https://weibo.com/" + USER_ID + "/profile?topnav=1&wvr=6&is_all=1"
    threads = []
    for id in ids:
        payload = {"mid" : id}
        del_thread = myThread(headers, payload)
        del_thread.start()
        threads.append(del_thread)
    for t in threads:
        t.join()

def delopr(headers, payload):
    respond = requests.post("https://weibo.com/aj/mblog/del?ajwvr=6", headers=headers, data=payload)
    print respond.content

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4,zh-CN;q=0.2',
        'cookie': COOKIE
    }
    url = "https://weibo.com/" + USER_ID + "/profile"
    re_pattern = re.compile(REGEX)
    for i in range(100):
        request = requests.get(url, headers=headers)
        with open('test.html', 'wb') as f:
            f.write(request.content)
        ids = []
        for match in re_pattern.finditer(request.content):
            ids.append(match.group(1))

        print(ids)
        if not ids:
            print('exit')
            time.sleep(1)
        delete(ids, headers)
        print('Deleted {} posts'.format(len(ids)))

if __name__ == '__main__':
    main()