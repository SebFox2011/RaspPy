from flask import Flask
from flask import render_template  # jinja2
from led import clignote
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
thread = Thread(target = clignote)
thread.start()
#thread.join()
print("thread lancé")