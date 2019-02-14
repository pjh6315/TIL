
data = list(map(int,input().split()))


def baby_gen(number):

    counts = [0] * 10
    run = 0
    triplet = 0

    for n in number:
        counts[n] += 1


    for i in range(len(counts)):
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1

        if counts[i] >= 1 and counts[i+1] >=1 and counts[i+2] >=1 :
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1

    if triplet + run == 2:
        return True
    else:
        return False


print(baby_gen(data))