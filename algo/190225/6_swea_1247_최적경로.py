import sys

sys.stdin = open("1247.txt")

t= int(input())



def dfs(now,end,dis,cnt):
	global result
	if cnt == 5:
		move = abs(now[0]-end[0]) + abs(now[1] - end[1])
		dis += move
		if result > dis:
			result = dis
	else:
		for p in range(1,len(point)):
			if visited[p] == 0 and dis < result:
				move = abs(now[0]-point[p][0]) + abs(now[1] - point[p][1])
				dfs(point[p],end,dis+move,cnt+1)



for tc in range(1,t+1):
	n = int(input())
	result = 987654321
	data = list(map(int,input().split()))
	visited = [0 for i in range(n+1)]
	point = [0]

	start = (data[0],data[1])
	end = (data[2],data[3])


	for i in range(4,len(data),2):
		point.append((data[i],data[i+1]))

	dfs(start,end,0,0)
	print(f'#{tc} {result}')


