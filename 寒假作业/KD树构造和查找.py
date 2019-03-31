# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/24 14:20
@description:
"""
import numpy as np

class Node:
    def __init__(self, value=None, split=None, left=None, right=None):
        self.value = value
        self.split = split #分割维度的序号
        self.left = left #左子树
        self.right = right #右子树

# 构建KD树
def buildKDTree(root, data):
    length = len(data)
    if length == 0:
        return
    dimension = len(data[0])
    max_var = 0
    split = 0
    for i in range(dimension):
        arr = []
        for j in data:
            arr.append(j[i])
        var = calVariance(arr)
        if var > max_var:
            max_var = var
            split = i
    data = sorted(data, key=lambda x: x[split])
    point = data[int(length / 2)]
    root = Node(point, split)
    root.left = buildKDTree(root.left, data[0:int(length / 2)])
    root.right = buildKDTree(root.right, data[int(length / 2) + 1:length])
    return root

# 计算方差
def calVariance(arr):
    temp = [float(i) for i in arr]
    arrList = np.array(temp)
    length = len(arrList)
    sum1 = arrList.sum()
    array2 = arrList * arrList
    sum2 = array2.sum()
    mean = sum1 / length
    var = sum2 / length - mean ** 2
    return var

# 计算欧式距离
def calDistance(point1, point2):
    sum = 0.0
    for i in range(len(point1)):
        sum = sum + (float(point1[i]) - float(point2[i]))**2
    return sum**0.5


def findKPoints(tree, target, k):
    node_k = []  # 存放k个最近距离
    result = []
    nodeList = []
    temp_root = tree
    while temp_root:
        nodeList.append(temp_root)
        dd = calDistance(target, temp_root.value)
        if len(node_k) < k:
            node_k.append(dd)
            result.append(temp_root.value)
        else:
            max_dist = max(node_k)
            if dd < max_dist:
                index = node_k.index(max_dist)
                del (node_k[index])
                del (result[index])
                node_k.append(dd)
                result.append(temp_root.value)
        ss = temp_root.split
        if target[ss] <= temp_root.value[ss]:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right
    while nodeList:
        back_point = nodeList.pop()
        ss = back_point.split
        max_dist = max(node_k)
        if len(node_k) < k or abs(float(target[ss]) - float(back_point.value[ss])) < max_dist:
            if float(target[ss]) <= float(back_point.value[ss]):
                temp_root = back_point.right
            else:
                temp_root = back_point.left
            if temp_root:
                nodeList.append(temp_root)
                curDist = calDistance(temp_root.value, target)
                if max_dist > curDist and len(node_k) == k:
                    index = node_k.index(max_dist)
                    del (node_k[index])
                    del (result[index])
                    node_k.append(curDist)
                    result.append(temp_root.value)
                elif len(node_k) < k:
                    node_k.append(curDist)
                    result.append(temp_root.value)
    showResults(node_k,result,k)

def showResults(node_k,result,k):
    dict = {}
    for i in range(k):
        dict[ node_k[i]] =result[i]
    result = sorted(dict.items(),key=lambda item:item[0])
    for i in range(k):
        temp = result[i][1]
        for j in range(2):
            print(temp[j],end="")
            if j == 0:
                print(" ",end="")
        if i<k-1:
            print(",",end="")

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        root = Node()
        data = [[a for a in i.split(" ")] for i in input().split(",")]
        target = [a for a in input().split(" ")]
        k = int(input())
        tree = buildKDTree(root, data)
        findKPoints(tree, target, k)
        print()

