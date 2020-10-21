import pymysql
from pyecharts.charts import Bar

if __name__ == '__main__':

    bar = Bar()
    bar.add_xaxis(["帽子"])
    #  获取游标
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='zxc4525577',
        charset='utf8',
        db='test',
        cursorclass=pymysql.cursors.DictCursor  # 指定类型
    )
    cursor = connect.cursor()

    sql = "select * from shopping"

    cursor.execute(sql)

    data = cursor.fetchall()

    for data_1 in data:
        a = []
        a.append(data_1['hat'])
        bar.add_yaxis(data_1['shop'], a)
    bar.render()
