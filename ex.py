from xlc.converters import DSFile as D

d = D('testdata/TEST.xlsx')

d.analyse()

for s in {0,1,'Sheet1','Sheet2','not_exist'}:
    d.convert(sheet=s, header=3,overwrite=False)
