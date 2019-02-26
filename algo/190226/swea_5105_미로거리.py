import sys

sys.stdin = open("5105.txt")

t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def issafe(y,x):
	global n
	if y >= 0 and y < n and x >=0 and x < n and data[y][x] != 1:
		return True
	else:
		return False

def miro(start_y,start_x):
	queue = []

	queue.append((start_y,start_x))

	while queue:
		temp = queue.pop(0)
		y = temp[0]
		x = temp[1]

		if data[y][x] != 1:
			data[y][x] = 1

		for dir in range(4):
			if issafe(y + dy[dir], x + dx[dir]) and (y + dy[dir], x + dx[dir]) not in queue:
				queue.append((y + dy[dir], x + dx[dir]))
				if distance[y + dy[dir]][x + dx[dir]] == -1:
					distance[y + dy[dir]][x + dx[dir]] = distance[y][x] + 1
				else:
					if distance[y + dy[dir]][x + dx[dir]] > distance[y][x] + 1:
						distance[y + dy[dir]][x + dx[dir]] = distance[y][x] + 1

for tc in range(1,t+1):
	n = int(input())

	distance = [[-1 for i in range(n+1)] for i in range(n+1)]

	data = []
	for i in range(n):
		data.append(list(map(int, input())))

	for y in range(n):
		for x in range(n):
			if data[y][x] == 2:
				start_y = y
				start_x = x
			elif data[y][x] == 3:
				end_y = y
				end_x = x

	miro(start_y, start_x)

	if data[end_y][end_x] == 1:
		print(f'#{tc} {distance[end_y][end_x]}')
	else:
		print(f'#{tc} 0')
