import sys

sys.stdin = open('input.txt','r')


data = list(map(int,input().split()))

print(data)

tmax = 0

for n in data:
    if tmax < n :
        tmax = n


print(tmax)


