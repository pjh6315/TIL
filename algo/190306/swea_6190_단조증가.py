import sys

sys.stdin = open("6190.txt")

t = int(input())

def isincrease(num):
    if num < 10:
        return True
    else:
        while num:
            t_num = num%10
            num = num//10
            if t_num < num%10:
                return False
        return True



for tc in range(1,t+1):
    n = int(input())

    data = list(map(int,input().split()))
    mymax = -987654321
    chk = False
    for i in range(n):
        for j in range(i+1,n):
            temp = data[i] * data[j]
            if isincrease(temp):
                chk= True
                if mymax < temp:
                    mymax = temp


    if chk:
        print('#%d %d' %(tc,mymax))
    else:
        print('#%d -1' %tc)