n = int(input())

for tc in range (1,n+1):
    man = int(input())
    min_st = 100000
    cnt = 0
    stone = list(map(int,input().split()))
    for k in stone:
        if abs(k) < min_st:
            min_st = abs(k)
    for k in stone:
        if abs(k) == min_st:
            cnt += 1
    print(f'#{tc} {min_st} {cnt}')