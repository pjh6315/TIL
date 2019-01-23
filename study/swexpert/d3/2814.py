t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    point = []
    for i in range(m):
        point.append(list(map(int,input().split())))
    
    print(point)