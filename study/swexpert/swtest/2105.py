t = int(input())

def dfs(p,llist,visited=None,path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []
    x = x+1
    y = y+1
    visited.append((x,y))



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