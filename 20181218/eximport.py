import os


os.chdir(r'C:\Users\student\pjh\20181218\dummy')
# print(os.getcwd())

for filename in os.listdir('.'):
    # 1  replace 함수이용 새로운 파일 이름 생성
    new_filename = filename.replace('합격자','')
    # 2  os.rename 함수이용 파일이름 변경
    os.rename(filename,new_filename)