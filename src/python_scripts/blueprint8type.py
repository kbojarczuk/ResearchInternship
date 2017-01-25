from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename,sh):
    if sh==3:
        stats = 'Disabled workers'
    elif sh==4:
        stats = 'Ethnic diversity'
    elif sh==5:
        stats = 'Part time work'path = 'creative_blueprint/type/'
        if(filename=='literature.xlsx'):
            wb =xlrd.open_workbook(path + '11' + '/' + filename)
        else:
            wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)
    elif sh==6:
        stats = 'Gender'
    elif sh==7:
        stats = 'Self-employment'
    for i in range(11, 13):


        #year from the first sheet
        # [row][col]
        year = sh0.cell_value(7, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)
        sh1 = wb.sheet_by_index(sh)
        empty = "\\N"
        #subsector stats
        distribution = [sh1.cell_value(5,c) for c in range(1,6)]
        type = sh1.cell_value(5,0)
        stats = [sh1.cell_value(4,c) for c in range(1,6)]

        for i in range(0, 5):
            sublist = [str(year), type, stats[i], distribution[i] * 100]
            list.append(sublist)


j=8
write('craft.xlsx',j)
write('design.xlsx',j)
write('heritage.xlsx',j)
write('literature.xlsx',j)
write('music.xlsx',j)
write('performing_arts.xlsx',j)
write('visual_arts.xlsx',j)

with open('blueprint8type.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


