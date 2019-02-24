import sys
sys.stdin = open("input_1224.txt")


for tc in range(1,11):
	length = int(input())

	stack = []
	result = []

	data = input()

	for s in data:
		if s not in ['(',')','+','-','*','/']:
			result.append(s)
		else:
			if len(stack) == 0:
				stack.append(s)
			elif s == '(' or s == '*' or s == '/':
				stack.append(s)
			elif s == '+' or s == '-':
				if stack[-1] == '*' or stack[-1] == '/':
					while len(stack) != 0 and stack[-1] == '*' or stack[-1] == '/' :
						result.append(stack.pop())
				stack.append(s)
			elif s == ')':
				while len(stack) != 0 and stack[-1] != '(':
					result.append(stack.pop())
				stack.pop()


	new_stack = []
	for s in result:
		if s not in ['+', '-', '*', '/']:
			new_stack.append(int(s))
		else:
			a = new_stack.pop()
			b = new_stack.pop()
			if s == '+':
				new_stack.append(b+a)
			elif s == '-':
				new_stack.append(b-a)
			elif s == '*':
				new_stack.append(b*a)
			elif s == '/':
				new_stack.append(b/a)

	print(f'#{tc} {new_stack[0]}')