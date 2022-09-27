import pandas as pd
from collections import defaultdict
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Ellipse
# from tensorflow.keras.applications import VGG16
# from tensorflow.keras.layers import Flatten
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.layers import Input
# from tensorflow.keras.models import Model
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.preprocessing.image import load_img
# from sklearn.model_selection import train_test_split

PATH = r"C:\Users\lptri\OneDrive\Documentos\Python_Scripts\FaceDetection\Datasets\FDDB-folds"
PATH_IM = r"C:\Users\lptri\OneDrive\Documentos\Python_Scripts\FaceDetection\Datasets"
all_files = os.listdir(PATH)

files = [x for x in all_files if len(x)>17]


with open(os.path.join(PATH,"FILE"), 'w') as outfile:
    for filename in files:
        with open((os.path.join(PATH,filename))) as infile:
            for line in infile:
                outfile.write(line)     

with open(os.path.join(PATH,"FILE"), 'r') as outfile:
    bbox_files= defaultdict(list)
    content =outfile.readlines()
    i=0
    
    for index, value in enumerate(content):
        if ("2002/" in value) or ("2003/" in value):
            value = value.replace("\n",".jpg")
            bbox_files[value]= [content[index + x].replace('  1\n','').split(" ") for x in range(2,int(content[index+1])+2)]

def plot_image(image_number, PATH_IM, bbox_files):
    
    n = 0
    for i in bbox_files:
               
        img = mpimg.imread(os.path.join(PATH_IM,i.replace("/","\\")))
        implot = plt.imshow(img)
        
        if n==image_number:
            for j in range(len((bbox_files[i]))):
                x = float(bbox_files[i][j][3])
                y = float(bbox_files[i][j][4])
                width = float(bbox_files[i][j][0])*2
                height = float(bbox_files[i][j][1])*2
                angle = -float(bbox_files[i][j][2])*4+90
                ax = plt.gca()
                ax.add_patch(Ellipse((x,y), width=width, height=height, angle=angle,edgecolor='red',facecolor='none',linewidth=1.5))
            print(i)
        if n==image_number:
            break
        n+=1

#plot_image(52, PATH_IM, bbox_files)

# for i in bbox_files:
#     img = load_img(PATH_IM,i.replace("/","\\"))
#     print(i)
#     break
