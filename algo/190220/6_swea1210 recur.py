import sys
sys.stdin = open("input.txt")

dy = [-1,1,0,0]
dx = [0,0,1,-1]
dir = 0

def issafe(y,x):

    if y>= 0 and y <=99 and x >= 0 and x<=99:
        return True
    else:
        return False

def find_start(data,now_y,now_x):
    global dir
    if now_y == 0:
        return now_x
    else:
        if issafe(now_y,now_x+1) and dir == 0 and data[now_y][now_x+1] == 1:
            dir = 2
        elif issafe(now_y,now_x-1) and dir == 0 and data[now_y][now_x-1] == 1:
            dir = 3
        elif issafe(now_y-1,now_x) and dir == 2 and data[now_y-1][now_x] == 1:
            dir = 0
        elif issafe(now_y-1,now_x) and dir == 3 and data[now_y-1][now_x] == 1:
            dir = 0

        now_x += dx[dir]
        now_y += dy[dir]

    return find_start(data,now_y,now_x)


for tc in range(1,11):
    t= input()
    data = []
    now_x = 0
    now_y = 0

    for i in range(100):
        data.append(list(map(int, input().split())))

    for i in range(100):
        if data[99][i] == 2:
            now_x = i
            now_y = 99



    print(f'#{tc} {find_start(data,now_y,now_x)}')