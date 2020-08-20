import numpy as np
import pandas as pd





# 3sigma原则
# 根据正太分布得出 99.73%的数据都在[u-3sigma ,u+3sigma ]之间，
# 那么我们人为超出这个区间的数据为异常值
# 剔除异常值----保留数据在[u-3sigma ,u+3sigma ]之间
def three_sigma(data):
    # sigma 异常值删除
    # :param data: 传入数据
    # :return: 剔除之后的数据，或者剔除异常值之后的行索引名称

    bool_id_1 = (data.mean() - 3 * data.std()) <= data
    bool_id_2 = (data.mean() + 3 * data.std()) >= data

    bool_num = bool_id_1 & bool_id_2

    return bool_num


# # 以 detail 为例 展示以amounts 进行异常值剔除，查看detail结果
# 加载数据
data = [
    [25698744, 5145, 444],
	[ np.nan,  np.nan, 445],
    [25698746, 5156,  446],
    [25698747,  np.nan, 447],
    [ np.nan, 5145, 448],
    [25698749,  np.nan, 9744000000],
    [25698743, 5454, 490],
    [25698743, 5454, 451],
    [25698743, 5454, 454],
    [25698743, 5454, 455],
    [25698743, 5454, 456],
    [25698743, 5454, 453],
    [25698743, 5454, 453],
    [25698743, 5454, 457],
    [25698743, 5454, 457],
    [25698743, 5454, 458]
]

data = pd.DataFrame(data, columns = ['商品id', '类别id', '门店编号'])
print(data.shape)


# 调用函数 进行detail中amount的异常值剔除
bool_num = three_sigma(data.loc[:, '门店编号'])

# 获取正常的detail
detail = data.loc[bool_num, :]
print(detail.shape)




# 箱线图分析

# qu %75的数
# ql %25的数
# 1.5 可以稍微调整，，一般使用1.5
# iqr = qu - ql
# 上限：qu + 1.5*iqr
# 下限 ：ql - 1.5*iqr

def box_analysis(data):
    '''
    进行箱线图分析，剔除异常值
    :param data: series
    :return: bool数组
    '''

    qu = data.quantile(0.75)
    ql = data.quantile(0.25)

    iqr = qu - ql

    # 上限
    up = qu + 1.5 * iqr
    # 下限
    low = ql - 1.5 * iqr

    # 进行比较运算
    bool_id_1 = data <= up
    bool_id_2 = data >= low

    bool_num = bool_id_1 & bool_id_2

    return bool_num

bool_num = box_analysis(data.loc[:, '门店编号'])
detail = detail.loc[bool_num, :]
print(detail.shape)