# 给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果大于num的个数。
# 请实现一个时间复杂度为O(length(arr))的算法
# Input: 输入的第一行为数组，每一个数用空格隔开，第二行为num。
# Output: 输出一个值。

def getNum(arr,k):
    res = 0
    arr_len = len(arr)
    for i in range(0,arr_len):
        min = arr[i]
        max = arr[i]
        for j in range(i+1,arr_len):
            if arr[j]>max:
                max = arr[j]
            if arr[j]<min:
                min = arr[j]
            if (max - min) > k:
                res += 1
            j +=1
    return res

if __name__ == "__main__":
    arr = [int(a) for a in input().split(' ')]
    k = int(input())
    print(getNum(arr,k))


