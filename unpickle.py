import cv2
import glob
import os 
import matplotlib.pyplot as plt
import numpy as np
import pickle

from sklearn import neural_network, discriminant_analysis
from sklearn.neighbors import KNeighborsClassifier


X, t  = pickle.load(open( "batch_10000.p", "rb" ) )



Xs = X[0:8000]
ts = t[0:8000]

Xv = X[9000:]
tv = t[9000:]

l = (80,160,80,40,20,10)           # layers
s = 'adam'       # stochastic gradient descent
lr = 0.00001        # learning rate
t = 10**(-5)    # tolerance
mi = 400      # maximum iterations
a = "logistic"

NN = neural_network.MLPClassifier(l,solver=s,learning_rate_init=lr,tol=t,verbose=True,
learning_rate="adaptive", max_iter=mi)
NN.fit(Xs,ts)
print(NN.score(Xv,tv))

pickle.dump(NN, open( "NN_model.p", "wb" ))