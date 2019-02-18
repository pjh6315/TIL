import sys

sys.stdin = open("input.txt",'r')

# input
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

def isSafe(y,x):
    if x>=0 and x < 5 and y >=0 and y< 5:
        return True
    else:
        return False

def my_cal(a,b):
    if a - b >= 0:
        return a-b
    else:
        return -(a-b)

data = [[0 for _ in range(5)] for _ in range(5)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
sum = 0



for i in range(5):
    data[i] = list(map(int,input().split()))

for y in range(5):
    for x in range(5):
        for dir in range(4):
                new_y = y + dy[dir]
                new_x = x + dx[dir]
                if isSafe(new_y,new_x):
                    sum += my_cal(data[new_y][new_x],data[y][x])


print(data)
print(sum)