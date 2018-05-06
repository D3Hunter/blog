#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import yappi
import time
import threading
import datetime


# 该模块需要一个config模块，提供ProfileDelay/ProfileInterval/ProfileExitAfterProfile三个参数
# import该模块后，会启动后台线程，并每隔ProfileInterval输出一次profile结果
def start_profile():
    time.sleep(config.ProfileDelay)

    yappi.start(True)

    while True:
        end = time.time() + config.ProfileInterval
        while time.time() < end:
            time.sleep(1)

        columns = {0: ("name", 60), 1: ("ncall", 16), 2: ("tsub", 9), 3: ("ttot", 9), 4: ("tavg", 9)}
        filename = "profile-{}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"))
        with open(filename, "w") as stream:
            stats = yappi.get_func_stats().sort("ttot", "desc").get()
            count = 0
            for stat in stats:
                stat._print(stream, columns)
                if getattr(stat, "children") is not None:
                    for child in stat.children:
                        stream.write("    ")
                        child._print(stream, columns)
                count += 1
                if count >= config.ProfileMaxPrint:
                    break
            yappi.get_thread_stats().print_all(out=stream)

    if config.ProfileExitAfterProfile:
        import os
        os._exit(1)


threading.Thread(target=start_profile, daemon=True).start()
