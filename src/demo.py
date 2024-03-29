# -*- coding: utf-8 -*-
"""demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ILvphBbajliCd8a-JkPAJg5RtOzyWf2z
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def demo(image_file, model):
    
    '''
    A demo
    Print the image and the model's prediction for it
    
    Arguments
    ---------
    image_file: name of the image file
    
    model:      model used
    
    '''
    
    
    # plt.imread reads an image from a file into an array
    # cv2.resize resizes an image
    # INTER_AREA – resampling using pixel area relation.
    #              It may be a preferred method for image decimation,
    #              as it gives moire’-free results.
    #              But when the image is zoomed,
    #              it is similar to the INTER_NEAREST method (a nearest-neighbor interpolation)
    img = cv2.resize(plt.imread(image_file),
                     dsize=(128, 128), # to resize to (128, 128)
                     interpolation=cv2.INTER_AREA)
    img = img * 1.0 / 255
    
    print("Original Image:")
    plt.figure(1)
    plt.imshow(plt.imread(image_file))
    plt.show()
    
    print("Processed Image:")
    plt.figure(2)
    plt.imshow(img)
    plt.show()
    
    img = np.expand_dims(img, axis=0)
    pred = model.predict_classes(img)
    
    if pred[0] == 0:
        print("Prediction: Comfort Inn")
    elif pred[0] == 1:
        print("Prediction: Best Western")
    else:
        print("Prediction: Hilton")