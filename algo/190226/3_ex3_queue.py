import sys

sys.stdin = open("ex3.txt")



def bfs(now):
	queue = []

	queue.append(now)
	while queue:
		temp = queue.pop(0)
		print(temp,end=' ')
		if not visited[temp]:
			visited[temp] = 1

		for i in range(1,8):
			if not visited[i] and mymap[temp][i] == 1 and i not in queue:
				queue.append(i)


data = list(map(int,input().split()))
mymap = [[0 for i in range(8)] for i in range(8)]

visited = [0 for i in range(8)]

for i in range(0,len(data),2):
	mymap[data[i]][data[i+1]] = 1
	mymap[data[i+1]][data[i]] = 1

bfs(1)