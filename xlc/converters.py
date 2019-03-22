import csv
import xlrd
import os

class DSFile(object):

  def __init__(self, 
  source_file, 
  dest_file=None, 
  sheet=None, 
  header=None, 
  options=None):
  
    if not os.path.exists(source_file):
      print('** File does not exist {}'.format(source_file))
      return None
      
    self.source_file = source_file
    self.dest_file = dest_file
    self.sheet = sheet
    self.header = header
    self.options = options
    
  def analyse(self,sheets=None):
    wb = xlrd.open_workbook(self.source_file)
    for sh in wb.sheets():
      print('Name: {} Rows: {} Cols: {}'.format(sh.name, sh.ncols, sh.nrows))
      
  def convert(self):
    print('Not yet implemented')
    
