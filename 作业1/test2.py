# 给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
# Input：输入的每一行是用空格隔开的0或1。
# Output: 输出一个数值。
# -*- coding:utf-8 -*-
def maximalRectangle(matrix):
    if len(matrix) == 0:
        return 0
    result = 0
    m = len(matrix)
    n = len(matrix[0])
    L = [0 for _ in range(n)]
    H = [0 for _ in range(n)]
    R = [n for _ in range(n)]

    for i in range(m):
        left = 0
        for j in range(n):
            if matrix[i][j] == 1:
                L[j] = max(L[j], left)
                H[j] += 1
            else:
                L[j] = 0
                H[j] = 0
                R[j] = n
                left = j + 1

        right = n
        for j in reversed(range(n)):
            if matrix[i][j] == 1:
                R[j] = min(R[j], right)
                result = max(result, H[j] * (R[j] - L[j]))
            else:
                right = j

    return result


if __name__ == "__main__":
    matrix = []
    while True:
        try:
            temp = input()
            temp = [int(a) for a in temp.split(' ')]
            matrix.append(temp)
            print(matrix)
        except:
            break

    print(maximalRectangle(matrix))
