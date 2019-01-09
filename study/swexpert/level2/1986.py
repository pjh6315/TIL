n = int(input())

for tc in range(1,n+1):
    sum = 0
    k = int(input())
    for i in range(1,k+1):
        if i%2:
            sum += i
        else:
            sum -= i

    print(f'#{tc} {sum}')