t = int(input())

# 1 우하 2 좌하 3 좌상 4 우상

def solve(x,y,now,llist,path=None,start=None):
    paths = []
    if start is None:
        start = [x,y]
    
    if path is None:
        path = [llist[x][y]]
        if llist[x+1][y+1] != 0 and llist[x+1][y+1] not in path:
            temp = path + [llist[x+1][y+1]]
            paths.append(tuple(temp))
            paths.extend(solve(x+1,y+1,1,llist,temp,start))
    
    elif now == 1:
        if llist[x+1][y-1] != 0 and llist[x+1][y-1] not in path:
            temp = path + [llist[x+1][y-1]]
            paths.append(tuple(temp))
            paths.extend(solve(x+1,y-1,2,llist,temp,start))
        if llist[x+1][y+1] != 0 and llist[x+1][y+1] not in path:
            temp = path + [llist[x+1][y+1]]
            paths.append(tuple(temp))
            paths.extend(solve(x+1,y+1,1,llist,temp,start))
    
    elif now == 2:
        if llist[x-1][y-1] != 0 and llist[x-1][y-1] not in path:
            temp = path + [llist[x-1][y-1]]
            paths.append(tuple(temp))
            paths.extend(solve(x-1,y-1,3,llist,temp,start))
        if llist[x+1][y-1] != 0 and llist[x+1][y-1] not in path:
            temp = path + [llist[x+1][y-1]]
            paths.append(tuple(temp))
            paths.extend(solve(x+1,y-1,2,llist,temp,start))
    
    elif now == 3:
        if x-1 == start[0] and y+1 == start[1]:
            temp = path + [llist[x-1][y+1]]
            paths.append(tuple(temp))
        elif llist[x-1][y+1] != 0 and llist[x-1][y+1] not in path:
            temp = path + [llist[x-1][y+1]]
            paths.append(tuple(temp))
            paths.extend(solve(x-1,y+1,4,llist,temp,start))
        if llist[x-1][y-1] != 0 and llist[x-1][y-1] not in path:
            temp = path + [llist[x-1][y-1]]
            paths.append(tuple(temp))
            paths.extend(solve(x-1,y-1,3,llist,temp,start))
    
    elif now == 4:
        if x-1 == start[0] and y+1 == start[1]:
            temp = path + [llist[x-1][y+1]]
            paths.append(tuple(temp))
        elif llist[x-1][y+1] != 0 and llist[x-1][y+1] not in path:
            temp = path + [llist[x-1][y+1]]
            paths.append(tuple(temp))
            paths.extend(solve(x-1,y+1,4,llist,temp,start))

    return paths
    
        

    


for tc in range(1,t+1):
    n = int(input())
    llist = [[0]*(n+2) for i in range(n+2)]
    tlist=[]
    t_result=[]
    check = 0
    max = 0
    for i in range(n):
        tlist.append(list(map(int,input().split())))
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            llist[i][j] = tlist[i-1][j-1]

    


    for i in range(0,n-2):
        for j in range(1,n-1):
            t_result.extend(solve(i+1,j+1,1,llist))

    for k in t_result:
        
        if k[0] == k[-1]:
            check = 1
            if max < len(k):
                max = len(k)-1
    if check:
        print(f'#{tc} {max}')
    else:
        print(f'#{tc} -1')

