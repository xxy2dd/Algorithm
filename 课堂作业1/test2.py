#Description
# Given an array of N distinct elementsA[ ],
#  find the minimum number of swaps required to sort the array.
# Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.
#
# Input
# The first line of input contains an integer T denoting the no of test cases .
# Then T test cases follow .
# Each test case contains an integer N denoting the no of element of the array A[ ].
# In the next line are N space separated values of the array A[ ] .(1<=T<=100;1<=N<=100;1<=A[] <=1000)

# Output
# For each test case in a new line output will be an integer denoting minimum umber of swaps that are required to sort the array.
def minSwaps(arr):
    n = len(arr)
    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
        # return answer
    return ans

if __name__ == "__main__":
    # Input
    # 2
    # 4
    # 4 3 2 1
    # 5
    # 1 5 4 3 2
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(a) for a in input().split(' ')]
        print(minSwaps(arr))


