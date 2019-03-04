import sys

sys.stdin = open("4865.txt")

t = int(input())

for tc in range(1,t+1):
    str1 = list(map(str,input()))
    str2 = list(map(str,input()))
    mymax = 0
    for c in str1:
        temp = str2.count(c)
        if mymax < temp :
            mymax = temp

    print('#%d %d' %(tc,mymax))

