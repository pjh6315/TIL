import sys

sys.stdin = open('1211.txt')

dy = [-1,1,0,0]
dx = [0,0,-1,1]



def issafe(y,x):
    if y>= 0 and y <=99 and x >= 0 and x<=99 and data[y][x] == 1:
        return True
    else:
        return False
# dir 1 하 2 좌 3 우
def miro(start,y,x,dir,cnt=0):
    global result,result_x
    if y == 99 :
        if result > cnt :
            result = cnt
            result_x = start
    else:
        # data[y][x] = 9
        if (dir == 1 or dir == 3) and issafe(y,x+1):
            miro(start,y,x+1,3,cnt+1)
        elif (dir == 1 or dir == 2) and issafe(y,x-1):
            miro(start,y,x-1,2,cnt+1)
        elif issafe(y+1,x):
            miro(start,y+1,x,1,cnt+1)
        else:
            return



for tc in range(1,11):
    data= []
    t = input()
    result_x = -1
    result = 987654321
    for i in range(100):
        data.append(list(map(int,input().split())))

    for i in range(100):
        if data[0][i] == 1:
            miro(i,0,i,1)


    print('#%d %d' %(tc,result_x))
