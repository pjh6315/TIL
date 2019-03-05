def initnext(p):
    next[0] = -1
    i = 0; j = -1
    while i<len(p):
        next[i] = j#next[i] = next[j] if (p[i]==p[j] and j>=0) else j
        while((j>=0) and (p[i]!=p[j])):
            j = next[j]
        i += 1
        j += 1

def kmp_table(pattern):
    """Compute the "next" table corresponding to pattern, for use in the
    Knuth-Morris-Pratt string search algorithm.

    """
    m = len(pattern)
    next = [-1] * m
    j = -1
    for i in range(1, m):
        while j > -1 and pattern[i-1] != pattern[j]:
            j = next[j]
        j += 1
        if pattern[i] != pattern[j]:
            next[i] = j
        else:
            next[i] = next[j]
    return next

s = input()
next = [0 for i in range(len(s)+1)]
initnext(s)

print(next)

print(kmp_table(s))