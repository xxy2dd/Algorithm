def  merge(seq,low,mid,high):
    left = seq[low:mid]
    right = seq[mid:high]
    i = 0
    j = 0
    result = []
    while i<len(left) and j <len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    seq[low:high] = result
    return seq
def mergeSort(seq):
    i = 1
    while i<len(seq):
        low = 0
        while i+low<len(seq):
            mid = low +i
            high = mid+i
            if len(seq)<high:
                high=len(seq)
            result= merge(seq,low,mid,high)
            low = high
        i *= 2
    return result

if __name__ == '__main__':
    try:
        while True:
        # arr = [24,3,56,34,3,78,12,29,49,84,51,9,100]
            s = [int(a) for a in input().split(' ')]
            n = s[0]
            arr = s[1:]
            print(mergeSort(arr))
            print()
    except EOFError:
        pass



