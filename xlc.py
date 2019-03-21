from app.converters import DS 

if __name__ == '__main__':
    w = DS('testdata/TEST.xlsx')
    if w is None:
        w.analyse()
    else:
        print('** Error: Unable to instantiate object')  
