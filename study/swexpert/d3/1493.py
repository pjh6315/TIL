t = int(input())

def wow(x):
    n=1
    while (n**2-n+2)/2 <= x :
        n+=1
    i = int(x - (((n-1)**2-(n-1)+2)/2))  

    return 1+i,n-1-i

def rev_wow(x,y):
    n= x+y-1
    i = (n**2-n+2)/2

    return int(i+x-1)

    
    
for tc in range(1,t+1):
    p,q = map(int,input().split())
    
    p = wow(p)
    q = wow(q)

    print(f'#{tc} {rev_wow(p[0]+q[0],p[1]+q[1])}')

