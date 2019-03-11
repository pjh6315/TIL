import sys

sys.stdin = open('2819.txt')

t = int(input())
result = []

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def issafe(y,x):
    if 0 <= y < 4 and 0<=x<4:
        return True
    else:
        return False

def dfs(now_y,now_x,cnt,temp=None):
    if temp == None:
        temp = []
    if cnt == 6:
        temp += [data[now_y][now_x]]
        if temp not in result:
            result.append(temp)

    else:
        for dir in range(4):
            next_y = now_y + dy[dir]
            next_x = now_x + dx[dir]
            if issafe(next_y,next_x):
                new_temp = temp + [data[now_y][now_x]]
                dfs(next_y,next_x,cnt+1,new_temp)



for tc in range(1,t+1):
    data = []

    for i in range(4):
        data.append(list(map(int,input().split())))


    for y in range(4):
        for x in range(4):
            dfs(y,x,0)

    print('#%d %d' %(tc,len(result)))