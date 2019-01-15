n = int(input())

for tc in range(1,n+1):
    k = int(input())
    count = 0
    print(f'#{tc}')
    for i in range(k):
        alpha = input().split()
        for j in range(int(alpha[1])):
            if count == 9 :
                print(alpha[0])
                count = 0
            else:
                print(alpha[0],end="")
                count += 1
    print()        