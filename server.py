from flask import Flask, render_template

from blueprints.stock import stock


app = Flask(__name__)

app.register_blueprint(stock)

@app.route('/')
def index():
    return render_template('index.html')