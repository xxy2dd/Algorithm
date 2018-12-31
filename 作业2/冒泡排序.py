def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
if __name__ == "__main__":
    while True:
        # arr = [24,3,56,34,3,78,12,29,49,84,51,9,100]
        s = [int(a) for a in input().split(' ')]
        n = s[0]
        arr = s[1:]
        print(bubbleSort(arr), end=" ")
        print()