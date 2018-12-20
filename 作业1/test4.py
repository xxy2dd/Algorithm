# 汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。
# 求当有N层塔的时候移动步数。
# Input：输入的第一行为N。
# Output: 移动步数。
# -*- coding:utf-8 -*-
# import datetime
def hanoi(n):
    if n==1:
        return 2
    else:
        return hanoi(n-1)*3+2

if __name__ == '__main__':
    # begin=datetime.datetime.now()
    # n=2
    n=int(input())
    print(hanoi(n))
    # end=datetime.datetime.now()
    # print(end-begin)