t = int(input())

for tc in range(1,t+1):
    n,k = map(int,input().split())

    a = list(map(int,input().split()))

    result = 0
    for i in range(1<<n):
        temp_sum = 0
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp_sum += a[j]
        
        if temp_sum == k:
            result += 1

    print(f'#{tc} {result}')