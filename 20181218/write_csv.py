lunch = {
    '용성돌솥':'054-474-7119',
    '별난짬뽕':'054-473-3040',
    '매콤돈가스':'054-472-2030'
}

import csv




with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csv_writer = csv.writer(f)

    for item in lunch.items(): # 리스트의 형태 (key,value)
        csv_writer.writerow(item)
        # f.write(f'{item[0]},{item[1]}\n')
