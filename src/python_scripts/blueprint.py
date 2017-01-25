from openpyxl import *
import csv
import xlrd
import re




list = []
def write(filename, area):
    for i in range(11, 13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        #year from the first sheet
        # [row][col]
        year = sh0.cell_value(5, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)

        sh1 = wb.sheet_by_index(1)

        empty = "\\N"
        #subsector stats
        sector = [sh1.cell_value(r,0) for r in range(7,14)]
        distribution = [sh1.cell_value(r,1) for r in range(7,14)]

        for i in range(0,7):
            sublist = [str(year), area, sector[i], distribution[i]*100]
            list.append(sublist)

        #country stats
        area2 ='UK'
        sector = [sh1.cell_value(r,0) for r in range(7,14)]
        distribution = [sh1.cell_value(r,2) for r in range(7,14)]


        for i in range(0,7):
            sublist = [str(year), area2, sector[i], distribution[i]*100]
            list.append(sublist)

def write2(filename, area):
    for i in range(11, 13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/' + filename)
        sh0 = wb.sheet_by_index(0)

        #year from the first sheet
        # [row][col]
        year = sh0.cell_value(5, 3)
        prog = re.compile("2010/\d\d")
        search = re.search(prog, str(year))
        if search:
            year = year[0:5] + "20" + year[5:7]
        else:
            year = int(year)

        sh1 = wb.sheet_by_index(1)

        empty = "\\N"
        #subsector stats
        sector = [sh1.cell_value(r,0) for r in range(7,14)]
        distribution = [sh1.cell_value(r,1) for r in range(7,14)]

        for i in range(0,7):
            sublist = [year, area, sector[i], distribution[i]*100]
            list.append(sublist)



write('wales.xlsx','Wales')
write2('england.xlsx','England')
write2('scotland.xlsx','Scotland')
write2('northern_ireland.xlsx','Northern Ireland')
write2('east_england.xlsx','East of England')
write2('east_midlands.xlsx','East Midlands')
write2('london.xlsx','London')
write2('north_west.xlsx','North West')
write2('south_east.xlsx','South East')
write2('south_west.xlsx','South West')
write2('west_midlands.xlsx','West Midlands')
write2('yorkshire_humberside.xlsx','Yorkshire and Humberside')

with open('blueprint1.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


