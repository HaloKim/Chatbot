from flask import Flask, render_template, redirect, request, url_for
import time
import flask_test
import json
from collections import OrderedDict
info = OrderedDict()

result = flask_test.Test()
app = Flask(__name__)


@app.route('/')
@app.route('/<string:qna>')
def inputTest(qna=None):
    return render_template('layout.html', qna=qna)


@app.route('/calculate', methods=['POST'])
def calculate(qna=None):
    if request.method == 'POST':
        question = request.form['qna']
        answer = result.return_value(question)
        info["Title"] = "채팅로그"
        info["Time"] = time.strftime('%y-%m-%d %H:%M:%S')
        info["Question"] = question
        info["Answer"] = answer
        with open("Chat_Log.txt", "a+", encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent="\t")
    else:
        qna = None

    return redirect(url_for('inputTest', qna=answer))


if __name__ == '__main__':
    app.run()
