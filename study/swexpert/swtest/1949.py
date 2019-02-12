t = int(input())

def longest(start,mt,n,length=1):
    x = start[0]
    y = start[1]
    c = 0
    
    l1,l2,l3,l4=0,0,0,0

    # 상
    if x - 1 >= 0 and mt[x-1][y] < mt[x][y]:
        c = 1
        l1 = longest((x-1,y),mt,n,length+1)
    # 하
    if x + 1 < n and mt[x+1][y] < mt[x][y]:
        c = 1
        l2 = longest((x+1,y),mt,n,length+1)
    # 좌
    if y - 1 >= 0 and mt[x][y-1] < mt[x][y]:
        c = 1
        l3 = longest((x,y-1),mt,n,length+1)
    # 우
    if y + 1 < n and mt[x][y+1] < mt[x][y]:
        c = 1
        l4 = longest((x,y+1),mt,n,length+1)

    if c == 0:
        return length
    else:
        return max(l1,l2,l3,l4)

for tc in range(1,t+1):
    n,k = map(int,input().split())

    mt = []
    high = []
    max_value = 0

    for i in range(n):
        mt.append(list(map(int,input().split())))

    for m in mt:
        t = max(m)
        if max_value < t:
            max_value = t

    for index,value in enumerate(mt):
        for index2,value2 in enumerate(value):
            if value2 == max_value:
                high.append((index,index2))

    max_value = 0
    for x in high:
        for i in range(n):
            for j in range(n):
                for t in range(0,k+1):
                    mt[i][j] -= t
                    wow = longest(x,mt,n)
                    mt[i][j] += t
                    if max_value < wow:
                        max_value = wow

    print(f'#{tc} {max_value}')
