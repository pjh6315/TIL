for tc in range(1,11):
    n = input()
    num = list(map(int,input().split()))
    minus = [1,2,3,4,5]
    i=0
    while num[7] > 0 :
        a=num.pop(0)
        a -= minus[i%5]
        i+=1
        if a<0:
            a=0
        num.append(a)

    
    print(f'#{tc}',end=" ")
    for a in num:
        print(a,end=" ")
    print()

