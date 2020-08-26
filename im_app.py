#!/usr/bin/env python
# coding: utf-8



import tensorflow as tf 
import cv2
import numpy as np 


model = tf.keras.models.load_model('/Users/thiraprarom/Botnoi/imgcls.h5')


classDict = {0: 'condo',1: 'house',}

# Create pipeline
def predictImage(image):
    data = []
    image = cv2.imread(image,cv2.IMREAD_COLOR)
    image = cv2.resize(image, (28, 28))
    label = classDict
    data.append(image)
    data = np.array(data)
    data = data/255.0
    prob = model.predict(data)
    predict = np.argmax(prob)
    label = classDict[predict]
    confident = prob[0][predict]
    return label, confident



predictImage('/Users/thiraprarom/Botnoi/im_cls/condo/30.jpg')

