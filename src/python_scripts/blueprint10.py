from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename, area,sh):
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
        qual = [sh1.cell_value(5,c) for c in range(1,4)]
        distr = [sh1.cell_value(8,c) for c in range(1,4)]
        cdistr = [sh1.cell_value(6,c) for c in range(1,4)]

        for i in range(0,3):
            sublist = [year, area, str(qual[i]), distr[i], cdistr[i]]
            list.append(sublist)

        #country stats
        area2='UK'
        qual = [sh1.cell_value(5,c) for c in range(1,4)]
        distr = [sh1.cell_value(8,c) for c in range(1,4)]
        cdistr = [sh1.cell_value(6,c) for c in range(1,4)]


        for i in range(0,3):
            sublist = [year, area2, str(qual[i]), distr[i], cdistr[i]]
            list.append(sublist)

def write3(filename, area,sh):
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
        qual = [sh1.cell_value(5,c) for c in range(1,4)]
        distr = [sh1.cell_value(8,c) for c in range(1,4)]
        cdistr = [sh1.cell_value(6,c) for c in range(1,4)]

        for i in range(0, 3):
            sublist = [year, area, str(qual[i]), distr[i], cdistr[i]]
            list.append(sublist)

def write2(filename, area,sh):
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
        qual = [sh1.cell_value(5,c) for c in range(1,4)]
        distr = [sh1.cell_value(8,c) for c in range(1,4)]
        cdistr = [sh1.cell_value(6,c) for c in range(1,4)]


        for i in range(0, 3):
            sublist = [year, area, str(qual[i]), distr[i], cdistr[i]]
            list.append(sublist)




j=10
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

with open('blueprint10.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


