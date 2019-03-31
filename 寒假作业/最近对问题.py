# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/30 14:51
@description:
"""
# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/1/30 14:51
@description:
"""
def nearestPoint(x,y):
    min =  pow(float(x[0])-float(x[1]),2)+pow(float(y[0])-float(y[1]),2)
    count = 1
    result = []
    for i in range(0,len(x)):
        for j in range(i+1,len(y)):
            dist = pow(float(x[i])-float(x[j]),2)+pow(float(y[i])-float(y[j]),2)
            if dist < min:
                min = dist
                count = 1
                result = []
                if len(result) != 0:
                    result.append(",")
                result.append(x[i])
                result.append(" ")
                result.append(y[i])
                result.append(",")
                result.append(x[j])
                result.append(" ")
                result.append(y[j])
            elif dist == min:
                count += 1
                if len(result)!=0:
                    result.append(",")
                result.append(x[i])
                result.append(" ")
                result.append(y[i])
                result.append(",")
                result.append(x[j])
                result.append(" ")
                result.append(y[j])
    return result
if __name__ =="__main__":
    n = int(input())
    for i in range(n):
        x = []
        y = []
        str = input().split(",")
        # print(str)
        for j in str:
            temp = j.split(" ")
            x.append(temp[0])
            y.append(temp[1])
    # print(x,y)
    print("".join(i for i in nearestPoint(x,y)))