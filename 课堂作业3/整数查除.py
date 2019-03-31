# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/14 20:24
@description:
"""

def findMulti(arr,k):
    result = []
    for i in k:
        count =0
        for n in arr:
            if n%i==0:
                count += 1
        result.append(count)
    return result

if __name__ == "__main__":

    n = int(input())
    for i in range(n):
        length = [int(a) for a in input().split(" ")]
        arr = [int(a) for a in input().split(" ")]
        k = [int(a) for a in input().split(" ")]
        result = findMulti(arr,k)
        print(" ".join(str(i) for i in result))

