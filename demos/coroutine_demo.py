#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
协程测试
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
        print('n=%d' % (n,))
        b = 9


def a():
    r = ''
    yield r
    print(r)



def b(c):
    c.send(None)
    c.send("jjj")

if __name__ == '__main__':
#     c = consumer()
#     produce(c)
    # for i in fab(5):
    #     print(i)
    x = a()
    b(x)
