import openpyxl

xl = openpyxl.Workbook()
ws = xl.active
ws['A1'].value = 'ABC'
xl.save('test1.xlsx')