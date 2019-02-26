import sys

sys.stdin = open("5102.txt")

t = int(input())

def bfs(start,end):
	global v
	queue = []
	queue.append(start)

	while queue:
		a = queue.pop(0)
		visited[a] = 1
		for next in range(1,v+1):
			if visited[next] == 0 and mymap[a][next] == 1 and next not in queue:
				queue.append(next)
				distance[next] = distance[a] + 1


for tc in range(1,t+1):

	v , e = map(int,input().split())
	mymap = [[0 for i in range(v+1)] for i in range(v+1)]
	distance = [0 for i in range(v+1)]
	visited = [0 for i in range(v+1)]
	for i in range(e):
		y,x = map(int,input().split())
		mymap[y][x] = 1
		mymap[x][y] = 1



	s, g = map(int,input().split())
	bfs(s,g)
	print(f'#{tc} {distance[g]}')