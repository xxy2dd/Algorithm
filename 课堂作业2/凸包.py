import copy
def dealleft(first,final,lis,temp):
    max = 0
    index = -1
    if first<final:
        for i in range(first,final):
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i
    else:
        for i in range(final,first):
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i
    if index!=-1:
        temp[index] = 1
        dealleft(first,index,lis,temp)
        dealleft(index,final,lis,temp)

def divide(lis,n):
    temp = {}
    lis_con_new = []
    if n==3:
        return lis
    for i in range(n):
        temp[i] = 0
    lis_con = copy.deepcopy(lis)
    lis_con.sort()
    temp[0] = 1
    temp[n-1] = 1
    dealleft(0,n-1,lis_con,temp)
    dealleft(n-1,0,lis_con,temp)
    for i in temp:
        if temp[i] == 1:
            lis_con_new.append(lis_con[i])
    return lis_con_new

if __name__ == "__main__":
    lis = [1,2,3,1,5,6]
    n = 6
    divide(lis,n)
