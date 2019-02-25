import copy
import sys

sys.stdin = open("input.txt")

t = int(input())
ans = []


def destroy(i, j, num, brick, width, height):
	des_queue = []
	brick[i][j] = 0
	# up, left , right , down
	for k in range(1, num):
		if i - k >= 0:
			des_queue.append((i - k, j))
		if j - k >= 0:
			des_queue.append((i, j - k))
		if j + k <= width - 1:
			des_queue.append((i, j + k))
		if i + k <= height - 1:
			des_queue.append((i + k, j))

	for gu in des_queue:
		destroy(gu[0], gu[1], brick[gu[0]][gu[1]], brick, width, height)


def reset(brick, width, height):
	for i in range(width):
		temp = []
		for j in range(height - 1, -1, -1):
			if brick[j][i] != 0:
				temp.append(brick[j][i])
		for j in range(height - 1, -1, -1):
			if len(temp) > 0:
				brick[j][i] = temp.pop(0)
			else:
				brick[j][i] = 0
	return brick


def bomb(now, cnt, brick, width, height, n):
	t_y=t_x=0
	if cnt == n :
		brick_cnt = 0
		for y in range(height):
			for x in range(width):
				if brick[y][x] != 0:
					brick_cnt += 1
		ans.append(brick_cnt)
		return
	elif now < width:
		for y in range(height):
			if brick[y][now] != 0:
				t_y = y
				t_x = now
				break
		bomb(now+1,cnt,brick,width,height,n)
		temp = copy.deepcopy(brick)
		destroy(t_y,t_x,temp[t_y][t_x],temp,width,height)
		reset(temp,width,height)
		bomb(now,cnt+1,temp,width,height,n)




for tc in range(1, t + 1):
	n, w, h = map(int, input().split())
	ans = []
	brick = []

	for i in range(h):
		brick.append(list(map(int, input().split())))
	# for i in brick:
	# 	print(i)
	# print('=================================')
	# destroy(1, 2, 1, brick, w, h)
	# reset(brick, w, h)
	# for i in brick:
	# 	print(i)
	# print('=================================')
	# destroy(2, 2, 3, brick, w, h)
	# reset(brick, w, h)
	# for i in brick:
	# 	print(i)
	# print('=================================')
	# destroy(8, 6, 2, brick, w, h)
	# reset(brick, w, h)
	# for i in brick:
	# 	print(i)
	# print('=================================')


	bomb(0, 0, brick, w, h, n)

	print(f'#{tc} {min(ans)}')
	print(ans)
	print(len(ans))