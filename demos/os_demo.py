#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""测试 os 模块"""

__author__ = 'sesehai'

import os

def testFork():
    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

if __name__ == '__main__':
    # testFork()
    # print(callable(testFork))

    print(type.__class__.__name__)
    os.chmod('./os_demo.py', 0755)
