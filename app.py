from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reviewform.html')

if __name__ == '__main__':
    app.run(debug=True)
