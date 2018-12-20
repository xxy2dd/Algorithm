def sortByCounts(arr,N):
    index = [0]*60
    arr_new = [0]*N
    for i in arr:
        index[i]=index[i]+1
    index_temp = index[:]
    index =sorted(index, reverse=True)
    i = 0
    for m in index:
        if m==0:
            break
        for n in range(0,len(index_temp)):
            if m == index_temp[n]:
                while index_temp[n] >= 1:
                    arr_new[i] = n
                    i=i+1
                    index_temp[n]=index_temp[n]-1
    return arr_new


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(a) for a in input().split(' ')]
        arr_sorted = sortByCounts(arr, N)
        for m in arr_sorted:
            print(m, end=" ")
        print()
