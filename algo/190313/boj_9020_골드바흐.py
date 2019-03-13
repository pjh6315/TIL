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

def dfs(now,sum):
    global n,result

    if sum > n:
        return
    elif sum == n:





sieve()
for tc in range(1,t+1):
    n = int(input())
    temp = []
    result = []
    for i in range(2,n+1):
        if isprime[i]:
            temp.append(i)

    def(0,0)