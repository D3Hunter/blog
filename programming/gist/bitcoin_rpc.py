#!/usr/bin/env python

import requests
import json
import sys
import base64


def bitcoin_rpc(method, params):
    usename = "xx"
    password = "yy"
    auth = "Basic " + base64.encodestring('%s:%s' % (usename, password))

    headers = {"Authorization": auth}
    payload = {"method": method, "params": params, "id": 1}
    response = requests.post("http://localhost:38332",
                             headers=headers, data=json.dumps(payload))
    return response.text


def get_estimaterawfee(target, threshold):
    params = [target, threshold]
    return bitcoin_rpc("estimaterawfee", params)


def get_confirm_rate(item):
    return item["withintarget"] / (item["totalconfirmed"] + item["inmempool"] + item["leftmempool"])


def print_estimate_fee_info(target, threshold):
    result_obj = json.loads(get_estimaterawfee(target, threshold))["result"]
    for item_name in ["short", "medium", "long"]:
        if item_name in result_obj:
            item = result_obj[item_name]
            rate = item["feerate"]
            pass_rate = get_confirm_rate(item["pass"])
            fail_rate = get_confirm_rate(item["fail"])
            print "%-6s: target %d, rate %s, threshold %f, pass %f, fail %f" % (item_name, target, rate, threshold, pass_rate, fail_rate)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "%s target threshold" % (sys.argv[0],)
        exit()

    target = int(sys.argv[1])
    threshold = float(sys.argv[2])

    print_estimate_fee_info(target, threshold)
