# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/23 20:56
@description:
"""
def DFS(cnt,m,visited):
    global num
    if cnt == n:
        num+=1
        return
    for i in range(n):
        if visited[i]==0 and is_ok(i,m,visited):
            visited[i] =1
            DFS(cnt+1,m,visited)
            visited[i] = 0
def is_ok(i,m,visited):
    for j in range(n):
        if m[j][i] == 1 and visited[j] == 0:
            return False
    return True

if __name__ =="__main__":
    n = int(input())
    for i in range(n):
        pairs = input().strip().split(',')
        s = set()
        for pair in pairs:
            x, y = pair.split()
            s.add(x)
            s.add(y)
        n = len(s)
        m = [[0 for _ in range(n)] for _ in range(n)]
        for pair in pairs:
            x, y = pair.split()
            m[ord(x) - ord('a')][ord(y) - ord('a')] = 1
        visited = [0] * n
        num = 0
        DFS(0,m,visited)
        print(num)