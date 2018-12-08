def maxInWindows(arr,k):
    arr_len = len(arr)
    sum = 0
    for i in range(arr_len-k+1):
        sum = sum + max(arr[i:i+k])
    print(sum)

if __name__ == '__main__':
    temp = input()
    k = int(input())
    temp = temp.split(' ')
    # print(temp)
    arr = [int(a) for a in temp]
    # print(arr)
    maxInWindows(arr,k)

