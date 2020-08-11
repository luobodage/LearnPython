import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from jqdatasdk import *

auth('18846936702','Zxc4525577')

q = query(valuation).filter(valuation.code=='000001.XSHE')
df = get_fundamentals(q,'2020-08-1')
print(df['market_cap'][0])
df = get_fundamentals(query(valuation,income).filter(valuation.code.in_(['000001.XSHE','600000.XSHG'])),date='2020-08-1')
print(df)


df = get_fundamentals(query(
    valuation.code,valuation.market_cap,valuation.pe_ratio,income.total_operating_revenue
).filter(
    valuation.market_cap > 1000,
    valuation.pe_ratio < 10,
    income.total_operating_revenue > 2e10
).order_by(
    valuation.market_cap.desc()
).limit(
    100
),date='2020-08-01')
print(df)

from sqlalchemy.sql.expression import or_
df = get_fundamentals(query(
    valuation.code
).filter(
    or_(
        valuation.market_cap > 1000,
        valuation.pe_ratio < 10
    )
))
print(df)

q = query(
    income.statDate,
    income.code,
    income.basic_eps,
    cash_flow.goods_sale_and_service_render_cash
).filter(
    income.code == '000001.XSHE'
)
year = get_fundamentals(q,statDate='2020')
print(year)


