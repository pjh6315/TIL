import sys

sys.stdin = open('9020.txt')


maxnum = 10001
isprime = [True] * (maxnum)
isprime[1] = False

t= int(input())


def sieve():
    global maxnum
    for i in range(2,maxnum):
        if isprime[i]:
            for j in range(i*2,maxnum,i):
                isprime[j] = False

def dfs(now,sum,temp=None):
    global n,result
    if temp == None:
        temp = []
    if sum > n:
        return
    elif sum == n and len(temp) == 2:
        if temp not in result:
            result.append(temp)
    elif len(temp) > 2:
        return
    elif now < len(data):
        new_temp = []
        new_temp += temp + [data[now]]

        dfs(now,sum+data[now],new_temp)

        dfs(now+1,sum+data[now],new_temp)

        dfs(now+1,sum,temp)





sieve()
for tc in range(1,t+1):
    n = int(input())
    data = []
    result = []
    mymin = 987654321
    for i in range(2,n+1):
        if isprime[i]:
            data.append(i)


    for i in range(len(data)-1,-1,-1):
        for j in range(len(data)-1,-1,-1):
            if data[i] + data[j] == n:

    print(result)

    # dfs(0,0)
    #
    # print('%d %d' %(result[-1][0],result[-1][1]))