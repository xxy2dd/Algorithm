# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/31 19:56
@description:
"""
from queue import Queue
def BFS(n,s,nodes,matrix):
    Q = Queue() #记录遍历的节点
    result = [] #存储结果
    indexs = Queue()
    visited = [0 for i in range(n)]
    for i in range(0,n):
        if matrix[i][0] == s:
            Q.put(s)
            visited[i] = 1
            indexs.put(i)
            while(Q.qsize()!=0):
                result.append(Q.get())
                index = indexs.get()
                for j in range(1,n+1):
                    if int(matrix[index][j]) == 1 and visited[j-1]==0:
                        indexs.put(j-1)
                        Q.put(nodes[j-1])
                        visited[j-1]=1
                    else:
                        continue
    return result
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        temp =  [a for a in input().split(' ')]
        # print(temp)
        n = int(temp[0])
        s = temp[1]
        nodes = [a for a in input().split(' ')]
        matrix = []
        while True:
            try:
                temp = [a for a in input().split(' ')]
                matrix.append(temp)
            except:
                break
        # print(matrix)
        result = BFS(n, s, nodes, matrix)
        print(" ".join(str(i) for i in result))
    # n = 4
    # s = 'a'
    # nodes =['a','b','c','d']
    # matrix = [['a',0,1,1,0],['b',1,0,1,0],['c',1,1,0,1],['d',0,0,1,0]]

