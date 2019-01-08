n = int(input())

for tc in range(1,n+1):
    time = list(map(int,input().split()))
    realtime=time[0]+time[2]+(time[1]+time[3])//60
    if realtime >= 12:
        realtime = realtime % 12
        if realtime == 0:
            realtime =12
    print(f'#{tc} {realtime} {(time[1]+time[3])%60}')