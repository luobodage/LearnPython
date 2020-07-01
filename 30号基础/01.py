# 成绩查询系统


def daoru():

    with open('ini.txt', 'r', encoding='utf-8') as file:
        # 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        for line in file.readlines():
            line = line.strip()
            k = line.split(' ')[0]
            v = line.split(' ')[1]
            dict_temp[k] = v



def InputAndPrint():
    inputName = input("键盘输入：")
    if inputName in dict_temp:
        # print("成绩")
        print(dict_temp[inputName])
    else:
        print("NotFound")


def main():
    daoru()
    InputAndPrint()


if __name__ == '__main__':
    dict_temp = {}
    main()
