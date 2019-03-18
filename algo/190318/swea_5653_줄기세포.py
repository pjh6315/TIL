import sys

sys.stdin = open('5653.txt')

t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def issafe(y,x):
    if data[y][x] == 0:
        return True
    else:
        return False

for tc in range(1,t+1):
    n, m ,k = map(int,input().split())

    grid = []

    data = [[0 for i in range(800)] for i in range(800)]

    live = []

    live_time = []

    wait = []

    wait_time = []

    temp = []

    temp_time = []

    for y in range(n):
        temp = list(map(int,input().split()))

        for x in range(len(temp)):
            ty = y + 400
            tx = x + 400
            data[ty][tx] = temp[x]
            if temp[x] != 0:
                wait.append((ty,tx))
                wait_time.append(temp[x])


    for time in range(k):
        temp = []

        temp_time = []
        if live:
            for i in range(len(live)):
                for dir in range(4):
                    new_y = live[i][0] + dy[dir]
                    new_x = live[i][1] + dx[dir]
                    if issafe(new_y,new_x):
                        temp.append((new_y,new_x))
                        temp_time.append(data[live[i][0]][live[i][1]])
                live_time[i] -= 1

            for i in range(len(live)):
                if live_time[i] == 0:
                    live.pop(i)
                    live_time.pop(i)

            for i in range(len(temp)):
                y = temp[i][0]
                x = temp[i][1]

                if data[y][x] < temp_time[i]:
                    data[y][x] = temp_time[i]
                    wait.append((y,x))
                    wait_time.append(temp_time[i])
        temp = []


        for i in range(len(wait)):
            y = wait[i][0]
            x = wait[i][1]

            wait_time[i] -= 1

            if wait_time[i] == 0:
                live.append((y,x))
                live_time.append(data[y][x])



    print(live)
    print(live_time)
    print(wait)
    print(wait_time)