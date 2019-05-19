 # Description
#
# Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}. If frequencies of two elements are same, print them in increasing order.
#
#
# Input
#
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.（1 ≤ T ≤ 70；30 ≤ N ≤ 130；1 ≤ A [ i ] ≤ 60 ）
#
#
# Output
#
# Print each sorted array in a seperate line. For each array its numbers should be seperated by space

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
    # Input
    # 1
    # 5
    # 5 5 4 6 4
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(a) for a in input().split(' ')]
        arr_sorted = sortByCounts(arr, N)
        for m in arr_sorted:
            print(m, end=" ")
        print()
