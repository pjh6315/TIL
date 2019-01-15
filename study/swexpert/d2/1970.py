n = int(input())

for tc in range(1,n+1):
    k = [50000,10000,5000,1000,500,100,50,10]
    money = int(input())
    print(f'#{tc} ')
    for i in range(0,8):
        print(money//k[i],end=' ')
        money = money%k[i]
    print()