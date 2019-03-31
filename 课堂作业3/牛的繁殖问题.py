# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/14 18:20
@description:
"""
def countCows(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==0:
        return 0
    else:
        return countCows(n-1)+countCows(n-2)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        year =  int(input())
        print(countCows(year))