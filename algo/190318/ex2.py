data = '01D06079861D79F99F'
# data = '0F97A3'

new_data = ''

for num in data:
    if ord('A') <= ord(num) <= ord('F'):
        num = ord(num) - 55
    else:
        num = int(num)

    for i in range(3,-1,-1):
        if num & (1<<i):
            new_data += '1'
        else:
            new_data += '0'


print(new_data)

result = []
cnt = 0
temp = ''
for num in new_data:

    temp += num
    cnt += 1
    if cnt == 7:
        result.append(temp)
        cnt = 0
        temp = ''

if len(temp) != 0:
    result.append(temp)

print(result)

for num in result:

    my_len = len(num) - 1
    temp = 0
    for n in num:
        if n == '1':
            temp += 1<<my_len

        my_len -= 1

    print(temp,end=' ')


