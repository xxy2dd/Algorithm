# 给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，每次向右滑动一个位置，
# 求出每一次滑动时窗口内最大元素的和。
# Input：输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。
# Output: 输出一个值。
#
def maxInWindows(arr,k):
    arr_len = len(arr)
    sum = 0
    for i in range(arr_len-k+1):
        sum = sum + max(arr[i:i+k])
    print(sum)

if __name__ == '__main__':
    # temp = [4, 3, 5, 4, 3, 3, 6, 7]
    temp = input()
    # k=3
    k = int(input())
    temp = temp.split(' ')
    # print(temp)
    arr = [int(a) for a in temp]
    # print(arr)
    maxInWindows(arr,k)

