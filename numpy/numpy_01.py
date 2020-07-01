import numpy as np

from PIL import Image

a = np.array(Image.open("11.png").convert('L'))

b = (100/255)*a + 150 

im = Image.fromarray(b.astype('uint8'))

im.save("4.png")