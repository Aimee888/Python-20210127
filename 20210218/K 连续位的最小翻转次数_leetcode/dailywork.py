#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Python-20210127 -> dailywork.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/2/18 10:06
@Desc    :
================================================="""
import collections


def minKBitFlips(A, K):
    # nums = 0
    # length = len(A)
    # while True:
    #     try:
    #         index_start = A.index(0)
    #     except:
    #         return nums
    #     index_end = index_start + K
    #     if index_end > length:
    #         return -1
    #     nums += 1
    #     for index in range(index_start, index_end):
    #         if A[index] == 0:
    #             A[index] = 1
    #         else:
    #             A[index] = 0
    N = len(A)
    que = collections.deque()
    res = 0
    for i in range(N):
        print("i = ", i)
        if que and i >= que[0] + K:
            que.popleft()
            print("pop", que)
        if len(que) % 2 == A[i]:
            if i + K > N:
                return -1
            que.append(i)
            print(que)
            res += 1
    return res


def main():
    a = [1, 0, 0, 0, 1, 1, 0]
    k = 2
    nums = minKBitFlips(a, k)
    print(nums)


if __name__ == '__main__':
    main()
