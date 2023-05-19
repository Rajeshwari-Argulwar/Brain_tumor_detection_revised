#http://buffml.com/

from keras.models import load_model
from keras.utils import load_img ,img_to_array
from PIL import Image
import cv2
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# dic = {0: 'Normal', 1: 'Doubtful', 2: 'Mild', 3: 'Moderate', 4: 'Severe'}
dic = {0: 'NOT DETECTED', 1: 'DETECTED'}

# Image Size
img_size = 240
model = load_model('brain_tumor_detector.h5')

def predict_label(img_path):
    image = cv2.imread(img_path, 1)
    print('image path', img_path)
    resized = cv2.resize(image, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    # i = np.array(resized) / 255.0
    resized = resized / 255.
    image = resized.reshape((1 ,240, 240, 3))
    print('I shape ',image)
    p = model.predict(image)
    print('result', p)
    # predicted_class = np.argmax(p, axis=1)
    # print('predicted class',predicted_class)
    if p[0][0] >0.5:
        res = 'Tumer detected'
    elif p[0][0] <= 0.5:
        res = 'Tumer not deteceted'
    return (res, p[0][0]*100)

# Routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html") 

@app.route("/predict", methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        img_path = "uploads/" + img.filename
        img.save(img_path)
        p = predict_label(img_path)
        print(p)
        return str(p).lower()

if __name__ == '__main__':
    app.run(debug=True)



