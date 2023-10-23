from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('ile:///C:/Users/use/OneDrive/Desktop/new%20E%20comace%20site/index.html')
def hello_world(name=None):
    return render_template('index.html', name=name)


