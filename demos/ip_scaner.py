#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python2.7.x ip_scaner.py

"""
不同平台，实现对所在内网端的ip扫描

有时候需要知道所在局域网的有效ip，但是又不想找特定的工具来扫描。
使用方法 python ip_scaner.py 192.168.1.1
(会扫描192.168.1.1-255的ip)
"""

import logging
import platform
import sys
import os
import time
import threading

def get_os():
    """
    get os 类型
    """
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"


def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    logging.info("cmd is %s" % " ".join(cmd))
    output = os.popen(" ".join(cmd)).readlines()
    logging.info("output: %s" % output)

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
    if flag:
        print("ip: %s is ok ***" % ip_str)


def find_ip(ip_prefix):
    """
    给出当前的127.0.0 ，然后扫描整个段所有地址
    """
    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        logging.info("find_ip %s" % ip)
        t = threading.Thread(target=ping_ip, args=(ip,))
        t.start()
        t.join()
        # time.sleep(0.3)


if __name__ == "__main__":
    print("start time %s" % time.ctime())
    command_args = sys.argv[1:]
    args = "".join(command_args)

    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    print("end time %s" % time.ctime())
