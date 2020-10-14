from flask.app import Flask
from flask import   render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

app = Flask(__name__,static_folder=STATIC_DIR,template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
