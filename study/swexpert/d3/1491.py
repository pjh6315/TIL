t = int(input())

def calcul(n,a,b,r,c):
    if n >= r*c:
        return a*(r-c)+b*(n-(r*c))
    else:
        return a*(r-c)+b*(n-(r*(c-1)))

for tc in range(1,t+1):
    n,a,b = map(int,input().split())

    new_n = int(n**0.5)

    r = new_n
    c = new_n - 1
    
    print(f'#{tc} {min(calcul(n,a,b,r,c),calcul(n,a,b,r,r),calcul(n,a,b,c+2,r))}')
