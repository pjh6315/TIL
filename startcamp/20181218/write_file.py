# f = open('ssafy.txt','w')  # w: write , r: read , a: append
# f.write('This is SSAFY!')
# f.close()


# \t : tab
# \\ : 백슬래시 '\' 입력하고싶을때
# \' \" : 마찬가지


with open('ssafy.txt','w',encoding='utf8') as f:
    f.writelines(['1\n','2\n','3\n'])
    
    """
    for i in range(10):
        f.write(f'This is \"SSAFY\"!!!!!! {i}\n')
    """