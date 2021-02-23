#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Python-20210127 -> max_sub_str.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/2/2 9:13
@Desc    :
================================================="""
from collections import defaultdict


def main():
    s = "AAAAAABABBBBCCCDDDD"
    k = 1
    dic_char = defaultdict(int)
    char_freq, char_start, char_end = 0, 0, 0
    maxlen = 0
    for c in s:
        char_end += 1
        dic_char[c] += 1
        char_freq = max(dic_char[c], char_freq)
        if (char_end - char_start - char_freq) > k:
            dic_char[s[char_start]] -= 1
            char_start += 1
        print(char_end, char_start)
        maxlen = char_end - char_start
    print(maxlen)
    return maxlen


if __name__ == '__main__':
    main()
