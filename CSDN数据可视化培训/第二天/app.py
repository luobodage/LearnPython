from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world1():
    return '欢迎来到这个啥都没有的网站 127.0.0.1:812/html 域名后缀加html进入二级域名'

@app.route('/html')
def hello_world():
    date_time = "2020年"
    return render_template('01.html', date_time=date_time, title="第一次作业")


if __name__ == '__main__':
    app.run(port=812)
