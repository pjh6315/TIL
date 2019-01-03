n = int(input())

for tc in range (1,n+1):
    vel = 0
    move = 0
    command = int(input())
    for i in range (0,command):
        car = list(map(int,input().split()))
        
        if car[0] == 0:
            move += vel
        elif car[0] == 1:
            vel += car[1]
            move += vel
        else:
            vel -= car[1]
            move += vel
    print(move)
