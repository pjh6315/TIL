t = int(input())

for tc in range(1,t+1):
    n = int(input())
    num = list(map(int,input().split()))
    ans = 0
    temp = 0

    for i in range (0,n):
        temp = max(temp,0) + num[i]
        ans = max(temp,ans)

    print(f'#{tc} {ans}')



