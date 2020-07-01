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
    a.append(s[:find_all("二、单项选择", s)[0]])
    for i in range(21):
        a.append(s[find_all('《西方经济学》练习', s)[i + 1]:find_all("二、单项选择", s)[i + 1]])
    with open("填空.txt", "w", encoding="utf-8") as f:
        for j in a:
            f.write(j)
        f.write("\n")
