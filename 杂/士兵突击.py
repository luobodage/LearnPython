class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[{}]弹尽粮绝了...".format(self.model))
            return

        self.bullet_count -= 1
        print("【{}】突突突...还剩【{}】".format(self.model, self.bullet_count))


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print("[{}]还没有枪~".format(self.name))
            return
        print("{}冲啊!!".format(self.name))

        self.gun.add_bullet(50)

        self.gun.shoot()

ak47 = Gun("AK47")

xsd = Soldier("许三多")

xsd.gun = ak47

xsd.fire()

