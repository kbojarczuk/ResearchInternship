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
    sth = sh.col_values(0,26,29)
    prg = sh.col_values(2+i*4,26,29)
    rg = sh.col_values(3+i*4,26,29)
    resp = sh.col_values(4+i*4,26,29)



    empty = "\\N"
    lempty ="\\N"
    for i in range(0,3):
        prog = re.compile("20\d\d/20\d\d")
        search = re.search(prog, str(year))
        if search:
            reg_year = search.group()
        else:
            reg_year = year[0:5]+"20"+year[5:7]
        sublist=[type,reg_year,str(sth[i]).replace(',',''),str(prg[i]).replace(',',''),
                str(rg[i]).replace(',',''),str(resp[i]).replace(',','')]
        list.append(sublist)

for i in range(0,3):
    year = data[3][30+i*14]
    sth = sh.col_values(0,26,29)
    prg = sh.col_values(30+i*14,26,29)
    rg = sh.col_values(32+i*14,26,29)
    resp = sh.col_values(42+i*14,26,29)



    empty = "\\N"
    lempty ="\\N"
    for i in range(0,3):
        prog = re.compile("20\d\d/20\d\d")
        search = re.search(prog, str(year))
        if search:
            reg_year = search.group()
        else:
            reg_year = year[0:5]+"20"+year[5:7]
        sublist=[type,reg_year,str(sth[i]).replace(',',''),str(prg[i]).replace(',',''),
                str(rg[i]).replace(',',''),str(resp[i]).replace(',','')]
        list.append(sublist)



print(list.__sizeof__())

with open('tp_arts_tenure_m.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


