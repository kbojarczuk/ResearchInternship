from openpyxl import *
import csv
import xlrd
import re


list = []
def write(filename, area3,sh):
    for i in range(11, 13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        #year from the first sheet
        # [row][col]
        year = sh0.cell_value(13, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)

        sh1 = wb.sheet_by_index(9)
        empty = "\\N"
        print(str(sh1.nrows) + "dsd " + str(sh1.ncols))
        #subsector stats
        area = [sh1.cell_value(r,0) for r in range(5,14)]
        qual = [sh1.cell_value(r,1) for r in range(5,14)]

        for i in range(0,9):
            sublist = [str(year), area[i], str(qual[i])]
            list.append(sublist)
        list.append([year, sh1.cell_value(15, 0), sh1.cell_value(15, 1)])





j=9
write('east_england.xlsx','East of England',j)


with open('blueprint9.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


