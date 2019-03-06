import sys

sys.stdin = open("4751.txt")


t = int(input())

for tc in range(1,t+1):
    mystr = input()

    n = len(mystr)

    no1 = '.'
    no2 = '.'
    no3 = '#'

    for i in range(n):
        no1 += '.#..'
        no2 += '#.#.'
        no3 += '.' + mystr[i] + '.#'

    print(no1)
    print(no2)
    print(no3)
    print(no2)
    print(no1)