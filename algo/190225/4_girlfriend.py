import sys

sys.stdin = open("girl.txt")

result = 987654321

flag = False

def dfs(now,end,now_cost):
	global result,flag
	visited[now] = 1
	if now == end:
		flag = True
		if result > now_cost:
			result = now_cost
		return
	else:
		for v in range(1,end+1):
			if visited[v] == 0 and mymap[now][v] == 1 and now_cost < result:
				dfs(v,end,now_cost+cost[now][v])
				visited[v] = 0

n,m = map(int,input().split())


visited = [0 for i in range(n+1)]
cost = [[0 for i in range(n+1)] for i in range(n+1)]
mymap = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
	y,x,temp_cost = map(int,input().split())
	mymap[y][x] = 1
	mymap[x][y] = 1
	cost[y][x] = temp_cost
	cost[x][y] = temp_cost


dfs(1,7,0)

if flag == False:
	print(-1)
else:
	print(result)
