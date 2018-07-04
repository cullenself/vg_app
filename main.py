from flask import Flask
from flask import request
from flask import render_template
import vg

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        img = vg.draw.readImageFromFile(request.files['picture'])
        out = vg.draw.rect(img, svgOutput=False).decode('utf-8')
        return render_template('output.html', img=out)
    else:
        return render_template('input.html', methods=vg.draw.methods)
