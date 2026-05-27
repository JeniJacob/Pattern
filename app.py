# app.py

from flask import Flask, render_template, request
import time

app = Flask(__name__)

def string_match(txt, pat):
    m = len(txt)
    n = len(pat)

    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    execution_time = ""

    if request.method == 'POST':
        txt = request.form['text']
        pat = request.form['pattern']

        stime = time.time()

        time.sleep(1)

        result = string_match(txt, pat)

        etime = time.time()

        execution_time = etime - stime - 1

    return render_template(
        'index.html',
        result=result,
        execution_time=execution_time
    )

if __name__ == '__main__':
    app.run()