
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        data =  [int(a) for a in input().split(' ')]
        a = data[0]
        b = data[1]
        c = data[2]
        print(pow(a,b)%c)