from pypinyin import lazy_pinyin
import pandas as pd
import pypinyin

import openpyxl


# 载入一个列表 返回一个全大写的列表
def upper_01(list1):
    list2 = []
    for i in list1:
        I = i.upper()
        list2.append(I)
    return list2


# 把大写字母和小写字母拼接成首字母大写的拼音列表
def pinjie():
    wanzheng = []
    for i in range(0, len(shouzimudaxie)):
        wanzheng.append(shouzimudaxie[i] + test_listsmall[i])
    return wanzheng


if __name__ == '__main__':
    # 读入EXCEL文件
    ex = pd.read_excel("test.xlsx")
    result = ""
    for i in range(ex.shape[0]):  # 遍历excel表格
        zh_word = (ex.iloc[i, 0])  # 读取第一列 首行默认不读取
        test_listbig = lazy_pinyin(zh_word, style=pypinyin.FIRST_LETTER)  # 读取每一个汉字的第一个首字母
        shouzimudaxie = upper_01(test_listbig)  # 利用upper_01函数 变为大写
        test_listsmall = lazy_pinyin(zh_word, style=pypinyin.FINALS)  # 读取每一个汉字除了首字母的其他拼音
        result = result + ''.join(pinjie()) + ' \n'  # 组合
    # 写文件
    with open('pinyinwenjian.txt', 'w') as f:
        f.write(result)
