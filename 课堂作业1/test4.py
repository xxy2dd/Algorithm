count = 0
def InversePairs(data):
    global count
    def MergeSort(lists):
        global count
        if len(lists) <= 1:
            return lists
        num = int(len(lists) / 2)
        left = MergeSort(lists[:num])
        right = MergeSort(lists[num:])
        r, l = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
                count += len(left) - l
        result += right[r:]
        result += left[l:]
        return result
    MergeSort(data)
    return count


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        data = [int(a) for a in input().split(' ')]
        print(InversePairs(data))
