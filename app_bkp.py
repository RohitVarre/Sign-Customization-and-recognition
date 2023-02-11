#Import necessary libraries
from flask import Flask, render_template, Response, jsonify
import tensorflow as tf
import os
import mediapipe as mp
import pandas as pd
import cv2
import numpy as np



#Initialize the Flask app
app = Flask(__name__)



## Intialize the model

code = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 
        8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 
        16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y'}

# Load the trained model
model = tf.keras.models.load_model('mediapipe.h5')


cap = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        ret,frame = cap.read()
        image = frame
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
            

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sign')
def sign():
    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)


if __name__ == "__main__":
    app.run()