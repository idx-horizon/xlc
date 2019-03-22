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
    self.basename = os.path.basename(source_file)
    self.dest_file = dest_file
    self.sheet = sheet
    self.header = header
    self.options = options
    
  def analyse(self,sheets=None):
    wb = xlrd.open_workbook(self.source_file)
    print('Source: {}, #sheets'.format(self.basename, sh.nsheets), 
    for sh in wb.sheets():
      print('Name: {} Rows: {} Cols: {}'.format(sh.name, sh.ncols, sh.nrows))
      
  def convert(self):
    with open(dest_file,'w') as fh_out:
      dw = csv.DictWriter(fh_out, fieldnames=['A','B'], lineterminator='\n')
      dw.writeheader()
      dw.writerow({'A': 1, 'B': 'Not yet implemented'})
      
    print('Not yet implemented')
    
