n = int(input())

for i in range(n):
    s = input()
    if int(s[4:6]) == 2:
        if int(s[6:8]) > 0  and int(s[6:8]) <= 28:
            print(f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:8]}')
        else:
            print(f'#{i+1} -1')
    elif int(s[4:6]) == 0:
        print(f'#{i+1} -1')
    elif int(s[4:6]) == 1 or 3 or 5 or 7 or 10 or 12 or 8:
        if int(s[6:8]) > 0  and int(s[6:8]) <= 31:
            print(f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:8]}')
        else:
            print(f'#{i+1} -1')
    elif int(s[4:6]) == 4 or 6 or 9 or 11:
        if int(s[6:8]) > 0  and int(s[6:8]) <= 30:
            print(f'#{i+1} {s[0:4]}/{s[4:6]}/{s[6:8]}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')






