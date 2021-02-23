#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Python-20210127 -> target_exe.py.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/2/23 8:57
@Desc    :
================================================="""
import sys


def main():
    print("target_exe started")  # main()函数开始了
    argc = len(sys.argv)
    if argc == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        result = a + b  # 两数相加
        print("a + b =", result)
        if a < 0 or a > 100:  # 对a的作用域进行判断
            print("a is not in [0, 100]")
        if a > 0 and b > 0:
            print("a and b >0")


if __name__ == '__main__':
    main()
