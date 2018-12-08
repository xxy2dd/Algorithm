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