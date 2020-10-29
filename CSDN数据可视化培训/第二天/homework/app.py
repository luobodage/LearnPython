from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def two_day():
    title = '全国计程车统计'
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(port=812)
