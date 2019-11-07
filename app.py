from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
