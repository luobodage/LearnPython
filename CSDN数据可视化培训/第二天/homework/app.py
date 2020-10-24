from flask import Flask, render_template

app = Flask(__name__)

@app.route('/html')
def two_day():
    title = '第二天的作业'
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(port=812)
