from flask import Flask

from threading import Thread

app = Flask('')

@app.route('/')

def home():

    return "uptimerobot.com'dan veya herhangi bir site hostlama aracını kullandığınızda onun gerçekten hostlandığını anlamak için yazmanız gereken bir mesaj"

def run():

  app.run(host='0.0.0.0',port=8080)

def keep_alive():  

    t = Thread(target=run)

    t.start()
