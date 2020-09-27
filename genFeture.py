import cv2
import glob
import os 
import matplotlib.pyplot as plt
import numpy as np
import pickle

name = "Alphabet"
path = os.getcwd()+"/"+name


imgs = []

for i in range(0,79):
    for f in glob.iglob("Alphabet/"+str(i+1)+"/1.png"):
        
        cv2.imshow("hi",cv2.imread(f,0))
        cv2.waitKey(0)


imgs = np.array(imgs)

for i in imgs:
    cv2.imshow("hi",i)
    cv2.waitKey(0)

def getPixelDensity(imgs):
    
        #np.ones((imgs.shape[0],))    
        return np.matmul(imgs.T, np.ones((imgs.shape[0],)))
    
    

#for i in getPixelDensity(imgs)


