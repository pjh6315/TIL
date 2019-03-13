import sys

sys.stdin = open('1929.txt')


def prime(num):
    if num < 2:
        return False
    i = 2
    while i*i <=num:
        if num % i == 0:
            return False
        i+=1
    return True

m , n = map(int,input().split())



for num in range(m,n+1):
    if prime(num):
        print(num)

