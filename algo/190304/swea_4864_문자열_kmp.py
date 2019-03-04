import sys

sys.stdin = open("4864.txt")

def kmp(target,pattern):
    pi = [0 for i in range(len(pattern))]
    pi[0] = -1

    i = 0
    j = 1
    while j < len(pattern) - 1:
        if pattern[i] != pattern[j]:
            if pattern[0] == pattern[j]:
                pi[j + 1] = pi[j]
            else:
                pi[j + 1] = 0
                i = 0
            j += 1
        elif pattern[i] == pattern[j]:
            pi[j + 1] = pi[j] + 1
            i += 1
            j += 1
    p = 0
    print(pi)
    while p < len(target)-len(pattern) +1:
        cnt = 0
        for i in range(len(pattern)):
            if pattern[i] == target[p + i]:
                cnt += 1
            else:
                break

        if cnt == len(pattern):
            return True
        else:
            p += cnt - pi[cnt]

    return False

t = int(input())

for tc in range(1,t+1):
    pattern = input()
    target = input()

    if kmp(target,pattern):
        print('#%d 1' %tc)
    else:
        print('#%d 0' %tc)
