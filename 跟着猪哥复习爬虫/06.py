import re
import os
import json
import time
import random

import requests
import jieba.analyse
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pyecharts.charts import WordCloud

s = requests.Session()
TOPIC_FILE_PATH = '单身话题.txt'
STOP_WORDS_FILE_PATH = 'stop_words.txt'
def login_sina():
    """
    登录新浪
    :return:
    """
    # 登录url
    login_url = 'https://passport.weibo.cn/sso/login'
    # 请求头
    headers = {'user-agent': 'Mozilla/5.0',
               'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'}
    # 传递用户名和密码
    data = {'username': '18846936702',
            'password': 'zxc4525577',
            'savestate': 1,
            'entry': 'mweibo',
            'mainpageflag': 1}
    try:
        r = s.post(login_url, headers=headers, data=data)
        r.raise_for_status()
    except:
        print('登录请求失败')
        return 0
    # 打印请求结果
    print(r.json())
    return 1

def spider_topic(page=1):
    """
    爬取新浪话题
    :param page:分页参数
    :return:
    """

    topic_url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%2390%E5%90%8E%E5%8D%95%E8%BA%AB%E5%8E%9F%E5%9B%A0TOP3%23%26t%3D0&isnewpage=1&extparam=pos%3D41%26c_type%3D31%26realpos%3D40%26flag%3D0%26filter_type%3Drealtimehot%26cate%3D0%26display_time%3D1565179797&luicode=10000011&lfid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&page_type=searchall'

    kv = {'user-agent': 'Mozilla/5.0',
          'Referer': 'https://m.weibo.cn/p/1008087a8941058aaf4df5147042ce104568da/super_index?jumpfrom=weibocom'}

    try:
        r = s.get(url=topic_url, headers=kv)
        r.raise_for_status()
    except:
        print("爬取失败")
        return
    #解析shuju
    r_json = json.loads(r.text)
    cards = r_json['data']['cards']
    # mblog = r_json['data']['cards'][0]['mblog']
    # print(mblog['text'])
    text_list = []
    for i in range(len(cards)):
        mblog = cards[i]['mblog']
        text = re.compile(r'<[^>]+>', re.S).sub(' ', mblog['text'])
        strinfo = re.compile(r'#.*?#')
        text = strinfo.sub('', text).strip()
        text_list.append(text)
        print(text)
        # 3、一次写入文件
    with open(TOPIC_FILE_PATH, 'a+', encoding='utf-8') as file:
        file.writelines('\n'.join(text_list))
    return 1

    # for card in mblog:
    #
    #     text = mblog['text']
    #     print(text)
def patch_spider_topic():
    # 爬取前先登录，登录失败则不爬取
    if not login_sina():
        return
    # 写入数据前先清空之前的数据
    if os.path.exists(TOPIC_FILE_PATH):
        os.remove(TOPIC_FILE_PATH)
    # 批量爬取
    for i in range(1, 1000):
        print('第%d页' % i)
        spider_topic(i)
        # 设置一个时间间隔
        time.sleep(random.randint(0,1))
def analysis_sina_content():
    """
    分析微博内容
    :return:
    """
    with open(TOPIC_FILE_PATH,encoding='utf-8') as file:
        comment_txt = file.read()
    # 数据清洗，去掉无效词
    jieba.analyse.set_stop_words(STOP_WORDS_FILE_PATH)
    # 词数统计
    words_count_list = jieba.analyse.textrank(comment_txt, topK=50, withWeight=True)
    print(words_count_list)
    # 生成词云
    word_cloud = (
        WordCloud()
            .add("", words_count_list, word_size_range=[10, 100], shape=SymbolType.ROUND_RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="90后单身原因"))
    )
    word_cloud.render('word_cloud.html')
if __name__ == '__main__':
    # spider_topic()
    # patch_spider_topic()
    analysis_sina_content()