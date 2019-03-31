# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/31 19:56
@description:
"""
def getDepthByBFS(n,nodes,matrix):
    graph = {}
    for i in nodes:
        graph[i] = []
    for i in range(0,n):
        for j in range(1,n+1):
            if int(matrix[i][j]) == 1:
                   graph[nodes[i]].append(nodes[j-1])
    return graph

def DFS(graph,start,depth):
    global S
    global max_depth
    if depth>max_depth:
        max_depth = depth
    for n in graph[start]:
        if n not in S:
            S.add(n)
            DFS(graph,n,depth+1)
            S.remove(n)



if __name__ == "__main__":
    n = int(input())
    result = []
    for i in range(n):
        max_depth = -1
        S = set()
        temp =  [a for a in input().split(' ')]
        # print(temp)
        n = int(temp[0]) #节点个数
        s = temp[1] #起始节点
        nodes = [a for a in input().split(' ')] #节点名称
        matrix = [] #邻接矩阵
        while True:
            try:
                temp = [a for a in input().split(' ')]
                matrix.append(temp)
            except:
                break
        # print(matrix)
        graph = getDepthByBFS(n,nodes,matrix)
        # print(graph)
        S.add(s)
        DFS(graph,s,1)
        result.append(max_depth)
    for i in result:
        print(i)