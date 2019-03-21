import xlrd
import csv
from app.converters import DS 

if __name__ == '__main__':
    w = DS('testdata\TEST.xlsx')
    w.analyse()
      
