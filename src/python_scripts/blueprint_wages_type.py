from openpyxl import *
import csv
import xlrd
import re


list = []

def write(filename, sh):
    for i in range(11,13):
        path = 'creative_blueprint/type/'
        if (filename == 'literature.xlsx'):
            wb = xlrd.open_workbook(path + '11' + '/' + filename)
        else:
            wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        # year from the first sheet
        # [row][col]
        year = sh0.cell_value(5, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)


        sh1 = wb.sheet_by_index(1)
        print(sh1.ncols)

        empty = "\\N"
        # wage stats area
        value = [sh1.cell_value(r, 1) for r in range(sh1.nrows-1, sh1.nrows)]
        ind = sh1.cell_value(sh1.nrows-2, 1)

        for i in range(0, 1):
            sublist = [str(year), ind, value[i]]
            list.append(sublist)

j=8
write('craft.xlsx',j)
write('design.xlsx',j)
write('heritage.xlsx',j)
write('literature.xlsx',j)
write('music.xlsx',j)
write('performing_arts.xlsx',j)
write('visual_arts.xlsx',j)



with open('blueprint_wages_type.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


