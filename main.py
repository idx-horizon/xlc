from app.converters import DS 

if __name__ == '__main__':
    w = DS(r'testdata\\TEST.xlsx')
    
    w.analyse() if w is not None else print('** Error: Unable to instantiate object')  
