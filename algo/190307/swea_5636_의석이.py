import sys

sys.stdin = open('5636.txt')

t = int(input())

for tc in range(1,t+1):
    data = []
    mydata=[[0 for i in range(15)] for i in range(5)]
    for i in range(5):
        data.append(list(input()))

    for y in range(5):
        end = len(data[y])
        for x in range(end):
            mydata[y][x] = data[y][x]
    print('#%d' %tc,end=' ')
    for x in range(15):
        for y in range(5):
            if mydata[y][x] != 0:
                print('%s' %mydata[y][x],end='')

    print()