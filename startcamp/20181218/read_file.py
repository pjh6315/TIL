with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()


    lines.reverse()

    # reve= 

with open('ssafy_reverse.txt','w',encoding='utf8') as f:

    f.writelines(lines)
