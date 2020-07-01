

def count():
	i = 5
	while i > 0:
		yield i # 将后面的变量返回到集合里，集合不能被索引。
		i -= 1

for i in count():
	print(i)

# def infintit_sevens():
# 	while True:
# 		yield 7

# for i in infintit_sevens():
# 	print(i)


# def make_word():
# 	word = ""
# 	for n in "spam":
# 		word += n
# 		yield word
# print(list(make_word()))

def decor(func):
	def wrap():
		print("=================")
		func()
		print("=================")
	return wrap

def prin_text():
	print("Hello World!!")

decorated = decor(prin_text)
decorated()