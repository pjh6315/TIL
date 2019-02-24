import sys
sys.stdin = open("ex1.txt")

t = int(input())
for tc in range(1,t+1):
	data = input()

	stack1= []
	result = []

	for s in data:
		if s in ['+','-','*','/']:
			stack1.append(s)

		else:
			result.append(s)

	while stack1:
		result.append(stack1.pop())


	print(''.join(result))
