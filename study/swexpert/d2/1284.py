n = int(input())

for i in range (0,n):
    num = list(map(int,input().split()))
    p = num[0]
    q = num[1]
    r = num[2]
    s = num[3]
    w = num[4]
    money_a = p * w
    if r >= w:
        money_b = q
    else:
        money_b = q + (w - r) * s 
    
    if money_a > money_b :
        print(f'#{i+1} {money_b}')
    else:
        print(f'#{i+1} {money_a}')