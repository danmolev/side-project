import cv2
import glob
import os 
import matplotlib.pyplot as plt
import numpy as np
import pickle
name = "Fin_Alph"
path = os.getcwd()+"/"+name


def make_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)

xTrain = []

j = 0

for i in range(0,79):
    for f in glob.iglob("Alp_rot/"+str(i+1)+"/*"):
        for d in range(0,10):
            j+=1


t = np.zeros((j,))
X = np.zeros((j,3600))
make_dir(path)

j=0
for i in range(0,79):
    print "making:", i
    make_dir(path+"/"+str(i+1))
    c = 0 
    for f in glob.iglob("Alp_rot/"+str(i+1)+"/*"):


        ls =  f.split("/")
        f_name = ls[-1].split(".")[0]

        img = cv2.imread(f,0)
        c+=1

        for d in range(0,5):
            new = 255-img
            row,col= img.shape
        
            sigma = 5*d
            gauss = np.random.normal(0,sigma,(row,col))
            gauss = gauss.reshape(row,col)
            noisy = new + gauss
            

            filename = path+"/"+str(i+1)+"/sig"+str(d)+'_'+f_name+'.png'
            # Using cv2.imwrite() method 
            # Saving the image 

            cv2.imwrite(filename,255-noisy)

            #X[j,:] = np.ndarray.flatten(noisy)
            #t[j] = i

            #j+=1



