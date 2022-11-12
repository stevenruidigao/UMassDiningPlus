import numpy as np
import cv2 as cv

testImgs = ["worcester_north_empty.png","worcester_south_empty.png","berk_empty.png","hamp_north_empty.png","hamp_south_empty.png"]

imgs = []
for i in testImgs:
    imgs.append(cv.imread(i))
'''px = img[0,0]
print( px )'''
'''
openCV Cascade models:

haarcascade_fullbody.xml
haarcascade_upperbody.xml <<<
haarcascade_lowerbody.xml
'''
bodyCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_upperbody.xml')


for img in imgs:
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    people = bodyCascade.detectMultiScale(grayscale, 1.1, 1)

    print("empty ",len(people))

    for (x,y,w,h) in people: 
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
    # Display frames in a window  
    cv.imshow('output', img) 
    cv.waitKey()
cv.destroyAllWindows()