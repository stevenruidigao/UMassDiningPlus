import numpy as np
import cv2 as cv #pip install opencv-python

testImgs = ["worcester_north_empty.png","worcester_north_full.png","worcester_south_empty.png","worcester_south_full.png",
            "berk_empty.png","berk_full.png",
            "hamp_north_empty.png","hamp_north_full.png","hamp_south_empty.png","hamp_south_full.png"]

imgs = []
for i in testImgs:
    imgs.append(cv.imread(i))
print(len(imgs)," images")
'''px = img[0,0]
print( px )'''
'''
openCV Cascade models:

haarcascade_fullbody.xml
haarcascade_upperbody.xml <<<
haarcascade_lowerbody.xml
'''
#cascade
bodyCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_upperbody.xml')

#hog
# initialize the HOG descriptor/person detector
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

for i, img in enumerate(imgs):
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    #using cascade
    people = bodyCascade.detectMultiScale(grayscale, 1.1, 1)
    for (x,y,w,h) in people: 
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    #using hog
    boxes, weights = hog.detectMultiScale(grayscale, winStride=(8,8) )
    for (x,y,w,h) in boxes: 
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    #print predictions
    print(testImgs[i]+": ", len(people), len(boxes))
    

    # Display frames in a window  
    cv.imshow('output', img) 
    cv.waitKey()
cv.destroyAllWindows()