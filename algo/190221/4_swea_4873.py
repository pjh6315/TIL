import sys
sys.stdin = open("input.txt")

t = int(input())

def delete(my_str):
	stack = []

	for index in range(len(my_str)):
		if len(stack) == 0:
			stack.append(index)
		elif my_str[stack[-1]] == my_str[index]:
			my_str[stack[-1]] = ''
			my_str[index] = ''
			stack.pop()
		else:
			stack.append(index)


	return len(my_str) - my_str.count('')




for tc in range(1,t+1):
	my_str = list(map(str,input()))


	print(f'#{tc} {delete(my_str)}')
