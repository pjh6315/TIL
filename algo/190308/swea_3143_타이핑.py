import sys

sys.stdin = open('3143.txt')

t = int(input())

for tc in range(1,t+1):
	a, b = input().split()

	cnt = a.count(b)

	new = a.replace(b,'')

	cnt += len(new)

	print('#%d %d' %(tc,cnt))