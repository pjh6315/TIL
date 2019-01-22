t = int(input())

for tc in range(1,t+1):
    n,m,k = map(int,input().split())
    man = list(map(int,input().split()))
    result = True
    eat = [0 *  i for i in range (max(man)+1)] 
    bread = [0 *  i for i in range (max(man)+1)]

    for i in man:
        eat[i] += 1

    for i in range (1,len(bread)):
        if i % m == 0:
            bread[i] += k
        bread[i] += bread[i-1]
        eat[i] += eat[i-1]

    for i in man:
        if bread[i] - eat[i] <0:
            result = False
            break
    
    if result:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
                 

    
