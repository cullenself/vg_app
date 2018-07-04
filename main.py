from flask import Flask
from flask import request
from flask import render_template
import vg

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.files['picture'])
        print(request.form['method'])
        return render_template('output.html')
    else:
        return render_template('input.html', methods=vg.draw.methods)
