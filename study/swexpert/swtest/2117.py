t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())

house = []

for i in range(n):
    house.append(list(map(int,input().split())))

print(house)