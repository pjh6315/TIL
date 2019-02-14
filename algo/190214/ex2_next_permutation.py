import sys

sys.stdin = open('ex2_input.txt','r')

data = list(map(int,input().split()))

def next_permutation(number):
    candi1 = candi2 = None

    for index in range(len(number)-1):
        if number[index] < number[index+1]:
            candi1 = index

    if candi1 == None:
        return False


    for index in range(len(number)-1,candi1,-1):
        if number[index] > number[candi1]:
            candi2= index
            break


    number[candi1],number[candi2] = number[candi2],number[candi1]

    number[candi1+1:] = number[:candi1:-1]

    return True


while next_permutation(data):
    print(data)



