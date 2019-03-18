# data = '0DEC'
data = '0269FAC9A0'

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
password = {'001101':'0','010011':'1','111011':'2','110001':'3','100011':'4','110111':'5','001011':'6','111101':'7','011001':'8','101111':'9'}
i = 0
result = []
while i < len(new_data) - 6:
    temp = new_data[i:i+6]

    if temp in password:
        result.append(password[temp])
        i = i+6
    else:
        i = i+1

print(result)

