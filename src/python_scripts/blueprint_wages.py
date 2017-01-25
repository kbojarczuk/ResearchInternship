from openpyxl import *
import csv
import xlrd
import re


list = []

def write(filename, area):
    for i in range(11,13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/'+filename)
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

        empty = "\\N"
        # wage stats area
        value = [sh1.cell_value(r, 1) for r in range(17, 18)]

        for i in range(0, 1):
            sublist = [str(year), area, value[i]]
            list.append(sublist)

        # wage stats country
        area2 = ['UK']
        value = [sh1.cell_value(r, 2) for r in range(17, 18)]

        for i in range(0, 1):
            sublist = [str(year), area2[0], value[i]]
            list.append(sublist)

def write2(filename, area):
    for i in range(11,13):
        path = 'creative_blueprint/region/'
        wb = xlrd.open_workbook(path + str(i) + '/'+filename)
        sh0 = wb.sheet_by_index(0)

        # year from the first sheet
        # [row][col]
        year = [sh0.cell_value(5, 3)]

        sh1 = wb.sheet_by_index(1)

        empty = "\\N"
        # wage stats area
        value = [sh1.cell_value(r, 1) for r in range(17, 18)]

        for i in range(0, 1):
            sublist = [str(year[0]), area, value[i]]
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




with open('blueprint_wages.csv', 'w', newline='') as f:
    c = csv.writer(f)
    for i in list:
        c.writerow(i)


