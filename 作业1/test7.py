# 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。
# Input: 输入时一个数组，数值通过空格隔开。
# Output: 输出筛选之后的数组，用空格隔开。如果有多种解雇哦，则一行一种结果。
# -*- coding:utf-8 -*-

def DoubleEndLIS(arr):
    max = 0
    k = 0
    result = [0]*len(arr)
    LIS = [0]*len(arr)
    B = [0]*len(arr)
    LIS[0] = arr[0]
    for i in range(0,len(arr)):
        left = 0
        right = B[k]
        while left<=right:
            mid = int((left+right)/2)
            if arr[i]<LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1
        LIS[left] = arr[i]
        if left>B[k]:
            B[k+1] = B[k] + 1
            k += 1
    for i in range(0,k):
        B[i] += 1
    print(LIS)
    k = 0
    LIS = [0] * len(arr)
    C = [0] * len(arr)
    LIS[0] = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        left = 0
        right = C[k]
        while left<=right:
            mid = int((left + right) / 2)
            if arr[i] < LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1
        LIS[left] = arr[i]
        if left > C[k]:
            C[k + 1] = C[k] + 1
            k += 1
    for i in range(0, k):
        C[i] += 1
    print(LIS)

    for i in range(len(arr)):
        if B[i]+C[i]>max:
            max = B[i] + C[i]

    return len(arr)-max+1



if __name__ == "__main__":
    arr = [int(a) for a in input().split(' ')]
    print(DoubleEndLIS(arr))

