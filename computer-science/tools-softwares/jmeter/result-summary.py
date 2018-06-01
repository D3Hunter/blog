#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

class LoadTestResult(object):
    def __init__(self, testid, runid, cpu, avg_used_heap, byterecv, bytesent, avg_response_time, qps):
        self.testid = testid
        self.runid = runid
        self.cpu = cpu
        self.avg_used_heap = avg_used_heap
        self.byterecv = byterecv
        self.bytesent = bytesent
        self.avg_response_time = avg_response_time
        self.qps = qps

    def generate_markdown_table(self, base=None):
        if base is None:
            return self.generate_markdown_table_without_base()
        table_row = "|%s/%s|" % (self.runid, base.runid)
        table_row += "%.2f%% (**%+.2f%%**)|" %(self.cpu, 100 * (self.cpu - base.cpu) / base.cpu)
        table_row += "%.2f MB (**%+.2f MB**)|" % (self.avg_used_heap, self.avg_used_heap - base.avg_used_heap)
        table_row += "%.2f MB/s|%.2f MB/s (**%+.2f MB/s**)|" % (self.byterecv, self.bytesent, self.bytesent - base.bytesent)
        table_row += "%.2f ms (**%+.2f%%**)|%.2f (**%+.2f%%**)|" % (self.avg_response_time,
            100 * (self.avg_response_time - base.avg_response_time) / base.avg_response_time,
            self.qps, 100 * (self.qps - base.qps) / base.qps)
        return table_row
    def generate_markdown_table_without_base(self):
        table_row = "|"
        table_row += "%s|" % (self.runid)
        table_row += "%.2f%%|" %(self.cpu)
        table_row += "%.2f MB|" % (self.avg_used_heap)
        table_row += "%.2f MB/s|%.2f MB/s|" % (self.byterecv, self.bytesent)
        table_row += "%.2f ms|%.2f|" % (self.avg_response_time, self.qps)
        return table_row
    def markdown_table_header():
        result = "||cpu|avg used heap|bytesrecv|bytessent|avg response time|qps|\n"
        result += "|---|---|---|---|---|---|---|"
        return result
# user.properties中设置jmeterPlugin.perfmon.interval=2000
SAMPLE_INTERVAL = 2
DURATION = 600

# 目录结构：
# test01
# +- base01
#   +- result.jtl # jmeter结果
#   +- perfmon.jtl # perfmon结果
# +- app01
# test02
# ......

if __name__ == "__main__":
    testid = sys.argv[1]

    results = []
    for runid in sys.argv[2:]:
        filename = "%s/%s/perfmon.jtl" % (testid, runid)
        perf_data = {}
        with open(filename, 'rb') as perfmon_csv:
            data_reader = csv.reader(perfmon_csv, delimiter=',')
            # remove header
            data_reader.next()
            # remove first 45 lines of each metric
            # those lines belongs to preheat phase
            for i in range(45 * 4):
                data_reader.next()
            for row in data_reader:
                key = row[2]
                value = int(row[1]) / 1000.0
                if key in perf_data:
                    perf_data[key][0] += value
                    perf_data[key][1] += 1
                else:
                    perf_data[key] = [value, 1]

        cpu = 0
        heap = 0
        bytesrecv = 0
        bytessent = 0
        for key, value in perf_data.iteritems():
            sum = float(value[0])
            count = value[1]
            if 'CPU' in key:
                cpu = sum / count;
            elif 'JMX' in key:
                heap = sum / count / (1 << 20)
            elif 'bytesrecv' in key:
                bytesrecv = sum / count / SAMPLE_INTERVAL / (1 << 20)
            else:
                bytessent = sum / count / SAMPLE_INTERVAL / (1 << 20)

        filename = "%s/%s/result.jtl" % (testid, runid)
        count = 0
        sum = 0
        with open(filename, 'rb') as result_jtl:
            data_reader = csv.reader(result_jtl, delimiter=',')
            # remove header
            data_reader.next()
            for row in data_reader:
                sum += int(row[1])
                count += 1
        response_time = sum / float(count)
        qps = count / float(DURATION)

        results.append(LoadTestResult(testid, runid, cpu, heap, bytesrecv, bytessent, response_time, qps))

    base = results[0]
    print base.generate_markdown_table()
    for result in results[1:]:
        print result.generate_markdown_table(base)

