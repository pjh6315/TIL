t = int(input())

for tc in range(1,t+1):
    n = int(input())

    number = input()
    counts = [0] * 10

    for n in number:
        counts[int(n)] +=1

    max = counts[0]
    max_index = 0
    for index in range(10):
        if max <= counts[index]:
            max = counts[index]
            max_index = index

    print(f'#{tc} {max_index} {max}')