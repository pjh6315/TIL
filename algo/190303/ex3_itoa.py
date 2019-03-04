a=12456

result = ''

for c in str(a):
    c = int(c)
    result = result + chr(c+ord('0'))

print(result)