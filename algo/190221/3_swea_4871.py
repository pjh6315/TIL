import sys
sys.stdin = open("input.txt")

t = int(input())



def node_check(node,start,end,visited):
	visited.append(start)
	next = []


	for p in node:
		if start == p[0] and p[1] not in visited:
			next.append(p)

	if len(next) == 0:
			return
	else:
		for p in next:
			node_check(node,p[1],end,visited)


for tc in range(1,t+1):
	v , e = map(int,input().split())

	node = []
	visited = []

	for i in range(e):
		node.append(tuple(map(int,input().split())))

	s, g = map(int,input().split())

	node_check(node,s,g,visited)

	print(visited)

	if g in visited:
		print(f'#{tc} 1')
	else:
		print(f'#{tc} 0')