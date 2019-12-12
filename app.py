from flask import Flask, render_template, request
import os
import io
from PIL import Image
import numpy as np
from keras.models import model_from_json

app = Flask(__name__)
model = model_from_json(open('pkl_objects/model.json').read())
model.load_weights('pkl_objects/model.h5')

@app.route('/')
def index():
    return render_template('reviewform.html')

def predict(image):
    image = image.resize((28, 28))
    image = image.convert('P')
    image = np.array(image)
    image = image.reshape(784)
    image = np.expand_dims(image, axis=0)
    print(image)
    preds = model.predict(image)

    return np.where(preds == preds.max())[1][0]

@app.route('/results', methods=['POST'])
def results():
    lhs_img = Image.open(io.BytesIO(request.files['lhs'].read()))
    rhs_img = Image.open(io.BytesIO(request.files['rhs'].read()))
    operation = request.form['operation']

    lhs = predict(lhs_img)
    rhs = predict(rhs_img)

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    return f'{lhs} {operation} {rhs} = {operations[operation](lhs, rhs)}\n'


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
