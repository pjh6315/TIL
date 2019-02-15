t = int(input())

for tc in range(1,t+1):
    n = int(input())

    number = list(map(int,input().split()))

    print(f'#{tc} {max(number)-min(number)}')