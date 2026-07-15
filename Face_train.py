import numpy as np
from PIL import Image
import os
import cv2 as cv

def train_face(data_dir, model_save_path):
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []
    for image_path in path:
        if image_path == ".DS_Store":
            continue
        img = Image.open(image_path).convert("L")
        img_np = np.array(img, "uint8")
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces.append(img_np)
        ids.append(id)
        print(f"Processed image for ID: {id}")
    ids = np.array(ids)
    clf = cv.face.LBPHFaceRecognizer_create()
    print(clf)
    clf.train(faces, ids)
    clf.write(model_save_path)
train_face("face&eye/data", "face&eye/model/trainner.xml")