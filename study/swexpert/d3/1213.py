for i in range(2):
    tc = int(input())
    check = input()
    sentence = input()
    temp = 0
    cnt = 0
    while sentence.find(check,temp) >= 0:
        cnt += 1
        temp = sentence.find(check,temp) + len(check)
        
    print(f'#{tc} {cnt}')