from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename,sh,n):
    for i in range(11, 13):
        path = 'creative_blueprint/type/'
        if(filename=='literature.xlsx'):
            wb =xlrd.open_workbook(path + '11' + '/' + filename)
        else:
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
        sh1 = wb.sheet_by_index(sh)
        sh2 = wb.sheet_by_index(9)
        empty = "\\N"
        #subsector stats
        type = sh1.cell_value(5,0)
        GVA = [sh2.cell_value(r,1) for r in range(5,5+n)]
        stats = [sh2.cell_value(r,0) for r in range(5,5+n)]

        for i in range(0, n):
            sublist = [str(year), type, stats[i], GVA[i]]
            list.append(sublist)


j=8
write('craft.xlsx',j,10)
write('design.xlsx',j,3)
write('heritage.xlsx',j,4)
write('literature.xlsx',j,2)
write('music.xlsx',j,7)
write('performing_arts.xlsx',j,7)
write('visual_arts.xlsx',j,3)

with open('blueprint9type.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


