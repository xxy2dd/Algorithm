'''
函数模块是：最长递增子序列
首先 输入一个数组，对数组中的每个数 1，3，6，8，7
第一个循环 对每个数                   第二个循环 对剩下的数        第三个循环
1         此时数组会先放入1                  3，6，8，7         -->   放入3，判断数组里的每个元素存放的还是数组，这个数组的最后一个值与当前放入的比较
                                                                     1 3，
                                                                     1 6 , 1 3 6
                                                                     1 8， 1 3 8， 1 6 8， 1 3 6 8
                                                                     1 7， 1 3 7， 1 6 7， 1 3 6 7
同理 3 6 8 7
得到所有的可能的递增序列，从中筛选最长的
'''

def LIS(arr):
    res = []
    for i in range(len(arr)):
        max_arr = []
        max_arr.append([arr[i]])
        for j in range(i+1,len(arr)):
            for x in range(len(max_arr)):
                if arr[j] > max_arr[x][-1]:
                    max_arr.append(max_arr[x] + [arr[j]])
        # print('{}'.format(i))
        # print(max_arr)
        for j in max_arr:
            res.append(j)
    # print(res)
    LIS_max = []
    L_max = 0
    for i in res:
        if len(i) > L_max:
            L_max = len(i)
    # print(l)
    for i in res:
        if len(i) == L_max:
            LIS_max.append(i)
    print(LIS_max)
    return LIS_max


if __name__ == '__main__':
    arr = [1,2,4,7,11,10,9,15,3,5,8,6]
    # LIS(arr)
    # arr = list(map(int, input().split()))
    arr_lefts = []
    arr_rights = []
    result_arrs = []
    for i in range(len(arr)):
        # print(arr[i])
        arr_left = arr[0:i]
        arr_right = arr[i:]
        arr_right.reverse()

        result_lefts = LIS(arr_left)
        result_rights = LIS(arr_right)

        for l in result_lefts:
            for r in result_rights:
                r.reverse()
                result_arrs.append(l + r)
    results = []
    for i in result_arrs:
        if i not in results:
            results.append(i)
    l = 0
    for i in results:
        if len(i)>l:
            l = len(i)
    for i in results:
        if len(i) == l:
            for j in i:
                print(j,end=' ')
            print("")