# 有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序；
# 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。
# Input: 输入为两行，分别为两个数组，每个值用空格隔开。
# Output: 输出变化之后的两个数组内元素和的差绝对值。
# -*- coding:utf-8 -*-
# 1.将两序列合并为一个序列，并排序，为序列Source
# 2.拿出最大元素Big，次大的元素Small
# 3.在余下的序列S[:-2]进行平分，得到序列max，min
# 4.将Small加到max序列，将Big加大min序列，重新计算新序列和，和大的为max，小的为min。
# 这种做法不能保证最后结果中的两个数组长度相同
def minCha(a,b):
    m1 = []
    m2 = []
    source = a + b
    source.sort(reverse=True)
    # print(source)
    while True:
        s1, s2 = sum(m1), sum(m2)
        if s1 > s2:
            if s1 - s2 >= source[0]:
                m2.append(source.pop(0) if len(source) >= 1 else 0)
                m1.append(source.pop() if len(source) >= 1 else 0)
            else:
                m2.append(source.pop(0) if len(source) >= 1 else 0)
                m1.append(source.pop(0) if len(source) >= 1 else 0)
        else:
            if s2 - s1 >= source[0]:
                m1.append(source.pop(0) if len(source) >= 1 else 0)
                m2.append(source.pop() if len(source) >= 1 else 0)
            else:
                m1.append(source.pop(0) if len(source) >= 1 else 0)
                m2.append(source.pop(0) if len(source) >= 1 else 0)
            # print(m1, m2)
        if len(source) == 0:
            break
    return abs(sum(m1) - sum(m2))

if __name__ == "__main__":
    arr1 = [int(a) for a in input().split(' ')]
    arr2 = [int(a) for a in input().split(' ')]
    print(minCha(arr1,arr2))
