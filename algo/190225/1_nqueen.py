

t = int(input())

queen = []
ans = 0


def isqueen(r):
	for i in range(1, r):
		if queen[i] == queen[r]:
			return False
		elif abs(queen[i] - queen[r]) == abs(i - r):
			return False
	return True


def dfs(now, n):
	global ans
	if now == n:
		ans += 1
	else:
		for i in range(1, n + 1):
			queen[now + 1] = i
			if isqueen(now + 1):
				dfs(now + 1, n)
			else:
				queen[now + 1] = 0
	queen[now] = 0


for tc in range(1, t + 1):
	n = int(input())
	ans = 0
	for i in range(1, n + 1):
		queen = [0 for i in range(11)]
		queen[1] = i
		dfs(1, n)
	print(f'#{tc} {ans}')
