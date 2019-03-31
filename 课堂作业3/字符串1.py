# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/14 18:39
@description:
"""

def findLCS(str):
    result = 0
    for i in range(0, int(len(str) / 2)):
        for j in range(i + 1, len(str)):
            if (j - i + 1) % 2 == 0:
                mid = int((j - i + 1) / 2)
                left_sum = 0
                right_sum = 0
                for p in range(i, mid + 1):
                    left_sum += int(str[p])
                for q in range(mid + 1, j + 1):
                    right_sum += int(str[q])
                if left_sum == right_sum:
                    if result<(j-i+1):
                        result = j-i+1
            j+=1
        i += 1
    return result

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        print(findLCS(s))
        print()