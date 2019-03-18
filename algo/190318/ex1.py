import sys

sys.stdin = open('ex1_input.txt')


def change(n):

    result = 0
    i = 6
    for num in n :
        if num == '1':
            result += 1 << i
        i -= 1


    return result

data = list(map(str,input().split()))



new_data = []
cnt = 0
temp = ''
for n in data:

    for c in n:
        temp += c
        cnt += 1

        if cnt == 7:
            cnt = 0
            new_data.append(temp)
            temp = ''

print(new_data)

# for n in new_data:
#     change(n)
for n in new_data:
    print(change(n),end=' ')


