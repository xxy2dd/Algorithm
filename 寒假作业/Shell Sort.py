# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/19 22:01
@description:
"""
def ShellSort(arr,index):
    n = len(arr)
    for gap in index:
        for i in range(gap,n):
            for j in range(i,gap-1,-gap):
                if arr[j] < arr[j-gap]:
                    arr[j],arr[j-gap] = arr[j-gap],arr[j]
                else:
                    break
    return arr

if __name__ =="__main__":
    # arr = [49,38,65,97,76,13,27,49,55,4]
    n = int(input())
    for i in range(n):
        arr = [int(a) for a in input().split(" ")]
        index = [int(a) for a in input().split(" ")]
        print(" ".join(str(i) for i in ShellSort(arr,index)))
