def find_all(sub, s):
    index_list = []
    index = s.find(sub)
    while index != -1:
        index_list.append(index)
        index = s.find(sub, index + 1)

    if len(index_list) > 0:
        return index_list
    else:
        return -1


def tk():
    # 填空
    tk = []
    tk.append(s[:find_all("二、单项选择", s)[0]])
    for i in range(21):
        tk.append(s[find_all('《西方经济学》练习', s)[i + 1]:find_all("二、单项选择", s)[i + 1]])
    with open("填空.txt", "w", encoding="utf-8") as f:
        for j in tk:
            f.write(j)
        f.write("\n")


def dx():
    # 单选
    dx = []

    for i in range(21):
        dx.append("西方经济学" + str(i + 1) + "\n")
        dx.append(s[find_all('二、单项选择', s)[i]:find_all("三、", s)[i]])

    with open("选择.txt", "w", encoding="utf-8") as f:
        for j in dx:
            f.write(j)
        f.write("\n")


def duox():
    # 多选
    duox = []

    for i in range(21):
        duox.append("西方经济学" + str(i + 1) + "\n")
        duox.append(s[find_all('三、多项选择', s)[i]:find_all("四、", s)[i]])

    with open("多选.txt", "w", encoding="utf-8") as f:
        for j in duox:
            f.write(j)
        f.write("\n")


def pd():
    # 判断
    pd = []

    for i in range(21):
        pd.append("西方经济学" + str(i + 1) + "\n")
        pd.append(s[find_all('四、判断', s)[i]:find_all("五、", s)[i]])

    with open("判断.txt", "w", encoding="utf-8") as f:
        for j in pd:
            f.write(j)
        f.write("\n")


def mcjs():
    # 名词解释
    mcjs = []

    for i in range(len(find_all("六、", s))):
        mcjs.append("西方经济学" + str(i + 1) + "\n")
        mcjs.append(s[find_all('五、', s)[i]:find_all("六、", s)[i]])

    with open("名词解释.txt", "w", encoding="utf-8") as f:
        for j in mcjs:
            f.write(j)
        f.write("\n")


def jd():
    # 简答
    jd = []

    for i in range(len(find_all("七、", s))):
        jd.append("西方经济学" + str(i + 1) + "\n")
        jd.append(s[find_all('六、', s)[i]:find_all("七、", s)[i]])

    with open("简答.txt", "w", encoding="utf-8") as f:
        for j in jd:
            f.write(j)
        f.write("\n")


def js():
    # 计算题
    jst = []

    for i in range(len(find_all("七、", s)) - 1):
        jst.append("西方经济学" + str(i + 1) + "\n")
        jst.append(s[find_all('七、', s)[i]:find_all("《西方经济学", s)[i + 1]])

    with open("计算题.txt", "w", encoding="utf-8") as f:
        for j in jst:
            f.write(j)
        f.write("\n")


if __name__ == '__main__':
    with open("整理.txt", "r", encoding="utf-8") as f:
        s = f.read()
    tk()
    dx()
    duox()
    pd()
    mcjs()
    jd()
    js()
