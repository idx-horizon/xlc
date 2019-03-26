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
    outfile = dest_file or self.source_file +'_sheet_' + str(sheet) + '.csv'
    
    wb = self.open()
    try:
      if isinstance(sheet, int):
        sh = wb.sheet_by_index(sheet)
      else:
        sh = wb.sheet_by_name(str(sheet))
    except Exception as e:
      print('Unable to set sheet {}, Exception: {}'.format(sheet,e))
      return None
            
    col_headers = []
    for h in range(sh.ncol): col_headers.append('Col{}'.format(h))
    
    with open(outfile,'w') as fh_out:
      dw = csv.DictWriter(fh_out, 
                          fieldnames=col_headers, 
                          lineterminator='\n',
                          quoting=csv.QUOTE_MINIMAL)
      dw.writeheader()
      
      for r in sh.get_rows()[header:]:
        output_row = {}
        for ix, c in enumerate(r):
          output_row['Col'+str(ix+1)] = c.value
        
        dw.writerow(output_row)
      
    print('Output to {}'.format(outfile))
    
