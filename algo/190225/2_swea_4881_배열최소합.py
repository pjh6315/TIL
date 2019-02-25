import sys

sys.stdin = open("4881.txt")

t = int(input())
ans = 987654321
data= []

def isok(now):
	temp = 0
	for i in range(1,now):
		if select[i] == select[now]:
			return False

		temp += data[i-1][select[i]-1]
		if temp > ans:
			return False

	return True

def dfs(now, end):
	global ans
	if now == end:
		temp = 0
		for i in range(1,end+1):
			temp += data[i-1][select[i]-1]
		if ans > temp:
			ans = temp
	else:
		for i in range(1,end+1):
			select[now+1] = i
			if isok(now+1):
				dfs(now+1,end)
			else:
				select[now+1] = 0
	select[now] = 0

for tc in range(1,t+1):
	n = int(input())
	ans = 987654321
	data = []

	for i in range(n):
		data.append(list(map(int,input().split())))

	for i in range(1,n+1):
		select = [0 for j in range(n+1)]
		select[1] = i
		dfs(1,n)

	print(f'#{tc} {ans}')