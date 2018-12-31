
def quickSort(arr,l,r):
    if l >= r:
        return
    stack = [l,r]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high <= low:
            continue
        pivot = arr[high]
        i = low -1
        for j in range(low,high+1):
            if arr[j] <= pivot:
                i+=1
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
        stack.extend([low,i-1,i+1,high])
    return arr
if __name__ == '__main__':
    try:
        while True:
            # arr = [24,3,56,34,3,78,12,29,49,84,51,9,100]
            s = [int(a) for a in input().split(' ')]
            n = s[0]
            arr = s[1:]
            print(quickSort(arr,0,n-1), end=" ")
            print()
    except EOFError:
        pass
