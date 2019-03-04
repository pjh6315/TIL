a=['1','2','C','A']
for i in range(len(a)):
    if '0'<= a[i] <= '9':
        a[i]=ord(a[i])-ord('0')
    elif 'A' <= a[i] <= 'F':
        a[i] = ord(a[i])-ord('A')+10


print(a)