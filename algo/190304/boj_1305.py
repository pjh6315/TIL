n = int(input())

pattern = input()

pi = [0 for i in range(len(pattern)+1)]
pi[0] = -1

i = 0
j = 1
while j < len(pattern) :
    if pattern[i] != pattern[j]:
        i = 0
        if pattern[i] == pattern[j]:
            pi[j+1] = 1
            i += 1
            j += 1
        else:
            pi[j+1] = 0
            j += 1
    elif pattern[i] == pattern[j]:
        pi[j+1] = pi[j] + 1
        i += 1
        j += 1

print(pi)

print(n-pi[n])