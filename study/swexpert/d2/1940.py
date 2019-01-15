n = int(input())

for tc in range (1,n+1):
    vel = 0
    move = 0
    command = int(input())
    for i in range (0,command):
        car = list(map(int,input().split()))
        
        if car[0] == 0:
            move += abs(vel)
        elif car[0] == 1:
            vel += car[1]
            move += abs(vel)
        else:
            vel -= car[1]
            if vel <0:
                vel = 0
            move += abs(vel)
    print(f'#{tc} {move}')
