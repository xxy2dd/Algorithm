# 输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。
# Input: 输入第一行是数组，每一个数用空格隔开；第二行是数字和。
# Output: 输出这样两个数有几对。
# -*- coding:utf-8 -*-
def getPairsWithSum(arr,sum):
    # 先排序
    quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
        [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
        [item for item in array[1:] if item > array[0]])
    arr = quick_sort(arr)
    if arr == None or len(arr) <= 0 or arr[-1] + arr[-2] < sum:
        return []
    start = 0
    end = len(arr) - 1
    res = 0
    # 双指针
    while start < end:
        if arr[start] + arr[end] < sum:
            start += 1
        elif arr[start] + arr[end] > sum:
            end -= 1
        else:
            res += 1
            start += 1
            end -= 1

    return res

if __name__ == "__main__":
    arr = [int(a) for a in input().split(' ')]
    sum = int(input())
    print(getPairsWithSum(arr,sum))