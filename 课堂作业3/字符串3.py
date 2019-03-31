# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/14 19:13
@description:
"""


def nativeStringMatcher(t, p):
    '''
    :param t: the string to check
    :param p: pattern
    '''
    n = len(t)
    m = len(p)
    result = []
    for s in range(0, n-m+1):
        if p == t[s:s+m]:
            result.append(s)
    return result



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        temp = input().split(",")
        target = temp[0]
        pattern = temp[1]
        result = nativeStringMatcher(target, pattern)
        print(" ".join(str(i) for i in result))


