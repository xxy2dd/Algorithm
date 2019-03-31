# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/20 20:31
@description:
"""

def ChessBoard(tr, tc, pr, pc, size):
    '''
    :param lx: 已知的L型格子的一个的x坐标
    :param ly: 已知的L型格子的一个的y坐标
    :param pr: 特殊方格的x坐标
    :param pc: 特殊方格的y坐标
    :param size: 棋盘尺寸
    :return:
    '''
    row_size = pow(2, k)  # 棋盘的边长
    global table
    global mark
    mark += 1
    count = mark
    if size == 1:
        return
    half = size // 2
    # 处理左上部分
    if pr < tr + half and pc < tc + half:
        ChessBoard(tr, tc, pr, pc, half)
    else:
        table[tr + half - 1][tc + half - 1] = count
        ChessBoard(tr, tc, tr + half - 1, tc + half - 1, half)
    #处理右上部分
    if pr < tr + half and pc >= tc + half:
        ChessBoard(tr, tc + half, pr, pc, half)
    else:
        table[tr + half - 1][tc + half] = count
        ChessBoard(tr, tc + half, tr + half - 1, tc + half, half)
    #处理左下部分
    if pr >= tr + half and pc < tc + half:
        ChessBoard(tr + half, tc, pr, pc, half)
    else:
        table[tr + half][tc + half - 1] = count
        ChessBoard(tr + half, tc, tr + half, tc + half - 1, half)
    # 处理右下部分
    if pr >= tr + half and pc >= tc + half:
        ChessBoard(tr + half, tc + half, pr, pc, half)
    else:
        table[tr + half][tc + half] = count
        ChessBoard(tr + half, tc + half, tr + half, tc + half, half)
    return table


def show(table,lx,ly):
    result=''
    n = len(table)
    for i in range(n):
        for j in range(n):
            if i == lx and j == ly:
                continue
            if table[i][j]==table[lx][ly] :
                result += str(i)+" "+str(j)+","
    print(result[:len(result)-1])




if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        arr = [int(a) for a in input().split(" ")]
        k = arr[0]
        point_s = arr[1:] #特殊方块的位置
        point_n = [int(a) for a in input().split(" ")] #已知的L型格子的一个坐标
        row_size = pow(2, k)
        mark = 0
        table = [[-1 for n in range(row_size)] for n in range(row_size)]  # 初始化棋盘
        table_l = ChessBoard(0,0,point_s[0],point_s[1],row_size)
        show(table_l,point_n[0],point_n[1])


