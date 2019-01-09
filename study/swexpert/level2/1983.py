n = int(input())

for tc in range(1,n+1):
    n,k = map(int,input().split())
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    score=[]
    for i in range(n):
        temp = []
        temp = list(map(int,input().split()))
        score.append(temp[0]*0.35+temp[1]*0.45+temp[2]*0.2)
    my_score = score[k-1]
    score.sort(reverse=True)
    print(f'#{tc} {grade[score.index(my_score)//(int(n/10))]}')