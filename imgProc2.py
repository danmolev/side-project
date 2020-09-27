from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from sklearn import neural_network, utils, discriminant_analysis
from sklearn.neighbors import KNeighborsClassifier

from sklearn.utils import shuffle
import cv2
import pickle



num_files = 0 
for i in range(0,79):
    for f in glob.iglob("Fin_Alph/"+str(i+1)+"/*"):
        num_files+=1

X = np.zeros((num_files,3600))
t = np.zeros(num_files)

c=0
for i in range(0,79):
    print "reading", i+1
    for f in glob.iglob("Fin_Alph/"+str(i+1)+"/*"):
        X[c,:] = cv2.imread(f,0).flatten()
        t[c] = i
        c+=1


print t[1000]
plt.imshow(X[1000,:].reshape(60,60),cmap='Greys', interpolation='nearest')

X,t = shuffle(X, t)

plt.figure()

print t[1000]
plt.imshow(X[1000,:].reshape(60,60),cmap='Greys', interpolation='nearest')
plt.show()

pickle.dump((X[:10000],t[:10000]), open( "batch_10000.p", "wb" ))




        
        


