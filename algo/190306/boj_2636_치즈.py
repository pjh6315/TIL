import sys

sys.stdin = open("2636.txt")

dy = [-1,1,0,0]
dx = [0,0,-1,1]

next_cheese = []
ans= 0
hour=0

def isok(y,x):
    global yy,xx
    if y >=0 and y < yy and x >=0 and x < xx:
        return True
    else:
        return False

def can_disappear(y,x):
    for dir in range(4):
        t_y = y + dy[dir]
        t_x = x + dx[dir]
        if cheese[t_y][t_x] == 9 :
            return True
    return False

def air(y,x):
    global yy,xx
    visited = [[0 for i in range(xx)] for i in range(yy)]
    queue = []

    queue.append((y,x))

    while queue:
        t = queue.pop(0)
        now_y = t[0]
        now_x = t[1]
        cheese[now_y][now_x] = 9
        visited[now_y][now_x] = 1
        for dir in range(4):
            next_y = now_y + dy[dir]
            next_x = now_x + dx[dir]
            if isok(next_y,next_x) and visited[next_y][next_x] == 0 and (next_y,next_x) not in queue:
                if cheese[next_y][next_x] == 0 or cheese[next_y][next_x] == 9:
                    queue.append((next_y,next_x))










    # if y==0 and x == 0:
    #     cheese[y][x] = 9
    #     cheese[yy-1][xx-1] = 9
    #     air(1,0)
    #     air(0,1)
    # elif y==yy-1 and x==xx-1:
    #     return
    # else:
    #     cheese[y][x] = 9
    #     for dir in range(4):
    #         next_y = y + dy[dir]
    #         next_x = x + dx[dir]
    #         # if cheese[next_y][next_x] == 1 and can_disappear(next_y,next_x) and (next_y,next_x) not in next_cheese:
    #         #     next_cheese.append((next_y,next_x))
    #         if isok(next_y,next_x):
    #             if cheese[next_y][next_x] == 0:
    #                 air(next_y,next_x)
    #             if cheese[next_y][next_x] == 1 and (next_y,next_x) not in next_cheese:
    #                 next_cheese.append((next_y,next_x))

def mycount():
    global yy,xx
    cnt = 0
    for y in range(yy):
        for x in range(xx):
            if cheese[y][x] == 1:
                cnt += 1
    return cnt




def disappear():
    global yy,xx,ans,hour

    while True :
        hour += 1
        cnt = 0
        next_cheese = []
        air(0,0)

        for y in range(yy):
            for x in range(xx):
                if cheese[y][x] == 1:
                    cnt += 1
                    if can_disappear(y,x):
                        next_cheese.append((y,x))
        if cnt != 0 :
            ans = cnt
        else:
            break

        for che in next_cheese:
            cheese[che[0]][che[1]] = 9

        # for k in cheese:
        #     print(k)
        # print('-----------------------')
        # print(next_cheese)
        # print(len(next_cheese))


    return


yy , xx = map(int,input().split())

cheese = []

for y in range(yy):
    cheese.append(list(map(int,input().split())))

disappear()
# air(0,0)
# for k in cheese:
#     print(k)
# print('-----------------------')
print(hour-1)
print(ans)
