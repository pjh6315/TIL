# from itertools import combinations
# t = int(input())

# for tc in range(1,t+1):
#     n,r = map(int,input().split())
#     n = [i for i in range(n)]
#     t_mod = list(combinations(n,r))
#     print(f'#{tc} {len(t_mod)%1234567891}')

# 시간초과

t = int(input())

def modinv(num,mod):
    result = 1
    t_mod = mod - 2
    while t_mod != 0 :
        if t_mod%2:
            result = (result*num) % mod
        num = (num**2)%mod
        t_mod = int(t_mod/2)
    return result

for tc in range(1,t+1):
    n,r = map(int,input().split())
    p = 1234567891
    fact = [1 for i in range(n+1)]
    for i in range(1,n+1):
        fact[i] = (fact[i-1]*i)%p
    
    print(f'#{tc} {int(fact[n]*modinv(fact[n-r],p)*modinv(fact[r],p))%p}')
    
