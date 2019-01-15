n = int(input())

for tc in range(1,n+1):
    k = int(input())
    num = list(map(int,input().split()))

    num.sort()

    print(f'#{tc} ',end='')
    for i in num:
        print(i,end=' ')
    print()