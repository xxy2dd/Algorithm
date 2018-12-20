
def first(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2;  # (low + high)/2;
        if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        if (x > arr[mid]):
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid - 1), x, n)

    return -1


# Sort A1[0..m-1] according to the order
# defined by A2[0..n-1].
def sortAccording(A1, A2, m, n):

    temp = [0] * m
    visited = [0] * m

    for i in range(0, m):
        temp[i] = A1[i]
        visited[i] = 0

    # Sort elements in temp
    temp.sort()

    # for index of output which is sorted A1[]
    ind = 0

    for i in range(0, n):

        # Find index of the first occurrence
        # of A2[i] in temp
        f = first(temp, 0, m - 1, A2[i], m)

        # If not present, no need to proceed
        if (f == -1):
            continue

        # Copy all occurrences of A2[i] to A1[]
        j = f
        while (j < m and temp[j] == A2[i]):
            A1[ind] = temp[j];
            ind = ind + 1
            visited[j] = 1
            j = j + 1

    # Now copy all items of temp[] which are
    # not present in A2[]
    for i in range(0, m):
        if (visited[i] == 0):
            A1[ind] = temp[i]
            ind = ind + 1


# Utility function to print an array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print("")

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N =  [int(a) for a in input().split(' ')]
        N1 = N[0]
        N2 = N[1]
        arr1 = [int(a) for a in input().split(' ')]
        arr2 = [int(a) for a in input().split(' ')]
        sortAccording(arr1,arr2,N1,N2)
        printArray(arr1,N1)

