import sys

sys.stdin = open("input.txt",'r')

def isSafe(y,x):
    if x >= 0 and x < 5 and y >= 0 and y < 5:
        return True
    else:
        return False

data = []

result = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    data.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dir = 0
now_x=0
now_y=0

for n in range(25):
    min_value = data[0][0]
    min_y = 0
    min_x = 0
    for y in range(5):
        for x in range(5):
            if min_value > data[y][x]:
                min_y = y
                min_x = x
                min_value = data[y][x]

    data[min_y][min_x] = 987654321
    result[now_y][now_x] = min_value

    if isSafe(now_y+dy[dir],now_x+dx[dir]) and result[now_y+dy[dir]][now_x+dx[dir]] == 0:
        now_y += dy[dir]
        now_x += dx[dir]
    else:
        dir = (dir+1)%4
        now_y += dy[dir]
        now_x += dx[dir]

for k in result:
    print(k)