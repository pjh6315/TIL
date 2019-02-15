t = int(input())


for tc in range(1,t+1):
    k,n,m = map(int,input().split())

    chk = True

    bus_stop = list(map(int,input().split()))

    for index in range(m):
        if index == 0 and bus_stop[index] > k:
            chk = False
        else:
            if bus_stop[index] - bus_stop[index-1] > k :
                chk = False


    if chk == False:
        print(f'#{tc} 0')
    else:
        max_move = k
        result = 0
        for index in range(len(bus_stop)):
            if bus_stop[index] > max_move:
                result += 1
                max_move = bus_stop[index-1] + k

        if max_move < n :
            result +=1

        print(f'#{tc} {result}')

