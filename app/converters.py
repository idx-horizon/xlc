import csv
import xlrd

class DS():

  def __init__(self, source_file, dest_file=None, sheet=None, header=None, options=None):
    self.source_file = source_file
    self.dest_file = dest_file
    
  def analyse(self):
    wb = xlrd.open_workbook(self.source_file)
    for sh in wb.sheets():
      print(Sheet: {} Rows: {} Cols: {}'.format(sh.name,sh.ncols, sh.nrows)
