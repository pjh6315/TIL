import sys

sys.stdin = open("4861.txt")

t = int(input())

def find_pelin(data,length,nn):
    # 가로
    for y in range(nn):
        for x in range(0,nn-length+1):
            temp = data[y][x:x+length]
            if temp == temp[::-1]:
                return temp
    # 세로

    t_data = [[0 for i in range(nn)] for i in range(nn)]

    for y in range(nn):
        for x in range(nn):
            t_data[y][x] = data[x][y]

    for y in range(nn):
        for x in range(0,nn-length+1):
            temp = t_data[y][x:x+length]
            if temp == temp[::-1]:
                return ''.join(temp)



    # 세로

for tc in range(1,t+1):
    n,m = map(int,input().split())

    pel = []

    for i in range(n):
        pel.append(input())

    print('#{} {}' .format(tc,find_pelin(pel,m,n)))
