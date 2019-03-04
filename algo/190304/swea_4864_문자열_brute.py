import sys

sys.stdin = open("4864.txt")

t = int(input())

def brute_f(target,pattern):
    p = 0
    while p < len(target) - len(pattern) + 1:
        cnt = 0
        for i in range(len(pattern)):
            if pattern[i] == target[p+i]:
                cnt += 1
            else:
                break

        if cnt == len(pattern):
            return True
        else:
            p += 1

    return False


for tc in range(1,t+1):
    pattern = input()
    target = input()

    if brute_f(target,pattern):
        print('#%d 1' % tc)
    else:
        print('#%d 0' % tc)