for tc in range(1,11):
    n = input()
    t_list = []
    llist = [[0]*100 for i in range(100)]
    cnt = 0
    for i in range(100):
        t_list.append(input().split())

    for i in range(100):
        for j in range(100):
            if t_list[j][i] != '0' :
                llist[i][j]=t_list[j][i]
            else:
                llist[i][j]=''
           
    temp = []
    for i in range(100):
        temp.append(''.join(llist[i]))
    for i in range(100):
        strtemp=0
        while temp[i].find('12',strtemp) >= 0:
            cnt += 1
            strtemp = temp[i].find('12',strtemp) + len('12')
    print(f'#{tc} {cnt}')


