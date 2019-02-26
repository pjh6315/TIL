import sys

sys.stdin = open("5097.txt")

t = int(input())

for tc in range(1,t+1):
	n,m = map(int,input().split())

	data = list(map(int,input().split()))

	for i in range(m):
		data.append(data.pop(0))


	print(f'#{tc} {data[0]}')