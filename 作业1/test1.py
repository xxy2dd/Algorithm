# 给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果小于等于num的个数。
# 请实现一个时间复杂度为O(length(arr))的算法
# Input: 输入的第一行为数组，每一个数用空格隔开，第二行为num。
# Output: 输出一个值。
# -*- coding:utf-8 -*-
def getNum(arr,k):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            # qmin[-1]表示数组qmin的最后一个元素，如果当前遍历的元素值比qmin[-1]小，那么qmin[-1]出栈，j入栈
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            # qmax[-1]表示数组qmax的最后一个元素，如果当前遍历的元素值比qmax[-1]大，那么qmax[-1]出栈，j入栈
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            # 如果此时最大值减最小值大于k，则跳出循环
            if arr[qmax[0]] - arr[qmin[0]] > k:
                break
            j += 1
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    return res

if __name__ == "__main__":
    arr = [int(a) for a in input().split(' ')]
    k = int(input())
    print(getNum(arr,k))
