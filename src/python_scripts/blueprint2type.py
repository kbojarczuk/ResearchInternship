from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename):
    for i in range(11, 13):
        path = 'creative_blueprint/type/'
        if(filename=='literature.xlsx'):
            i=12
            wb =xlrd.open_workbook(path + '11' + '/' + filename)
        else:
            wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        #year from the first sheet
        # [row][col]
        year = sh0.cell_value(7, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)
        sh1 = wb.sheet_by_index(2)
        empty = "\\N"
        #subsector stats
        age = [sh1.cell_value(4, c) for c in range(1, 13)]
        distr = [sh1.cell_value(5,c) for c in range(1,13)]
        type = sh1.cell_value(5, 0)

        for i in range(0,12):
            if len(age[i]) < 4:
                aget = "100"
            else:
                aget = str(age[i][3:5])
            sublist = [str(year), type, age[i][0:2],aget, distr[i]*100]
            list.append(sublist)



write('craft.xlsx')
write('design.xlsx')
write('heritage.xlsx')
write('literature.xlsx')
write('music.xlsx')
write('performing_arts.xlsx')
write('visual_arts.xlsx')

with open('blueprint2type.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


