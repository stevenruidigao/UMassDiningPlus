import numpy as np
import torch
from transformers import YolosFeatureExtractor, YolosForObjectDetection
import cv2 as cv
from PIL import Image
import requests



#model = torch.load(r"yolov6s\\model.pt",weights_only=False)
#https://huggingface.co/facebook/detr-resnet-50

image = Image.open(r"hamp_north_full.png")
#load test images
testImgs = ["worcester_north_empty.png","worcester_north_full.png","worcester_south_empty.png","worcester_south_full.png",
            "berk_empty.png","berk_full.png",
            "hamp_north_empty.png","hamp_north_full.png","hamp_south_empty.png","hamp_south_full.png"]

imgs = []
for i in testImgs:
    imgs.append(cv.imread(i))
print(len(imgs)," images")


feature_extractor = YolosFeatureExtractor.from_pretrained("hustvl/yolos-tiny")
model = YolosForObjectDetection.from_pretrained("hustvl/yolos-tiny")

for n, img in enumerate(imgs):
    print("Next Image: "+testImgs[n])

    inputs = feature_extractor(images=img, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    target_sizes = torch.tensor([image.size[::-1]])
    results = feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]

    totalPeople = 0

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i) for i in box.tolist()]
        # let's only keep detections with score > 0.9
        if score > 0.7 and model.config.id2label[label.item()] == "person":
            print(
                f"Detected {model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )
            cv.rectangle(img,(box[0],box[1]),(box[2], box[3]),(0,255,0),2)
            totalPeople += 1
    print(totalPeople, "people")
    cv.imshow('output', img) 
    cv.waitKey()

cv.destroyAllWindows()