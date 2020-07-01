#彩色转换成黑白

#!/user/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image

img = Image.open("2 (2).png")   # 读取图片
img = img.convert("L")   # 转化为黑白图片
img.save("zbh2.png")   # 存储图片

