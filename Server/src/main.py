from app import app
from bson import json_util
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)