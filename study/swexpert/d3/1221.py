t = int(input())
numdict = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
rev_numdict= {0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}
for tc in range(1,t+1):
    a,b = map(str,input().split())
    llist = list(map(str,input().split()))
    temp = []
    ans = []
    for num in llist:
        temp.append(numdict[num])

    temp.sort()
    
    for num in temp:
        ans.append(rev_numdict[num])
    print(f'#{tc}')
    print(' '.join(ans))