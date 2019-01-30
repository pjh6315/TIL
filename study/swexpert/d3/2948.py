import bisect
t = int(input())

for tc in range(1,t+1):
    n,m = input().split()

    llist1 = input().split()
    llist2 = input().split()

    ans = 0
    llist1.sort()
    llist2.sort()
    if len(llist1) >= len(llist2):
        a = llist1
        b = llist2
    else:
        a = llist2
        b = llist1


    for k in b:
        if bisect.bisect(a,k) > 0:
            ans += 1       
        
    print(f'#{tc} {ans}')