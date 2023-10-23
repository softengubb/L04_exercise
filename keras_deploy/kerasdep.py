import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:7403/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Serialize the result, you can add additional fields
        return jsonify(result='Goldfish', probability='99.999')

    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7403)
