t = int(input())

def heapify(llist,index):
    if index == 0:
        tmax = index
        left = index * 2 + 1
        right = index * 2 + 2
        if left < len(llist) and llist[tmax] < llist[left]:
            tmax = left
        if right < len(llist) and llist[tmax] < llist[right]:
            tmax = right
        if tmax != index:
            llist[tmax], llist[index] = llist[index], llist[tmax]
            heapify(llist,tmax)
    else:
        parents = index // 2

        if llist[index] > llist[parents]:
            llist[index],llist[parents] = llist[parents],llist[index]
            heapify(llist,parents)

def hheap(tlist,llist):
    if tlist[0] == 1 :
        llist.append(tlist[1])
        heapify(llist,len(llist)-1)
    else:
        if len(llist) > 0 :
            result = llist.pop(0)
            heapify(llist,0)
            return result
        else:
            return -1

for tc in range(1,t+1):
    n = int(input()) 
    myheap = []
    result = []
    for i in range(n):
        temp = list(map(int,input().split()))
        result.append(hheap(temp,myheap))
    print(f'#{tc} ',end="")
    for n in result:
        if n is not None:
            if n != len(result)-1:
                print(n,end=" ")
            else:
                print(n)
    print()
