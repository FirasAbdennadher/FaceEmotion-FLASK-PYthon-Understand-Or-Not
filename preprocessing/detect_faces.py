# USAGE
# python detect_faces.py --image 20frame220.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
import numpy as np

import cv2
from PIL import Image   
# construct the argument parse and parse the arguments

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")

# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it

for k in range(273):
    image = cv2.imread(str(k)+".jpg")
    
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
    	(300, 300), (104.0, 177.0, 123.0))
    # pass the blob through the network and obtain the detections and
    # predictions
    print("[INFO] computing object detections...")
    net.setInput(blob)
    detections = net.forward()
    
    # loop over the detections
    for i in range(0, detections.shape[2]):
    	# extract the confidence (i.e., probability) associated with the
    	# prediction
    	confidence = detections[0, 0, i, 2]
    
    	# filter out weak detections by ensuring the `confidence` is
    	# greater than the minimum confidence
    	if confidence > 0.5:
            im = Image.open(str(k)+".jpg").convert('L')
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            
            im = im.crop((startX, startY, endX, endY))
            im.save(str(k)+'.jpg')
    
    # show the output image
    ##cv2.imshow("Output"+str(k), image)
    cv2.waitKey(0)