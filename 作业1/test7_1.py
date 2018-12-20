# 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。
# Input: 输入时一个数组，数值通过空格隔开。
# Output: 输出筛选之后的数组，用空格隔开。如果有多种解雇哦，则一行一种结果。
# -*- coding:utf-8 -*-

def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


#
if __name__ == "__main__":
    result = []
    #     arr = [int(a) for a in input().split(' ')]
    arr = [1, 2, 4, 7, 11, 10, 9, 15, 3, 5, 8, 6]
    B = lis(arr)
    B_index = [0] * len(B)
    for m in range(0, len(B)):
        B_index[m] = arr.index(B[m])
    arr_reverse = list(reversed(arr))
    C = list(reversed(lis(arr_reverse)))
    C_index = [0] * len(C)
    for m in range(0, len(C)):
        C_index[m] = arr.index(C[m])

    for i in range(0, len(B)):
        if B[i] == C[0]:
            max = len(B[:i] + C)
            for m in range(i + 1, len(B_index)):
                for n in range(0, len(C_index)):
                    if C_index[n] > B_index[m]:
                        if len(B_index[:(m+1)] + C_index[n:]) > max:
                            max = len(B_index[:(m + 1)] + C_index[n:])
                            result = B[:(m + 1)] + C[n:]
                        else:
                            result = B[:i] + C
            print(result)

