import sys

sys.stdin = open("5431.txt")

t = int(input())

for tc in range(1,t+1):

    student, hw = map(int,input().split())

    hw_check = [0 for i in range(student+1)]

    data = list(map(int,input().split()))

    for k in data:
        hw_check[k] = 1

    print('#%d' %tc,end='')
    for i in range(1,len(hw_check)):
        if hw_check[i] == 0 :
            print(' %d' %i,end='')

    print()