# -*- coding: utf-8 -*-
import pandas as pd
path='一、车次上车人数统计表.xlsx';
data=pd.read_excel(path);
print(data)
data=pd.read_excel(path,'Sheet2')  #读取sheet里面的数据
print(data)
dta=pd.read_excel('dta.xlsx')  #无表头
print(dta)
