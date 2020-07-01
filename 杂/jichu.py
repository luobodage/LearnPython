class person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我是{}呀 ".format(self.name) + "我现在{}公斤".format(self.weight)

    def run(self):
        print("{}跑了半个小时，之后".format(self.name))
        self.weight = self.weight - 0.5
        return self.weight

    def eat(self):
        print("{}吃了半个小时，之后".format(self.name))
        self.weight = self.weight + 1.0
        return self.weight


xm = person('小明', 75.0)
xm.run()
print(xm)

xmei = person('小美',45)
xmei.run()
xmei.eat()
print(xmei)
