#!/usr/bin/env python
import sys
import csv
import re

if __name__ == "__main__":
    testid = sys.argv[1]
    runid = sys.argv[2]
    filename = "%s/%s/perfmon.jtl" % (testid, runid)

    with open(filename, 'rb') as perfmon_csv, open("load-influxdb.txt", "wb") as output:
        data_reader = csv.reader(perfmon_csv, delimiter=',')
        # skip header
        data_reader.next()
        for row in data_reader:
            time = (int(row[0]) / 1000) * 1000000000
            value = int(row[1]) / 1000
            label = re.sub(r"pid=[0-9]+", "", row[2]).replace(" ", "\\ ")
            output.write("perfmon,testid=%s,runid=%s,label=%s value=%d %d\n" % (testid, runid, label, value, time))

