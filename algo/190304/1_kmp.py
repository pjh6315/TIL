target = 'abc abcdab abcdabcdabde'
pattern = 'abcdabd'

pi = [0 for i in range(len(pattern))]
pi[0] = -1

i = 0
j = 1
while j < len(pattern) -1:
    if pattern[i] != pattern[j]:
        if pattern[0] == pattern[j]:
            pi[j+1] = pi[j]
        else:
            pi[j+1] = 0
            i = 0
        j += 1
    elif pattern[i] == pattern[j]:
        pi[j+1] = pi[j] + 1
        i += 1
        j += 1

print(pi)

p = 0

while p < len(target):
    cnt = 0
    for i in range(len(pattern)):
        if pattern[i] == target[p+i]:
            cnt += 1
        else:
            break

    if cnt == len(pattern):
        break
    else:
        p += cnt - pi[cnt]


print(p)

