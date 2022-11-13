import numpy as np
import torch
from transformers import DetrFeatureExtractor, DetrForObjectDetection
import cv2 as cv
from PIL import Image
import streamData as sd
import time
import csv
import json
import redis



#model = torch.load(r".\yolov6s\model.pt")
#https://huggingface.co/facebook/detr-resnet-50

#for size rescaling
image = Image.open(r"hamp_north_full.png")

camNames = ["worcester_south","worcester_north","berk_entrance","hamp_south","hamp_north"]
diningNames = ["worcester","berkshire","hampshire"]
maxActivity = [52,11,46] #maximum number of people seen in each dining hall
'''
worcester_south 23
worcester_north 29
berk_entrance 11
hamp_south 27
hamp_north 19
'''

diningStreams = ["https://www.youtube.com/watch?v=89KPOnjHEC4","https://www.youtube.com/watch?v=7wHgOpwHz8k",
"https://www.youtube.com/watch?v=70PKbo5ouIM","https://www.youtube.com/watch?v=RprORF_ggOA","https://www.youtube.com/watch?v=TWC87AgKJHA"]

#ML model
confidenceThreshold = 0.7

feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

#connect to database
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def updateLoads(location, load):
   loads = json.loads(redis_client.get('umadp:location:' + location + ':loads'))
   loads.append(load)
   redis_client.set('umadp:location:' + location + ':loads', json.dumps(loads))

def getLoads(location):
    return json.loads(redis_client.get('umadp:location:' + location + ':loads'))

#calculate the activity level
def getActivity(newActivity):
    people = [0] * len(diningNames)

    history = calcHistory(newActivity)
    
    #worcester
    people[0] = (history[0] + history[1])/maxActivity[0]

    #berk
    people[1] = (history[2])/maxActivity[1]

    #hamp
    people[1] = (history[3] + history[4])/maxActivity[2]
    return people
    
recentCaptures = 5; #number of previous recordings to account for
def calcHistory(newActivity):
    avg = [0] * len(camNames)
    i = 0
    with open('people_data.csv', 'r') as csvfile:
        for row in reversed(list(csv.reader(csvfile))):
            for j in range(len(row)-1):#don't scan the date column
                avg[j] += row[j]/recentCaptures
            if (i > recentCaptures-1):
                break
            i += 1
        
        for j in range(len(row)-1):
            avg[j] += newActivity[j]
    return avg

#continuously run
while True:
    totalPeople = []
    for i, stream in enumerate(diningStreams):
        try:
            frame = sd.getYoutubeFrameAtTime(stream, save_image=False)

        except:
            totalPeople.append(0)
            continue

        inputs = feature_extractor(images=frame, return_tensors="pt")
        outputs = model(**inputs)

        # convert outputs (bounding boxes and class logits) to COCO API
        target_sizes = torch.tensor([image.size[::-1]])
        results = feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]

        totalPeople.append(0)

        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(j) for j in box.tolist()]
            # pick out and count the "person" labels
            if score > confidenceThreshold and model.config.id2label[label.item()] == "person":
                totalPeople[i] += 1
        print("people in",camNames[i],totalPeople[i])
    
    #calculate activity level
    activity = getActivity(totalPeople)

    #update database
    for n in range(len(activity)):
        updateLoads(diningNames[n], activity[n])

    #record data
    totalPeople.append(time.strftime("%a, %d %b %H:%M:%S", time.localtime()))
    with open("people_data.csv", 'a') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)
            
        # writing the data rows 
        csvwriter.writerow(totalPeople)
    
    #wait
    time.sleep(30)


