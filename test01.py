a = 1
b = 1

while True:
    c = 100 - (a + b)
    if a * 5 + b * 3 + c * 1 == 100 and a + b + c == 100:
        print(a, b, c)
    if a >= (100 - 3 - 1) / 5:
        break
    if b >= (100 - 5 - 1) / 3:
        a += 1
        b = 1
    b += 1
