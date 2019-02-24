import sys
sys.stdin = open("input_4875.txt")

t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]
data=[]

def issafe(y,x,length):
	if y >= 0 and y < length and x >=0 and x < length and data[y][x] != 1:
		return True
	else:
		return False

def miro(start_y,start_x,end_y,end_x):
	data[start_y][start_x] = 1

	if start_y == end_y and start_x == end_x:
		return
	else:
		for dir in range(4):
			if issafe(start_y+dy[dir],start_x+dx[dir],len(data[0])):
				miro(start_y+dy[dir],start_x+dx[dir],end_y,end_x)



for tc in range(1,t+1):
	n = int(input())
	data = []

	for i in range(n):
		data.append(list(map(int,input())))

	for y in range(5):
		for x in range(5):
			if data[y][x] == 2:
				start_y = y
				start_x = x
			elif data[y][x] == 3:
				end_y = y
				end_x = x

	miro(start_y,start_x,end_y,end_x)

	if data[end_y][end_x] == 1:
		print(f'#{tc} 1')
	else:
		print(f'#{tc} 0')