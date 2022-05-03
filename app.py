import os
from flask import Flask,render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import webbrowser
from threading import Timer

subscription_key = "b58bec6a7f4e4f95bb4a6e4972ba81ed"
endpoint = "https://euservergerm.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = __file__.split("app.py")[0] + '/static'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        image = app.config['UPLOAD_FOLDER'] + '/' + filename
        image = open(image, "rb")
        data = computervision_client.describe_image_in_stream(image)
        desc = ""
        confidence = 0
        tags = ""

        for t in data.tags:
            tags = tags + t + ", "

        for d in data.captions:
            desc = d.text
            confidence = round(d.confidence*100, 2)

        return render_template("interface.html", desc=desc, confidence=confidence, tags=tags, meta=data.metadata, filename=filename)
    else:
        return render_template("interface.html", desc="")
def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    Timer(1, open_browser).start() 
    app.run(port=5000)
    app.run(debug=True)