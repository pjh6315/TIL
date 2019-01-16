n = int(input())

for tc in range (1,n+1):
    num = int(input())
    num_list = [2,3,5,7,11]
    count = [0,0,0,0,0]

    for i in range(5):
        while num%num_list[i] == 0:
            count[i] += 1
            num /= num_list[i]
    
    print(f'#{tc} {count[0]} {count[1]} {count[2]} {count[3]} {count[4]}')