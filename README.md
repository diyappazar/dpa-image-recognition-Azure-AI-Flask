# Image Recognition Flask App

This is a Flask app that allows you to recognize images using Azure Cognitive Services/Computer Vision. 

## Prerequisites
* An Azure account. Learn how to create a free account in Create an [Azure account for students](https://azure.microsoft.com/en-us/free/students/?WT.mc_id=academic-0000-cxa)
* [Python3.6](https://www.python.org/downloads/) or later and VS code installed on your computer. 
* [Visual Studio Code](https://code.visualstudio.com/) should be installed. Choose the Visual Studio Code that works for your configuration: Windows, Linux, or macOS.
* Install the Flask library using pip: `pip install Flask`

## Set up Azure Cognitive Services/Computer Vision Account
1. Go to the [Azure portal](https://portal.azure.com/) and sign in with your Azure account.
2. Click on "Create a resource" and search for "Computer Vision".
3. Click on "Create" and fill in the required information.
4. Once the resource has been created, click on "Keys and Endpoint" in the left menu.
5. Copy the "Endpoint" and one of the "Keys" and save them for later use.

## Run the App
1. Create a new Python file in your project directory and paste in the following code:

```python
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = request.form['image_url']
        subscription_key = "your_subscription_key"
        endpoint = "your_endpoint"
        
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key,
        }
        
        data = '{"url": "' + image_url + '"}'
        
        response = requests.post(endpoint, headers=headers, data=data)
        response.raise_for_status()
        
        analysis = response.json()
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        
        return render_template('index.html', image_caption=image_caption)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()

```

## Representation: 
https://user-images.githubusercontent.com/65700836/166441391-51e3a9f9-1525-461b-95a0-9f3909466d0e.mp4

