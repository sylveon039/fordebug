from __future__ import division, print_function, absolute_import
from flask import Flask,request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file'].read()
    fd = open('number.png','wb')
    fd.write(f)
    fd.close()
    num = func()
    return "Number recognition: " + str(num)


def func():
    img = Image.open('./number.png').convert('L')

    # resize
    if img.size[0] != 28 or img.size[1] != 28:
        img = img.resize((28, 28))

    arr = []

    for i in range(28):
        for j in range(28):
            pixel = 1.0 - float(img.getpixel((j, i)))/255.0
            arr.append(pixel)
    arr_1 = np.array(arr, dtype='f').reshape(1, 784)

    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    x = tf.placeholder(tf.float32, [1, 784])

    saver = tf.train.Saver()
    sess = tf.InteractiveSession()
    saver.restore(sess, "data/model.ckpt")

    y = tf.matmul(x, W) + b
    result = sess.run(y, feed_dict={x:arr_1})
    number = np.argmax(result)
    return number


@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
    <body>
    <form action='/upload' method='post' enctype='multipart/form-data'>
        <input type='file' name='file'>
    <input type='submit' value='Upload'>
    </form>
    '''
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=False)