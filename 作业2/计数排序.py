#
def countSort(arr,k):
    N = len(arr)
    # 临时数组，最大下标为k
    count_tmp = [0 for i in range(k+1)]
    # 结果数组
    result = [0 for i in range(N)]
    # 记录每一个元素出现的次数
    for i in range(N):
        count_tmp[arr[i]] += 1
    # 记录每一个元素等于或者小于他的元素个数，从第一个开始
    for i in range(1,len(count_tmp)):
        count_tmp[i]+=count_tmp[i-1]
    # 遍历arr中的每一个数，放在相应的结果数组的位置
    # 比如说有5个元素小于等于x，那么x应该放在第6个位置上，下标为5
    for i in range(N):
       result[count_tmp[arr[i]]-1] = arr[i]
       count_tmp[arr[i]] -= 1
    return result

if __name__ == '__main__':
    try:
        while True:
            # arr = [24,3,56,34,3,78,12,29,49,84,51,9,100]
            s = [int(a) for a in input().split(' ')]
            n = s[0]
            arr = s[1:]
            k = max(arr)
            print(countSort(arr,k), end=" ")
            print()
    except EOFError:
        pass
