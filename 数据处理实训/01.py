import xlrd
import xlwings as xw
workbook=xlrd.open_workbook('1.xlsx')

sheet=workbook.sheets()[0]
#第B列
print(sheet.col_values(1))

new = []
for i in sheet.col_values(1):
    print(i)
    i = str(i)
    new.append([i])
    print(type(i))

print(new)

sht = xw.Book().sheets('sheet1')  # 新增一个表格
sht.range('A1').value = new




# sht = xw.Book().sheets('sheet1')  # 新增一个表格
# sht.range('A1').options(transpose=True).value = new