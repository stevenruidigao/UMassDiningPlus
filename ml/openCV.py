import numpy as np
import cv2
import frames
import time

'''
openCV Cascade models:

haarcascade_fullbody.xml
haarcascade_upperbody.xml <<<
haarcascade_lowerbody.xml
'''

diningStreams = {
   "Worcester South": "https://www.youtube.com/watch?v=89KPOnjHEC4",
   "Worcester North": "https://www.youtube.com/watch?v=7wHgOpwHz8k",
   "Berkshire Entrance": "https://www.youtube.com/watch?v=70PKbo5ouIM",
   "Hampshire South": "https://www.youtube.com/watch?v=RprORF_ggOA",
   "Hampshire North": "https://www.youtube.com/watch?v=TWC87AgKJHA",
}

bodyCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

while True:
   for key in diningStreams:
      frame = frames.getYoutubeFrameAtTime(diningStreams[key], save_image=False)
      grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      people = bodyCascade.detectMultiScale(grayscale, 1.1, 1)

      for (x,y,w,h) in people: 
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

      cv2.imwrite(diningStreams[key].split("=")[1]+"_rect.png", frame)
   time.sleep(30)