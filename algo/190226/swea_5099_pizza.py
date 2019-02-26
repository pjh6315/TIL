import sys

sys.stdin = open("5099.txt")

t = int(input())

for tc in range(1,t+1):
	n, m = map(int,input().split())

	cheese = list(map(int,input().split()))
	fire = []
	for i in range(m):
		cheese[i] = [i+1,cheese[i]]

	for i in range(n):
		fire.append(cheese.pop(0))

	
	while len(fire) > 1:
		pizza = fire.pop(0)

		pizza[1] = pizza[1] // 2

		if pizza[1] != 0 :
			fire.append(pizza)
		else:
			if len(cheese)>0:
				fire.append(cheese.pop(0))



	print(f'#{tc} {fire[0][0]}')
