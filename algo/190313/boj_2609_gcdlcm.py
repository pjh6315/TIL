import sys

sys.stdin = open('2609.txt')


def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b,gcd):
    return (a*b)//gcd




a, b = map(int,input().split())

my_gcd = gcd(a,b)

my_lcm = lcm(a,b,my_gcd)

print(my_gcd)
print(my_lcm)
