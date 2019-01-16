t = int(input())

for tc in range(1,t+1):
    money, n = map(str,input().split())
    cha_m= []
    if len(money) == 1 :
        ans  = money
    else:
        for i in range(int(n)):
            length = len(cha_m)
            if i == 0:
                for j in range(0,len(money)-1):
                    for k in range(j+1,len(money)):
                        temp = []
                        temp = list(money)
                        temp[j],temp[k] = temp[k], temp[j]
                        cha_m.append(temp)
                        kkk = set(cha_m)
                        cha_m = list(kkk)
            else:
                for o in range(length):
                    a=cha_m.pop(0)
                    for j in range(0,len(a)-1):
                        for k in range(j+1,len(a)):
                            temp = []
                            temp = list(a)
                            temp[j],temp[k] = temp[k], temp[j]
                            cha_m.append(temp)
                            kkk = set(cha_m)
                            cha_m = list(kkk)
            

    final = []
    for d in range(0,len(cha_m)):
        final.append(int(''.join(cha_m[d])))
    print(f'#{tc} {max(final)}')