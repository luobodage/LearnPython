import xlwt
new_workbookl = xlwt.Workbook()
worksheet = new_workbookl.add_sheet('sheet1')
worksheet.write(0,0,'test')
new_workbookl.save('test.xls')