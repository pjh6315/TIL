



def initnext(p):
    next[0] = -1
    i = 0; j = -1
    while i<len(p):
        next[i] = j#next[i] = next[j] if (p[i]==p[j] and j>=0) else j
        while((j>=0) and (p[i]!=p[j])):
            j = next[j]
        i += 1
        j += 1

s = input()
next = [0 for i in range(len(s))]
initnext(s)

print(next)