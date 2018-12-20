# -*- encoding: utf-8 -*-
"""
有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
"""

def minCha(arr1,arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    cha = sum1-sum2
    len1 = len(arr1)
    len2 = len(arr2)
    while cha != 0:
        bestChange,besti,bestj=0,0,0
        for i in range(len1):
            for j in range(len2):
                exchangeCha = arr1[i] - arr2[j]
                if abs(cha-2*exchangeCha) <abs(cha-2*bestChange):
                    bestChange,besti,bestj = exchangeCha,i,j
        if bestChange == 0:
            return False
        temp = arr1[besti]
        arr1[besti] = arr2[bestj]
        arr2[bestj] = temp
        sum1 = sum1-bestChange
        sum2 = sum2+bestChange
        cha = sum1-sum2
    return True

if __name__ == "__main__":
    arr1 = [int(a) for a in input().split(' ')]
    arr2 = [int(a) for a in input().split(' ')]
    minCha(arr1,arr2)
    print(abs(sum(arr1)-sum(arr2)))
