#!/usr/bin/env python

import sys
import requests
import json
import time


def full_running(ip, rps):
	r = requests.get('http://10.128.6.' + ip + ':8089/stats/requests')
	result = r.json()
	print "state for 10.128.6." + ip + " is " + result['state']
	return result['state'] == 'running' and result['total_rps'] > rps

def all_running(ips, rps):
	result = True
	for ip in ips.split(','):
		result &= full_running(ip, rps)
	return result

if len(sys.argv) < 2:
	print 'usage:' + sys.argv[0] + ' <ip-list> <rps>'
	exit()

ips = sys.argv[1]
rps = sys.argv[2]

success = False
while not success:
	time.sleep(5)
	success = all_running(ips, rps)
	print 'new state: ' + success

print 'wait for another 10 seconds'
time.sleep(10)

