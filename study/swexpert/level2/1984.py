n = int(input())

for tc in range(1,n+1):
    num = list(map(int,input().split()))
    num.remove(max(num))
    num.remove(min(num))
    print(f'#{tc} {int(round(sum(num)/8,0))}')