from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from sklearn import neural_network, utils, discriminant_analysis
from sklearn.neighbors import KNeighborsClassifier

import cv2






def setNN(xTrain,tTrain):
    l = 1           # layers
    s = 'sgd'       # stochastic gradient descent
    lr = 10        # learning rate
    t = 10**(-8)    # tolerance
    mi = 1000       # maximum iterations
    a = "logistic"
    
    
    
    NN = neural_network.MLPClassifier(verbose=True)

    NN.fit(xTrain,tTrain) #Fiting 
    print NN.score(xTrain,tTrain)
    return NN
    

im = Image.open('sample2.png').convert('L')


im2 = cv2.imread('sample2.png',0)


plt.figure()
plt.imshow(im2,cmap='Greys', interpolation='nearest')

xTrain = []
tTrain = []
j= 0
for i in range(0,79):
    for f in glob.iglob("Alphabet/"+str(i+1)+"/*"):
 
       #c = Image.open(f).convert('L')
       #a = np.asarray(c)
       #xTrain.append(255-a)
 
       c = 255 - np.asarray(Image.open(f))
       
      

       xTrain.append(c.flatten())
       tTrain.append(i)
       j+=1

xTrain = np.array(xTrain)
tTrain = np.array(tTrain)

#sigma = 10
#noise = sigma*np.random.normal(size=np.shape(xTrain)) 
#xTrain = xTrain + noise

#NN = setNN(xTrain,tTrain)
#print NN.score(xTrain,tTrain)


model = discriminant_analysis.QuadraticDiscriminantAnalysis()
model = model.fit(xTrain,tTrain)
print model.score(xTrain,tTrain)

#print xTrain.shape 
#im.show()


#neigh = KNeighborsClassifier(n_neighbors=3)
#neigh.fit(xTrain,tTrain)
#print neigh.score(xTrain,tTrain)

a = np.asarray(im)
a = 255 - a





all_lines = []
line = []

white_line = np.full(im.size[0],255,dtype=int)





for row in a:

 

    if np.sum(row) > 0:
        line.append(row)
    else:
        if line != []:
            all_lines.append(np.array(line))
            line = []




all_letters = []
letter = []

for l in all_lines:
    for col in l.T:
        if 500 < np.sum(col)  :
            letter.append(col)

        else:
            if letter != []:
                all_letters.append(np.array(letter).T)
                letter = []
       

plt.figure()

ln = len(all_letters)




flat = []

print "starting..."

for i in range(0,ln):


    p = plt.subplot(10, ln/10 + 1, i+1)


    new = resize(all_letters[i], (60, 60))

    flat.append(new.flatten())

    


    plt.imshow(new,cmap='Greys', interpolation='nearest')
 
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)




flat = np.array(flat)


l = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z','A','B',"C",
        "D","E","F","G","H","I","J",'K','L','M',
        'N','O','P','Q','R','S','T','U','V','W',
        'X','Y','Z','1',"2","3","4","5","6","7",
        "8","9","0",",",";",":","?","!",".","@",
        "#","$","%","&","(",")","{","}","[","]"]
		
for p in model.predict(flat):
    print l[p],

plt.show()