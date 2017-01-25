from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename, area,sh):
    if sh==3:
        stats = 'Disabled workers'
    elif sh==4:
        stats = 'Ethnic diversity'
    elif sh==5:
        stats = 'Part time work'
    elif sh==6:
        stats = 'Gender'
    elif sh==7:
        stats = 'Self-employment'
    for i in range(11, 13):

        path = 'creative_blueprint/region/'
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

        sh1 = wb.sheet_by_index(sh)
        empty = "\\N"
        #subsector stats
        distribution = [sh1.cell_value(5,c) for c in range(1,3)]
        type = [sh1.cell_value(4,c) for c in range(1,3)]

        for i in range(0,2):
            sublist = [str(year), stats,type[i], area, distribution[i]*100]
            list.append(sublist)

        #country stats
        area2='UK'
        distribution = [sh1.cell_value(6, c) for c in range(1, 3)]
        type = [sh1.cell_value(4,c) for c in range(1,3)]

        for i in range(0,2):
            sublist = [str(year), stats,type[i], area2, distribution[i] * 100]
            list.append(sublist)

def write2(filename, area,sh):
    if sh == 3:
        stats = 'Disabled workers'
    elif sh == 4:
        stats = 'Ethnic diversity'
    elif sh == 5:
        stats = 'Part time work'
    elif sh == 6:
        stats = 'Gender'
    elif sh == 7:
        stats = 'Self-employment'
    for i in range(11, 13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        # year from the first sheet
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
        # subsector stats
        distribution = [sh1.cell_value(5, c) for c in range(1, 3)]
        type = [sh1.cell_value(4, c) for c in range(1, 3)]

        for i in range(0, 2):
            sublist = [str(year), stats,type[i], area, distribution[i] * 100]
            list.append(sublist)


for j in range (3,7):
    write('wales.xlsx','Wales',j)
    write2('england.xlsx','England',j)
    write2('scotland.xlsx','Scotland',j)
    write2('northern_ireland.xlsx','Northern Ireland',j)
    write2('east_england.xlsx','East of England',j)
    write2('east_midlands.xlsx','East Midlands',j)
    write2('london.xlsx','London',j)
    write2('north_west.xlsx','North West',j)
    write2('south_east.xlsx','South East',j)
    write2('south_west.xlsx','South West',j)
    write2('west_midlands.xlsx','West Midlands',j)
    write2('yorkshire_humberside.xlsx','Yorkshire and Humberside',j)

with open('blueprint3.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


