# 全国城市地图示例
from pyecharts import Geo

data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("哈尔滨", 14),("齐齐哈尔", 16),
    ("盐城", 15),("双鸭山",8),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]

geo = Geo(
    "全国部分城市空气质量",
    title_color="#fff",
    title_pos="center",
    width=800,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo

# 导出绘图html文件，可直接用浏览器打开
geo.render('全国空气质量地图分布.html')
geo