import sys

sys.stdin = open("1767.txt")

t = int(input())

def isok(llist,y,x,dir):
    global n
    # 상 하 좌 우
    if dir == 1:
        for yy in range(0,y):
            if llist[yy][x] != 0:
                return False
    elif dir == 2:
        for yy in range(y+1,n):
            if llist[yy][x] != 0:
                return False
    elif dir == 3:
        for xx in range(0,x):
            if llist[y][xx] != 0:
                return False
    elif dir == 4:
        for xx in range(x+1,n):
            if llist[y][xx] != 0:
                return False
    return True
def dfs(llist,now,line,cnt):
    global n
    if now == len(core):
        return line
    else:





for tc in range(1,t+1):
    n = int(input())

    data = []
    core = []

    for i in range(n):
        data.append(list(map(int,input().split())))

    for y in range(n):
        for x in range(n):
            if data[y][x] == 1 and y != 0 and x != 0:
                core.append((y,x))

    print(core)
