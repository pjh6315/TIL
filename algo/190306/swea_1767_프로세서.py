import sys

sys.stdin = open("1767.txt")

t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def isok(llist,y,x,dir):
    global n
    # 상 하 좌 우
    temp = {}
    if dir == 0:
        for yy in range(0,y):
            temp.append((y,x))
            if llist[yy][x] != 0:
                return False
    elif dir == 1:
        for yy in range(y+1,n):
            temp.append((y, x))
            if llist[yy][x] != 0:rn
                return False
    elif dir == 2:
        for xx in range(0,x):
            temp.append((y, x))
            if llist[y][xx] != 0:
                return False
    elif dir == 3:
        for xx in range(x+1,n):
            temp.append((y, x))
            if llist[y][xx] != 0:
                return False
    return temp

def dfs(llist,now,line,cnt,select_list=None):
    global n
    if select_list == None:
        select_list = {}

    if now == len(core):
        result.append((line,cnt))
    else:
        for dir in range(4):
            a = isok(llist,core[now][0],core[now][1],dir)
            if a != False:
                





for tc in range(1,t+1):
    n = int(input())

    data = []
    core = []
    result =[]
    for i in range(n):
        data.append(list(map(int,input().split())))

    for y in range(n):
        for x in range(n):
            if data[y][x] == 1 and y != 0 and x != 0:
                core.append((y,x))

    print(core)
