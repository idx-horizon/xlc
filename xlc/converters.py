import csv
import xlrd
import os

class DSFile(object):

  def __init__(self, 
               source_file, 
               options=None):
  
    if not os.path.exists(source_file):
      print('** File does not exist {}'.format(source_file))
      return None
      
    self.source_file = source_file
    self.basename = os.path.basename(source_file)
    self.options = options
    
  def open(self):
    return xlrd.open_workbook(self.source_file)
    
  def analyse(self,sheets=None):
    wb = self.open()
    print('Source: {}, #sheets: {}'.format(self.basename, wb.nsheets))
     
    for sh in wb.sheets():
      print('Name: {} Rows: {} Cols: {}'.format(sh.name, sh.ncols, sh.nrows))
      
  def convert(self, dest_file=None, sheet=0, header=0):
    out_file = dest_file or self.source_file +'_sheet_' + str(sheet) + '.csv'
    
    wb = self.open()
    sh = wb.sheet_by_index(sheet)
    col_headers = ['ColA', 'ColB', 'ColC']
    
    with open(out_file,'w') as fh_out:
      dw = csv.DictWriter(fh_out, fieldnames=col_headers, lineterminator='\n')
      dw.writeheader()
      
      for r in sh.get_rows():
        output_row = []  
        for c in r:
          output_row.append c.value
        
        dw.writerow(output_row)
      
    print('Not yet implemented')
    
