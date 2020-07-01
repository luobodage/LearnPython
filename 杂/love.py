def year():
    for i in range(1999, 2101, 1):
        print(i, end='年')
    return None


def mounth():
    for i in range(12):
        print(i + 1, end='月')
    return None


def day():
    for i in range(31):
        print(i + 1, end="日")
    return None


def hours():
    for i in range(24):
        print(i + 1, end='时')
    return None


def minute():
    for i in range(60):
        print(i + 1, end='分')
    return None


def second():
    for i in range(60):
        print(i + 1, end='秒')
    return None


if __name__ == '__main__':
    year()
    mounth()
    day()
    hours()
    minute()
    second()
