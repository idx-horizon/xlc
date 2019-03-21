from app.converters import DSFile as DS
#FN = 'testdata/TEST.xlsx'
if __name__ == '__main__':
    w = DS('testdata/TEST.xlsx')
    
    if w is not None: 
       w.analyse()
    else:
        print('** Error: Unable to instantiate object')  
  