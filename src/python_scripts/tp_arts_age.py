from openpyxl import *
import csv
import xlrd
import re

wb = xlrd.open_workbook('museums.xls')
type = 'museums'
sh = wb.sheet_by_index(2)

data = [[sh.cell_value(r,c) for c in range (sh.ncols)]
for r in range (sh.nrows)]



list = []
for i in range(0,7):
    year = data[3][2+i*4]
    sth = sh.col_values(0,7,12)
    prg = sh.col_values(2+i*4,7,12)
    rg = sh.col_values(3+i*4,7,12)
    resp = sh.col_values(4+i*4,7,12)



    empty = "\\N"
    lempty ="\\N"
    for i in range(0,5):
        prog = re.compile("20\d\d/20\d\d")
        search = re.search(prog, str(year))
        if search:
            reg_year = search.group()
        else:
            reg_year = year[0:5]+"20"+year[5:7]
        if len(sth[i])<4:
            lala = "100"
        else:
            lala = str(sth[i][3:5])

        sublist=[type,reg_year,str(sth[i][0:2]).replace(',',''),lala.replace(',',''),str(prg[i]).replace(',',''),
                str(rg[i]).replace(',',''),str(resp[i]).replace(',','')]
        list.append(sublist)

for i in range(0,3):
    year = data[3][30+i*14]
    sth = sh.col_values(0,7,12)
    prg = sh.col_values(30+i*14,7,12)
    rg = sh.col_values(32+i*14,7,12)
    resp = sh.col_values(42+i*14,7,12)



    empty = "\\N"
    lempty ="\\N"
    for i in range(0,5):
        prog = re.compile("20\d\d/20\d\d")
        search = re.search(prog, str(year))
        if search:
            reg_year = search.group()
        else:
            reg_year = year[0:5]+"20"+year[5:7]

        if len(sth[i])<4:
            lala = "100"
        else:
            lala = str(sth[i][3:5])

        sublist=[type,reg_year,str(sth[i][0:2]).replace(',',''),lala.replace(',',''),str(prg[i]).replace(',',''),
                str(rg[i]).replace(',',''),str(resp[i]).replace(',','')]
        list.append(sublist)



print(list.__sizeof__())

with open('tp_arts_age_m.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


