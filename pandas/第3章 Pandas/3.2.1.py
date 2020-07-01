# -*- coding: utf-8 -*-
import pandas as pd       #导入Pandas库
import numpy as np       #导入Numpy库



s = pd.Series([1,np.nan,1,2,2,3,4,5,6,'wyd'])
s.to_excel('wyd.xlsx')


