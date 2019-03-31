# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/24 14:20
@description:
"""
# 匈牙利算法
import numpy as np
from scipy.optimize import linear_sum_assignment

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        tasks = int(input())
        # temp = [[int(a) for a in b.split(" ")] for b in input().split(",")]
        # print(temp)
#         生成cost矩阵
        cost = [[0 for _ in range(tasks)] for _ in range(tasks)]
        temp = input().split(",")
        for t in temp:
            people,task,value = t.split(" ")
            cost[int(people)-1][int(task)-1] = int(value)
        cost = np.array(cost)
        # print(cost)
        row_ind, col_ind = linear_sum_assignment(cost)
        # print(row_ind)  # 开销矩阵对应的行索引
        # print(col_ind)  # 对应行索引的最优指派的列索引
        # print(cost[row_ind, col_ind])  # 提取每个行索引的最优指派列索引所在的元素，形成数组
        # print(cost[row_ind, col_ind].sum())  # 数组求和
        result = col_ind + 1
        print(" ".join(str(i) for i in result))




