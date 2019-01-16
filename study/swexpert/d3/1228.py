for tc in range(1,11):
    n = input()
    pw = list(map(int,input().split()))
    ins = int(input())
    llist = input().split('I')
    real=[]
    for i in range(1,ins+1):
        real.append(llist[i].split())
    for i in range(ins):
        for j in range(int(real[i][1])):
            pw.insert(int(real[i][0])+j,real[i][2+j])

    print(f'#{tc}',end=' ')
    for i in range(10):
        print(pw[i],end=' ')
    print()