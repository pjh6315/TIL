n = int(input())

for i in range (0,n):
    num = list(map(int,input().split()))
    print(f'#{i+1} {max(num)}')