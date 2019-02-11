t = int(input())

for tc in range(1,t+1):
    n,k = map(int,input().split())

    mt = []

    for i in range(n):
        mt.append(list(map(int,input().split())))

    print(mt)