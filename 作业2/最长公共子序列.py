'''
最长公共子序列
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
Input
输入为两行，一行一个字符串
Output
输出如果有多个则分为多行，先后顺序不影响判断。
Sample Input 1
1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1
23G456K
23G45JK
'''
def LCS(X,Y):
    len1 = len(X)+1
    len2 = len(Y)+1
    C = [[0 for j in range(len2)] for i in range(len1)]
    B = [[0 for j in range(len2)] for i in range(len1)]

    for i in range(1,len1):
        for j in range(1,len2):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1]+1
                B[i][j] = 'LeftTop'
            elif C[i-1][j]>C[i][j-1]:
                C[i][j] = C[i-1][j]
                B[i][j] = 'Top'
            elif C[i-1][j]<C[i][j-1]:
                C[i][j] = C[i][j-1]
                B[i][j] = 'Left'
            else:
                C[i][j] = C[i][j - 1]
                B[i][j] = 'LeftOrTop'
    maxLen = C[len(X)][len(Y)]
    result = ""
    printLCS(B,1,maxLen,len(X),len(Y),X,Y,result)

def printLCS(B,curLen,maxLen,i,j,X,Y,result):
    if i == 0 or j == 0:
        return result_dic
    if B[i][j] == 'LeftTop':
        if curLen == maxLen:
            result += X[i-1]
            result_dic[result] = i-1
        elif curLen<maxLen:
            result += X[i - 1]
            printLCS(B,curLen+1,maxLen,i-1,j-1,X,Y,result)
    elif B[i][j] == 'Left':
        printLCS(B, curLen, maxLen, i , j - 1, X, Y, result)
    elif B[i][j] == 'Top':
        printLCS(B, curLen , maxLen, i-1 , j, X, Y, result)
    elif B[i][j] == 'LeftOrTop':
        printLCS(B, curLen, maxLen, i , j - 1, X, Y, result)
        printLCS(B, curLen, maxLen, i -1, j , X, Y, result)

if __name__ == "__main__":
    X =list("1A2BD3G4H56JK")
    Y = list("23EFG4I5J6K7")
    # X = list(input())
    # Y = list(input())
    result_dic = dict()
    LCS(X,Y)
    for res in result_dic.keys():
        print(res)

