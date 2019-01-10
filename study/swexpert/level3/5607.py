from itertools import combinations
t = int(input())

for tc in range(1,t+1):
    n,r = map(int,input().split())

    temp = combinations(n,r)
    print(temp)

