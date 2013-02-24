# parse and import data from Diasend.com

# TODO
# build objects for the other data readings from diasend
# start building charts using matplotlib
# parse dexcom data
# data design what data for charts, time periods

import xlrd
from Glucose import *

DATE_COLUMN = 0
MGDL_COLUMN = 1

def import_glucose(file_name):

    readings = []

    # open the workbook
    wb = xlrd.open_workbook(file_name)

    # get the worksheet with the glucose readings
    ws = wb.sheet_by_name('Name and glucose')

    # the first 5 lines are general information, discard
    # parse in the remeaning data
    for row in range(5, ws.nrows):
        date = ws.cell_value(row,DATE_COLUMN)
        mgdl = ws.cell_value(row,MGDL_COLUMN)
        #print date 
        #print mgdl
        #print "{0} - {1}".format(date, mgdl) 
        #print "-----"
        readings.append(Glucose(date, mgdl))

    for i in readings:
        print i.date
        print i.mgdl

if __name__ == '__main__':

    filename = 'files/import.xls'

    import_glucose(filename)
