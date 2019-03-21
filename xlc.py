import xlrd
import csv
from app.converters import DS 

if __name__ == '__main__':
    w = DS(r'testdata\\TEST.xlsx')
    if w:
        w.analyse()
    else:
        print('** Unable to instantiate object')  
