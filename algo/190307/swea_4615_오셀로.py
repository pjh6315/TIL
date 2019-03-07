import sys

sys.stdin = open('4615.txt')

dy = [-1,1,0,0,-1,-1,1,1]
dx = [0,0,-1,1,-1,1,-1,1]

t = int(input())

def finish():
    global n
    white = 0
    black = 0
    for y in range(1,n+1):
        for x in range(1,n+1):
            if mymap[y][x] == 1:
                black +=1
            elif mymap[y][x] == 2:
                white +=1

    return (black,white)

def issafe(y,x):
    global n
    if y >= 1 and y <= n and x >= 1 and x <= n :
        return True
    else:
        return False

def play(y,x,color):
    if mymap[y][x] != 0:
        return
    else:

        # 상 하 좌 우 좌상 우상 좌하 우하
        for dir in range(8):
            chk = False
            next_y = y + dy[dir]
            next_x = x + dx[dir]
            if issafe(next_y,next_x) and mymap[next_y][next_x] != 0:
                while issafe(next_y,next_x):
                    if mymap[next_y][next_x] == color:
                        chk = True
                    elif mymap[next_y][next_x] == 0:
                        chk = False
                        break
                    else:
                        next_y = next_y + dy[dir]
                        next_x = next_x + dx[dir]

                    if chk == True:
                        break

            if chk:
                while True:
                    if next_y == y and next_x == x :
                        break
                    next_y -= dy[dir]
                    next_x -= dx[dir]
                    mymap[next_y][next_x] = color
                mymap[y][x] = color








for tc in range(1,t+1):
    n,m = map(int,input().split())

    mymap = [[0 for i in range(n+1)] for i in range(n+1)]

    mymap[n//2+1][n//2+1] = 2
    mymap[n // 2][n // 2] = 2
    mymap[n // 2][n // 2+1] = 1
    mymap[n // 2+1][n // 2] = 1

    player = []

    for i in range(m):
        player.append(list(map(int,input().split())))

    for i in range(m):
        y = player[i][0]
        x = player[i][1]
        color = player[i][2]
        play(y,x,color)
        # for x in mymap:
        #     print(x)
        # print('==================================================================')
    ans = finish()
    print('#%d %d %d' %(tc,ans[0],ans[1]))

