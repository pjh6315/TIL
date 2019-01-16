for tc in range(1,11):
    n = input()
    pw = list(map(int,input().split()))
    ins = int(input())
    num = input().split()
    check=0
    insert_list=[]
    delete_list=[]
    add_list=[]
    for number in num:
        if number == 'I':
            if len(insert_list) != 0 :
                for i in range(int(insert_list[1])):
                    pw.insert(int(insert_list[0])+i,insert_list[2+i])
                    
            elif len(delete_list) != 0:
                for i in range(int(delete_list[1])):
                    pw.pop(int(delete_list[0]))
            elif len(add_list) != 0 :
                for i in range(int(add_list[0])):
                    pw.append(add_list[1+i])
            insert_list=[]
            delete_list=[]
            add_list=[]
            check=1
        elif number == 'D':
            if len(insert_list) != 0 :
                for i in range(int(insert_list[1])):
                    pw.insert(int(insert_list[0])+i,insert_list[2+i])
                    
            elif len(delete_list) != 0:
                for i in range(int(delete_list[1])):
                    pw.pop(int(delete_list[0]))
            elif len(add_list) != 0 :
                for i in range(int(add_list[0])):
                    pw.append(add_list[1+i])
            insert_list=[]
            delete_list=[]
            add_list=[]
            check=2
        elif number =='A':
            if len(insert_list) != 0 :
                for i in range(int(insert_list[1])):
                    pw.insert(int(insert_list[0])+i,insert_list[2+i])
                    
            elif len(delete_list) != 0:
                for i in range(int(delete_list[1])):
                    pw.pop(int(delete_list[0]))
            elif len(add_list) != 0 :
                for i in range(int(add_list[0])):
                    pw.append(add_list[1+i])
            insert_list=[]
            delete_list=[]
            add_list=[]
            check =3
        else:
            if check == 1:
                insert_list.append(number)
            elif check ==2:
                delete_list.append(number)
            elif check ==3:
                add_list.append(number)

    if len(insert_list) != 0 :
        for i in range(int(insert_list[1])):
            pw.insert(int(insert_list[0])+i,insert_list[2+i])
                    
    elif len(delete_list) != 0:
        for i in range(int(delete_list[1])):
            pw.pop(int(delete_list[0]))
    elif len(add_list) != 0 :
        for i in range(int(add_list[0])):
            pw.append(add_list[1+i])
            

    print(f'#{tc}',end=' ')
    for i in range(10):
        print(pw[i],end=' ')
    print()