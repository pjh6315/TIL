n = int(input())

for tc in range(1,n+1):
    day = int(input())
    result = 0
    max = 0
    money = list(map(int,input().split()))

    for i in range(day-1,-1,-1):
        if max < money[i]:
            max = money[i]
        else:
            result += max - money[i]
    

    print(f'#{tc} {result}')
