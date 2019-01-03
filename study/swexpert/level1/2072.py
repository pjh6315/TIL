n = int(input())

for i in range (0,n):
    sum = 0
    num = list(map(int,input().split()))

    for j in num:
        if j%2 ==1 :
            sum += j

    print(f'#{i+1} {sum}')