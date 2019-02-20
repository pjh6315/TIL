import sys
sys.stdin = open("input.txt")

def isok(wow):
    stack = []
    info = [0] * 128 # char 1byte ASCII code 7bit
    info[ord('(')] = ')'
    info[ord('{')] = '}'
    info[ord('[')] = ']'
    info[ord('<')] = '>'
    for k in wow:
        if k == '(' or k == '{' or k == '[' or k == '<':
            stack.append(k)
        elif len(stack) == 0:
            return False
        elif k != info[ord(stack.pop())]:
            return False

    if len(stack) == 0:
        return True
    else:
        return False




for tc in range(5):
    data = input()

    if isok(data):
        print('ok')
    else:
        print('no')




