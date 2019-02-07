t= int(input())

def check (nowx,nowy,llist):
    queue = []
    # print(f'{nowx} {nowy} {llist[nowx][nowy]}')
    if llist[nowx][nowy] == '1':
        if llist[nowx-1][nowy] in ['1','2','5','6']:
            queue.append((nowx-1,nowy))
        if llist[nowx+1][nowy] in ['1','2','4','7']:
            queue.append((nowx+1,nowy))
        if llist[nowx][nowy+1] in ['1','3','6','7']:
            queue.append((nowx,nowy+1))
        if llist[nowx][nowy-1] in ['1','3','4','5']:
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '2':
        if llist[nowx-1][nowy] in ['1','2','5','6']:
            queue.append((nowx-1,nowy))
        if llist[nowx+1][nowy] in ['1','2','4','7']:
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '3':
        if llist[nowx][nowy+1] in ['1','3','6','7']:
            queue.append((nowx,nowy+1))
        if llist[nowx][nowy-1] in ['1','3','4','5']:
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '4':
        if llist[nowx-1][nowy] in ['1','2','5','6']:
            queue.append((nowx-1,nowy))
        if llist[nowx][nowy+1] in ['1','3','6','7']:
            queue.append((nowx,nowy+1))
        llist[nowx][nowy] = '9'   

    if llist[nowx][nowy] == '5':
        if llist[nowx][nowy+1] in ['1','3','6','7']:
            queue.append((nowx,nowy+1))
        if llist[nowx+1][nowy] in ['1','2','4','7']:
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '6':
        if llist[nowx][nowy-1] in ['1','3','4','5']:
            queue.append((nowx,nowy-1))
        if llist[nowx+1][nowy] in ['1','2','4','7']:
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '7':
        if llist[nowx-1][nowy] in ['1','2','5','6']:
            queue.append((nowx-1,nowy))
        if llist[nowx][nowy-1] in ['1','3','4','5']:
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'
        

    # for i in llist:
    #     print(i)
    # print(queue)
    return queue


for tc in range(1,t+1):
    n,m,r,c,l = map(int,input().split())
    llist = [['0'] * (m+2) for i in range(n+2)]
    tlist= []
    result = []
    temp = []
    for i in range(n):
        tlist.append(input().split())

    for i in range(1,n+1):
        for j in range(1,m+1):
            llist[i][j]= tlist[i-1][j-1]
    
    r = r+1
    c = c+1

    # for i in llist:
    #     print(i)
    # print()
    for i in range(l):
        if i == 0 :
            temp.extend(check(r,c,llist))
        else:
            temp2 = temp[:]
            for k in temp2:
                temp.extend(check(k[0],k[1],llist))
                temp.pop(0)
            # print(temp)

    cnt = 0 
    for i in range(1,n+1):
        for j in range(1,m+1):
            if llist[i][j]== '9':
                cnt += 1
   
    print(f'#{tc} {cnt}')