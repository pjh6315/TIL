def up(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return up(n-1) + up(n-2)

n = int(input())


print(up(n))
