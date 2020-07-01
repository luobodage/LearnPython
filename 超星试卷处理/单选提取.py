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


if __name__ == '__main__':
    with open("整理.txt", "r", encoding="utf-8") as f:
        s = f.read()
    a = []

    for i in range(21):
        a.append("西方经济学"+str(i+1)+"\n")
        a.append(s[find_all('二、单项选择', s)[i]:find_all("三、", s)[i]])

    with open("选择.txt", "w", encoding="utf-8") as f:
        for j in a:
            f.write(j)
        f.write("\n")
