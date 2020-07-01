class HoseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[{}]占地{}平米".format(self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        return ("房子的户型为{},面积为{},剩余面积为{},家具都有{}"
                .format(self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加{}".format(item))

        if item.area > self.free_area:
            print("{}面积太大了 装不下来啦".format(item.name))
            return

        self.item_list.append(item.name)

        self.free_area -= item.area


if __name__ == '__main__':
    bed = HoseItem("席梦思", 4)

    chest = HoseItem("衣柜", 2)

    table = HoseItem("餐桌", 1.5)

    print(bed)
    print(chest)
    print(table)

    my_home = House('两室一厅', 100)
    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)

    print(my_home)
