import sys

sys.stdin = open("input.txt",'r')

t = int(input())

def paint(p1_x,p1_y,p2_x,p2_y,c,result):
    for y in range(p1_y,p2_y+1):
        for x in range(p1_x,p2_x+1):
            if result[y][x] == 0 or result[y][x] == c:
                result[y][x] = c
            else:
                result[y][x] = 3

def find_color(result):
    cnt = 0
    for y in range(10):
        for x in range(10):
            if result[y][x] == 3:
                cnt +=1

    return cnt

for tc in range(1,t+1):
    n = int(input())

    area = []

    result = [[0 for i in range(10)] for i in range(10) ]

    for i in range(n):
        area.append(list(map(int,input().split())))


    for point in area:
        paint(point[0],point[1],point[2],point[3],point[4],result)

    print(f'#{tc} {find_color(result)}')