import math
a=1
b=2
cnt=0
print(f'{a} < √2 < {b}')
while True:
    
    if a**2 < 2 and 2 < ((b+a)/2)**2:
        b=(b+a)/2
    else:
        a=(b+a)/2
    cnt+=1
    print(f'{a} < √2 < {b}')
    if math.floor(a*1000000) / 1000000 == math.floor(b*1000000) / 1000000:
        break
    

    
    