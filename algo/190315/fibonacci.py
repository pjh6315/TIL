fibo = [-1] * 10100

fibo[0] = 0
fibo[1] = 1

for now in range(2,1010):
    fibo[now] = fibo[now-1] + fibo[now -2]


print(fibo[1000])

def getsome(num):
    if fibo[num] == -1:
        fibo[num] = getsome(num-1) + getsome(num-2)
        return fibo[num]
    else:
        return fibo[num]


print(getsome(1000))