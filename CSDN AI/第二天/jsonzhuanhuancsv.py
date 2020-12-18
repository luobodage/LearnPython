import pandas as pd
import json
from pandas.io.json import json_normalize

data = '世界疫情数据.json'
with open(data, 'r') as f:
    strF = f.read()
    if len(strF) > 0:

        datas = json.loads(strF)
    else:
        datas = {}
data_csv =json_normalize(datas)
data_csv.to_csv('Result.csv') # 转换成csv文件