import time
import requests
import json
import os
import random
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from wordcloud import WordCloud

WC_MASJ_IMG = "wawa.jpg"
comment_file_path = 'c:/Users/萝卜ovo/Desktop/Python/ImportGitHub/跟着猪哥复习爬虫/id.txt'
WC_FONT_PATH = 'ziti/FZLTXHJW.TTF'

def spider_comment(page = 0):
    # 爬取京东评论
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1070129528' \
          '&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    try:
        r = requests.get(url)
        r.raise_for_status()
        # print('京东评论数据：'+ r.text[:500])
    except:
        print('爬取失败')

    r_json_str = r.text[20:-2]
    # print("京东评论：" + r_json_str[:500])
    r_json_obj = json.loads(r_json_str)
    r_json_comments = r_json_obj['comments']
    # print("京东评论数据：")
    # for r_json_comments in r_json_comments:
    #     print(r_json_comments['content'])

    for r_json_comments in r_json_comments:
        with open(comment_file_path,'a+') as file:
            file.write(r_json_comments['content'] + '\n')
        print(r_json_comments['content'])

def batch_spider_comment():
    """
    批量爬取评价
    :return:
    """
    # 写入数据前先清空之前的数据
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for i in range(100):
        spider_comment(i)
        time.sleep(random.random() * 5)

def cut_word():
    """
    对数据分词
    :return:分词后的数据
    """
    with open(comment_file_path) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt,cut_all=True)
        wl = " ".join(wordlist)
        print(wl)
        return wl
def create_word_cloud():
    """
    生成词云
    :return:
    """
    #设置词云形状图片
    wc_mask = np.array(Image.open(WC_MASJ_IMG))
    #设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color = "white",max_words=2000,mask=wc_mask,scale=4,
                        max_font_size=50,random_state=42,font_path=WC_FONT_PATH)
    #生成词云
    wc.generate(cut_word())

    #在只设置mask的情况下，你将会的到一个拥有图片形状的词云
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.figure()

    plt.savefig("ciyun.jpg" ,dpi=100, format='jpg')
    plt.show()


if __name__ == '__main__':
    # batch_spider_comment()
    # cut_word()
    create_word_cloud()