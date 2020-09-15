from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba
import jieba.analyse

WC_MASJ_IMG = "wawa.jpg"
WC_FONT_PATH = 'ziti/FZLTXHJW.TTF'

STOP_WORDS_FILE_PATH = 'stop_words.txt'

with open('chineseword', 'r', encoding='UTF-8') as f:
    comment_txt = f.read()
jieba.analyse.set_stop_words(STOP_WORDS_FILE_PATH)
wordlist = jieba.cut(comment_txt, cut_all=True)
wl = " ".join(wordlist)

wc_mask = np.array(Image.open(WC_MASJ_IMG))
# 设置词云的一些配置，如：字体，背景色，词云形状，大小
wc = WordCloud(background_color="white", max_words=2000, mask=wc_mask, scale=4,
               max_font_size=50, random_state=42, font_path=WC_FONT_PATH)

wc.generate(wl)
# 在只设置mask的情况下，你将会的到一个拥有图片形状的词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.savefig("ciyun.jpg", dpi=100, format='jpg')
plt.show()
