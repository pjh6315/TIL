t = int(input())

# 1 우하 2 좌하 3 좌상 4 우상

def dfs(x,y,now,llist,path=None):
    x = x+1
    y = y+1
    paths = []
    if path is None:
        path = [llist[x][y]]
        paths.extend(dfs(x+1,y+1,1,llist,path))
    
    if now == 1:
        if llist[x+1][y+1] != 0:
            dfs(x+1,y+1,1,llist,path)
    

    


for tc in range(1,t+1):
    n = int(input())
    llist = [[0]*(n+2) for i in range(n+2)]
    tlist=[]

    for i in range(n):
        tlist.append(list(map(int,input().split())))
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            llist[i][j] = tlist[i-1][j-1]

    print (llist)