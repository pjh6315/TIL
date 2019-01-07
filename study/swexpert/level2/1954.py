n = int(input())

def move(direction,i,j):
    if direction == 'right':
        j+=1
    elif direction == 'left':
        j-=1
    elif direction == 'up':
        i+=1
    elif direction == 'down':
        i-=1


for tc in range(1,n+1):
    num = int(input())
    nlist = [[0]*(num+2) for i in range(num+2)]
    
    for i in range (1,num+2):
        for j in range(1,num+2):
            nlist[i][j] = 5
    for i in range (0,num+3):
        for j in range(0,num+3):
            print(nlist[i][j])
    i = 1
    j = 1
    # direction = 'right'
    # for n in range (1,num**2+1):
    #     nlist[i][j] = n
    #     if nlist[i+1][j] 

        