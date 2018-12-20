# 找到给定数组的给定区间内的倒数第K小的数值。
# Input: 输入的第一行为数组，每一个数用空格隔开；
# 第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。
# Output: 结果。
# -*- coding:utf-8 -*-
def getDTopk(arr,range,k):
    start = range[0]
    end = range[1]
    # 先从待排序的数组中找出一个数作为基准数（取第一个数即可），然后将原来的数组划分成两部分：
    # 小于基准数的左子数组和大于等于基准数的右子数组。
    # 然后对这两个子数组再递归重复上述过程，直到两个子数组的所有数都分别有序。
    # 最后返回“左子数组” + “基准数” + “右子数组”，即是最终排序好的数组。
    quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
        [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
        [item for item in array[1:] if item > array[0]])
    temp = quick_sort(arr[start-1:end])
    return temp[k-1]


if __name__ == "__main__":
    arr = [int(a) for a in input().split(' ')]
    range = [int(a) for a in input().split(' ')]
    k = int(input())
    print(getDTopk(arr,range,k))



