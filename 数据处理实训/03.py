import xlrd
import xlwings as xw
workbook=xlrd.open_workbook('example.xls')

sheet=workbook.sheets()[0]
#第B列
print(sheet.col_values(1))

new = []
for i in sheet.col_values(0):
    print(i)
    i = str(i)
    new.append([i])
    print(type(i))

print(new)




# sht = xw.Book().sheets('sheet1')  # 新增一个表格
# sht.range('A1').options(transpose=True).value = new