import sys

sys.stdin = open('6109.txt')

t = int(input())

def reset(dir):
	global n
	if dir == 'up':
		for x in range(n):
			temp = []
			for y in range(n):
				if data[y][x] != 0 :
					temp.append(data[y][x])
			temp.append(0)
			new_temp=[]
			for index in range(len(temp)-1):
				if temp[index] == temp[index+1]:
					new_temp.append(temp[index] * 2)
					temp[index+1] = 0
				elif temp[index] != 0:
					new_temp.append(temp[index])


			for y in range(n):
				if new_temp:
					data[y][x] = new_temp.pop(0)
				else:
					data[y][x] = 0

	elif dir == 'down':
		for x in range(n):
			temp = []
			for y in range(n-1,-1,-1):
				if data[y][x] != 0:
					temp.append(data[y][x])
			temp.append(0)
			new_temp = []
			for index in range(len(temp) - 1):
				if temp[index] == temp[index + 1]:
					new_temp.append(temp[index] * 2)
					temp[index + 1] = 0
				elif temp[index] != 0:
					new_temp.append(temp[index])

			for y in range(n-1,-1,-1):
				if new_temp:
					data[y][x] = new_temp.pop(0)
				else:
					data[y][x] = 0
	elif dir == 'right':
		for y in range(n):
			temp = []
			for x in range(n-1,-1,-1):
				if data[y][x] != 0:
					temp.append(data[y][x])
			temp.append(0)
			new_temp = []
			for index in range(len(temp) - 1):
				if temp[index] == temp[index + 1]:
					new_temp.append(temp[index] * 2)
					temp[index + 1] = 0
				elif temp[index] != 0:
					new_temp.append(temp[index])

			for x in range(n-1,-1,-1):
				if new_temp:
					data[y][x] = new_temp.pop(0)
				else:
					data[y][x] = 0
	else:
		for y in range(n):
			temp = []
			for x in range(n):
				if data[y][x] != 0:
					temp.append(data[y][x])
			temp.append(0)
			new_temp = []
			for index in range(len(temp) - 1):
				if temp[index] == temp[index + 1]:
					new_temp.append(temp[index] * 2)
					temp[index + 1] = 0
				elif temp[index] != 0:
					new_temp.append(temp[index])

			for x in range(n):
				if new_temp:
					data[y][x] = new_temp.pop(0)
				else:
					data[y][x] = 0
for tc in range(1,t+1):
	n, s = input().split()
	n = int(n)

	data = []

	for i in range(n):
		data.append(list(map(int,input().split())))


	reset(s)

	print('#%d' %tc)

	for y in range(n):
		for x in range(n):
			if x != n-1:
				print('%d' %data[y][x], end = ' ')
			else:
				print('%d' %data[y][x])






