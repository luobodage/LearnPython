import jqdatasdk as jq

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib



jq.auth('username','password')

jqdata = jq.get_price("000001.XSHE",start_date="2020-08-01",end_date="2020-08-08")

df = pd.DataFrame(jqdata)

df1 = df.loc["2020-08-03":"2020-08-04","open"]

# print(df1)

x = np.linspace(0,5,10)
y = x ** 2
plt.figure()

plt.subplot(1,2,1)
plt.plot(x,y,'r--')

plt.subplot(1,2,2)
plt.plot(x,y,'g*-')
plt.show()


