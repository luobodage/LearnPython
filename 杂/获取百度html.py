def duichen(x):
    a = x % 10
    b = x // 100
    if a == b:
        c = True
    else:
        c = False
    return c


su = 0
for n in range(100, 1000):
    if duichen(n):
        su = n % 10 + n // 100 + (n / 10) % 10
print(su)
