import sys
sys.stdin = open("input.txt")

t = int(input())
info = [0] * 128 # char 1byte ASCII code 7bit
info[ord('(')] = ')'
info[ord('{')] = '}'

temp = [')','}']

def chk(sentence):
	stack = []
	for k in sentence:
		if k == '{' or k == '(':
			stack.append(k)
		elif k in temp:
			if len(stack) == 0 :
				return 0
			elif info[ord(stack.pop())] != k:
				return 0

	if len(stack) != 0:
		return 0
	return 1



for tc in range(1,t+1):
	s = input()

	print(f'#{tc} {chk(s)}')


