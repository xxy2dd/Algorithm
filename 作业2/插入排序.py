def insertSort(arr):
    n = len(arr)
    for j in range(1,n):
        for i in range(j,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
            else:
                break
    return arr

if __name__ == "__main__":
    while True:
        # arr = [24,3,56,34,3,78,12,29,49,84,51,9,100]
        s = [int(a) for a in input().split(' ')]
        n = s[0]
        arr = s[1:]
        print(insertSort(arr), end=" ")
        print()