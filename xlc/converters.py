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
      
  def validate(self):
    pass
        
  def convert(self, dest_file=None, sheet=0, header=0, col_headers=None,overwrite=True):
    outfile = dest_file or self.source_file +'_sheet_' + str(sheet) + '.csv'
    
    if os.path.exists(outfile):
      if overwrite == True:
        print('WARNING: {} will be overwritten'.format(outfile)
      else
        print('ERROR: {} already exists'.format(outfile)\
        return None
        
      
    wb = self.open()
    try:
      sh = wb.sheet_by_index(sheet) if isinstance(sheet, int) else wb.sheet_by_name(str(sheet))
    except Exception as e:
      print('** ERROR: Handling sheet {}, Exception: {}'.format(sheet,e))
      return None
            
    col_headers = []
    for h in range(sh.ncols): 
      col_headers.append('Col{}'.format(h))
    
    with open(outfile,'w') as fh_out:
      dw = csv.DictWriter(fh_out, 
                          fieldnames=col_headers, 
                          lineterminator='\n',
                          quoting=csv.QUOTE_MINIMAL)
      dw.writeheader()
      
      for row_num, row_data in enumerate(sh.get_rows()):
        if row_num <= header:
          pass
          
        output_row = {} 
        for ix, c in enumerate(row_data):
            output_row['Col{}'.format(ix)] = c.value

        dw.writerow(output_row)
      
    print('Output to {}'.format(outfile))
    
