import sys
sys.stdin = open("input_4874.txt")

t = int(input())

def calcul(data):
	new_stack = []
	for s in data:
		if s not in ['+', '-', '*', '/', '.']:
			new_stack.append(int(s))
		else:
			if s == '.':
				break
			elif len(new_stack) <= 1:
				return False
			a = new_stack.pop()
			b = new_stack.pop()
			if s == '+':
				new_stack.append(b + a)
			elif s == '-':
				new_stack.append(b - a)
			elif s == '*':
				new_stack.append(b * a)
			elif s == '/':
				new_stack.append(int(b / a))

	if len(new_stack) == 1:
		return new_stack[0]
	else:
		return False

for tc in range(1,t+1):
	data = list(map(str,input().split()))


	if calcul(data):
		print(f'#{tc} {calcul(data)}')
	else:
		print(f'#{tc} error')