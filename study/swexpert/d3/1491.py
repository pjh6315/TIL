t = int(input())

def calcul(n,a,b):
    min = 10**15
    for c in range(1,int(n/2)+1):
        for r in range(c,int(n/2)+1):
            if r*c > n:
                break
            else:
                if min > a*(r-c) + b * (n-(r*c)):
                    min = a*(r-c) + b * (n-(r*c))
    return min


    

for tc in range(1,t+1):
    n,a,b = map(int,input().split())
    
    print(f'#{tc} {calcul(n,a,b)}')
