import sys

sys.stdin = open('4948.txt')

maxnum = 123456*2 + 1
isprime = [True] * (300000)
isprime[1] = False
def prime(num):
    if num < 2:
        return False
    i = 2
    while i*i <=num:
        if num % i == 0:
            return False
        i+=1
    return True

def sieve():
    global maxnum
    for i in range(2,maxnum+1):
        if isprime[i]:
            for j in range(i*2,maxnum+1,i):
                isprime[j] = False
sieve()
while True:
    n = int(input())
    cnt = 0
    if n == 0 :
        break
    else:

        for num in range(n+1,2*n+1):
            if isprime[num]:
                cnt+=1

        print(cnt)

