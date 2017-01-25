from openpyxl import *
import csv
import xlrd
import re


#grants ---------------------------------------

wb = xlrd.open_workbook('local16.xlsx')
sh = wb.sheet_by_index(2)

#1314 add 10 to columns
# [row][col]
n = 88
list = []
type = sh.cell_value(6,n)
year = '2016/2017'
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

# [row][col]
type = sh.cell_value(6,n+1)
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n+1) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)


# [row][col]
type = sh.cell_value(6,n+2)
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n+2) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

# [row][col]
type = sh.cell_value(6,n+3)
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n+3) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

# [row][col]
type = sh.cell_value(7,n+4)
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n+4) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

# [row][col]
type = sh.cell_value(6,n+5)
ecode = [sh.cell_value(r,0) for r in range(7,450)]
budget = [sh.cell_value(r,n+5) for r in range(7,450)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

with open('local16.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


