from xlc.converters import DSFile as D

d = D('testdata/TEST.xlsx')

d.analyse()
d.convert(sheet=0)

d.convert(sheet=1)
d.convert(sheet='Sheet1')
d.convert(sheet='doesnotexist')
