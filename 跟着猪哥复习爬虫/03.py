
import requests
import json
import os

def spider_comment():
    # 爬取京东评论
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1070129528&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    comment_file_path = 'c:/Users/萝卜ovo/Desktop/Python/ImportGitHub/跟着猪哥复习爬虫/id.txt'
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
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for r_json_comments in r_json_comments:
        with open(comment_file_path,'a+') as file:
            file.write(r_json_comments['content'] + '\n')
        print(r_json_comments['content'])

if __name__ == '__main__':
    spider_comment()