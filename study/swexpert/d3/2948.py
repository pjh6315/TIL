import bisect

t = int(input())

def binary_search(arr,x):
    i = bisect.bisect_left(arr,x)
    return i < len(arr) and arr[i] == x

for tc in range(1,t+1):
    n,m = input().split()

    llist1 = input().split()
    llist2 = input().split()

    ans = 0
    llist1.sort()
    llist2.sort()
   

 
    for s in llist1:
        if binary_search(llist2,s):
            ans+=1
        




    print(f'#{tc} {ans}')