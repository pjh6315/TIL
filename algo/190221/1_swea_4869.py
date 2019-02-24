

t = int(input())

def paper(n):
	if n == 10:
		return 1
	elif n == 20:
		return 3
	else:
		return paper(n-20)*2 + paper(n-10)

for tc in range(1,t+1):
	n = int(input())

	print(f'#{tc} {paper(n)}')