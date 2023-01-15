# -*- coding: utf-8 -*-
"""Mosquito Larvae Testing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vrIQ0FNaJxfvp7Iw3NnMPm1p9KKs0aKa

# Installing dependencies and APIs
"""

!pip install requests pillow requests_toolbelt

!pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="Zr84egV6YQLKRBydHsDv")

# using the workspace method on the Roboflow object
workspace = rf.workspace("thesis-ormgx")

# identifying the project for upload
project = workspace.project("mosquito-larvae-dataset")

"""# Drive path installment"""

from google.colab import drive #Importing google drive account

drive.mount("/content/gdrive")

from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
from os import listdir
from roboflow import Roboflow
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

import requests
import base64
import io
import os
import glob
import shutil
import cv2

#======================================================================================================================================================

        #UNCOMMENT FOR AEDES TESTING

# Images_link = "/content/gdrive/MyDrive/For testing/Aedes" #If google drive option is used, insert parth of the source google drive here
# !mkdir results_folder
# Results_folder = "/content/results_folder" #Insert path where you want the results to be saved

# path = "/content/results_folder"
# if os.path.exists(path):
#  img = cv2.imread(path)
# else:
#  print("Path does not exist:", path)

# # obtaining your API key: https://docs.roboflow.com/rest-api#obtaining-your-api-key
# rf = Roboflow(api_key="Zr84egV6YQLKRBydHsDv")
# workspace = rf.workspace("thesis-ormgx")
# version = project.version(16)
# project = workspace.project("mosquito-larvae-dataset")
# model = version.model

#======================================================================================================================================================

         # #UNCOMMENT FOR ANOPHELES TESTING

# Images_link = "/content/gdrive/MyDrive/For testing/Anopheles" #If google drive option is used, insert parth of the source google drive here
# !mkdir results_folder
# Results_folder = "/content/results_folder" #Insert path where you want the results to be saved

# path = "/content/results_folder"
# if os.path.exists(path):
#   img = cv2.imread(path)
# else:
#   print("Path does not exist:", path)

# # obtaining your API key: https://docs.roboflow.com/rest-api#obtaining-your-api-key
# rf = Roboflow(api_key="Zr84egV6YQLKRBydHsDv")
# workspace = rf.workspace("thesis-ormgx")
# version = project.version(14)
# project = workspace.project("mosquito-larvae-dataset")
# model = version.model

#======================================================================================================================================================

        #UNCOMMENT FOR CULEX TESTING

# Images_link = "/content/gdrive/MyDrive/For testing/Culex" #If google drive option is used, insert parth of the source google drive here
# !mkdir results_folder
# Results_folder = "/content/results_folder" #Insert path where you want the results to be saved

# path = "/content/results_folder"
# if os.path.exists(path):
#   img = cv2.imread(path)
# else:
#   print("Path does not exist:", path)

# # obtaining your API key: https://docs.roboflow.com/rest-api#obtaining-your-api-key
# rf = Roboflow(api_key="Zr84egV6YQLKRBydHsDv")
# workspace = rf.workspace("thesis-ormgx")
# version = project.version(16)
# project = workspace.project("mosquito-larvae-dataset")
# model = version.model

#======================================================================================================================================================

# Testing iteration to each images
raw_data_location = Images_link
for raw_data_extension in ['.jpg', '.jpeg', 'png']:
## using the following line for raw_data_externsion results in inference on
## specified file types only
# raw_data_extension = ".jpg" # e.g jpg, jpeg, png
    globbed_files = glob.glob(raw_data_location + '/*' + raw_data_extension)
    for img_path in globbed_files:
        predictions = model.predict(img_path, confidence=40, overlap=30)
        # save prediction image
        predictions.save(f'inferenceResult_{os.path.basename(img_path)}')
        predictions_json = predictions.json()
        # print(predictions_json)

src_dir = "/content" # DONT CHANGE; Directory where the results from iteration comes from
dst_dir = Results_folder #Directory Folder
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.move(jpgfile, dst_dir)

path='/content/results_folder'
image=os.listdir(path)
type(image)

src_dir = "/content" # DONT CHANGE; Directory where the results from iteration comes from
dst_dir = Results_folder #Directory Folder
for jpgfile in glob.iglob(os.path.join(src_dir, "*.png")):
    shutil.move(jpgfile, dst_dir)

path='/content/results_folder'
image=os.listdir(path)
type(image)


img_data=[]
for img in image:
  img_arr=cv2.imread(os.path.join(path,img))
  img_rgb = cv2.cvtColor(img_arr,cv2.COLOR_BGR2RGB)
  # plt.figure()
  # plt.imshow(im_rgb)
  img_data.append(img_rgb)

plt.figure(figsize=(25,25))
for i in range(len(img_data)):
  plt.subplot(6,3,i+1)
  plt.imshow(img_data[i])

import os
import glob
import shutil

files = glob.glob('/content/results_folder/*')
for f in files:
    os.remove(f)

shutil.rmtree('/content/results_folder')