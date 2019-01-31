t= int(input())

def check (nowx,nowy,llist):
    queue = []
    print(f'{nowx} {nowy} {llist[nowx][nowy]}')
    if llist[nowx][nowy] == '1':
        if llist[nowx-1][nowy] == '1' or '2' or '5' or '6':
            queue.append((nowx-1,nowy))
        if llist[nowx+1][nowy] == '1' or '2' or '4' or '7':
            queue.append((nowx+1,nowy))
        if llist[nowx][nowy+1] == '1' or '3' or '6' or '7':
            queue.append((nowx,nowy+1))
        if llist[nowx][nowy-1] == '1' or '3' or '4' or '5':
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '2':
        if llist[nowx-1][nowy] == '1' or '2' or '5' or '6':
            queue.append((nowx-1,nowy))
        if llist[nowx+1][nowy] == '1' or '2' or '4' or '7':
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '3':
        if llist[nowx][nowy+1] == '1' or '3' or '6' or '7':
            queue.append((nowx,nowy+1))
        if llist[nowx][nowy-1] == '1' or '3' or '4' or '5':
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '4':
        if llist[nowx-1][nowy] == '1' or '2' or '5' or '6':
            queue.append((nowx-1,nowy))
        if llist[nowx][nowy+1] == '1' or '3' or '6' or '7':
            queue.append((nowx,nowy+1))
        llist[nowx][nowy] = '9'   

    if llist[nowx][nowy] == '5':
        if llist[nowx][nowy+1] == '1' or '3' or '6' or '7':
            queue.append((nowx,nowy+1))
        if llist[nowx+1][nowy] == '1' or '2' or '4' or '7':
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '6':
        if llist[nowx][nowy-1] == '1' or '3' or '4' or '5':
            queue.append((nowx,nowy-1))
        if llist[nowx+1][nowy] == '1' or '2' or '4' or '7':
            queue.append((nowx+1,nowy))
        llist[nowx][nowy] = '9'

    if llist[nowx][nowy] == '7':
        if llist[nowx-1][nowy] == '1' or '2' or '5' or '6':
            queue.append((nowx-1,nowy))
        if llist[nowx][nowy-1] == '1' or '3' or '4' or '5':
            queue.append((nowx,nowy-1))
        llist[nowx][nowy] = '9'
        

    for i in llist:
        print(i)
    print()
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

    for i in llist:
        print(i)
    print()
    for i in range(l):
        if i == 0 :
            temp.extend(check(r,c,llist))
            result.append((r,c))
        else:
            temp2 = temp[:]
            for k in temp2:
                temp.extend(check(k[0],k[1],llist))
                result.append(temp.pop())

    # for i in llist:
    #     print(i)
    print(list(set(result)))
   