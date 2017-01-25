from openpyxl import *
import csv
import xlrd
import re


#grants ---------------------------------------

wb = xlrd.open_workbook('local2014.xls')
sh = wb.sheet_by_index(2)

#1314 add 10 to columns
# [row][col]
list = []
type = 'employees'
year = '2014/2015'
ecode = [sh.cell_value(r,0) for r in range(9,453)]
budget = [sh.cell_value(r,55) for r in range(9,453)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)

# [row][col]
type = 'running expenses'
ecode = [sh.cell_value(r,0) for r in range(9,453)]
budget = [sh.cell_value(r,56) for r in range(9,453)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)


# [row][col]
type = 'sales fees and charges'
ecode = [sh.cell_value(r,0) for r in range(9,453)]
budget = [sh.cell_value(r,58) for r in range(9,453)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)
'''
# [row][col]
type = 'capital items'
ecode = [sh.cell_value(r, 0) for r in range(9, 453)]
budget = [sh.cell_value(r, 72) for r in range(9, 453)]


for i in range(0, 443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)


'''

# [row][col]
type = 'other income'
ecode = [sh.cell_value(r,0) for r in range(9,453)]
budget = [sh.cell_value(r,59) for r in range(9,453)]


empty = "\\N"
lempty ="\\N"
for i in range(0,443):
    sublist = [type, year, budget[i], ecode[i][1:5]]
    list.append(sublist)


with open('local_budget1415.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


