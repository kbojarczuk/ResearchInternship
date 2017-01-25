from openpyxl import *
import csv
import xlrd
import re


#grants ---------------------------------------

wb = xlrd.open_workbook('local2012.xls')
sh = wb.sheet_by_index(2)


# [row][col]
list = []
ecode = [sh.cell_value(r,0) for r in range(9,453)]
ons = [sh.cell_value(r,1) for r in range(9,453)]
name = [sh.cell_value(r,2) for r in range(9,453)]
region = [sh.cell_value(r,3) for r in range(9,453)]
clas = [sh.cell_value(r,4) for r in range(9,453)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [ecode[i][1:5],ons[i].replace(',',''),name[i].replace(',',''),region[i].replace(',',''),clas[i].replace(',','')]
    list.append(sublist)


print(list.__sizeof__())

with open('local_list2.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


