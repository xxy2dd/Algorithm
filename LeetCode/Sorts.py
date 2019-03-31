# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/18 19:18
@description:
"""
import math
# 比较相邻的元素，如果num1>num2,那么交换
# 重复上一步直到结尾，此时最后的元素是最大的元素
# 重复以上步骤
def bubbleSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1, 0, -1):
        indicator = False #用于优化（没有交换表示已经有序，结束循环）
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                indicator = True
        if not indicator: #说明列表已经有序
            break
    return arr
# 基于选择划分，需要选定基准值(pivot)
def QuickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    def partition(arr,left,right):
        pivot = left
        while left<right:
            while left<right and arr[right]>=arr[pivot]:
                right = right -1
            while left<right and arr[left]<=arr[pivot]:
                left =left + 1
            arr[left],arr[right] = arr[right],arr[left]
        arr[left],arr[pivot] = arr[pivot],arr[left]
        return left

    def quick(arr,left,right):
        if left>=right:
            return
        mid = partition(arr,left,right)
        quick(arr.left,mid-1)
        quick(arr,mid+1,right)




# 在未排序序列中找到最小元素，放在起始位置
# 继续在剩余未排序元素中继续寻找最小元素，放在已排序元素末尾
# 重复上一步
def selectionSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        if minIndex!=i:
            arr[i],arr[minIndex] =  arr[minIndex],arr[i]
    return arr

# 假设第一个元素是有序序列，第二个元素至最后为无序序列
# 扫描无序序列，
def insertSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1,n):
        j = i
        target = arr[i] #待插入元素
        while j>0 and target<arr[i-1]: #比较、后移
            arr[i] = arr[i-1]
            j = j-1
        arr[j] = target
    return arr

