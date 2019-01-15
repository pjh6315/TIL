n = int(input())

for tc in range(1,n+1):
    num = int(input())
    nlist = [[0]*(num+2) for i in range(num+2)]
    
    for i in range (1,num+1):
        for j in range(1,num+1):
            nlist[i][j] = 100
            
    i = 1
    j = 1
    direction = 'right'
    for n in range (1,num**2+1):
        nlist[i][j] = n
       
        if direction == 'right':
            if nlist[i][j+1] != 100:
                direction = 'down'
                i+=1
            else:
                j+=1

        elif direction == 'left':
            if nlist[i][j-1] != 100:
                direction = 'up'
                i-=1
            else:
                j-=1
        elif direction == 'up':
            if nlist[i-1][j] != 100:
                direction = 'right'
                j+=1
            else:
                i-=1
        elif direction == 'down':
            if nlist[i+1][j] != 100:
                direction = 'left'
                j-=1
            else:
                i+=1

        
        
    print(f'#{tc}')
    for i in range (1,num+1):
        for j in range(1,num+1):
            print(nlist[i][j],end=" ")
            if j%(num) == 0:
                print()    