from flask import Flask
from flask import request
from flask import render_template
import vg

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        for key in vg.INPUTS:
            print(key)
            vg.INPUTS[key]['val'] = vg.INPUTS[key]['clean'](request.form[key])
        img = vg.draw.readImageFromFile(request.files['picture'])
        meth = vg.draw.methods[request.form['method']]
        out = meth(img, svgOutput=False, b64Output=True).decode('utf-8')
        return render_template('output.html', img=out)
    else:
        print(vg.INPUTS)
        return render_template('input.html', methods=vg.draw.methods, inputs=vg.INPUTS)
