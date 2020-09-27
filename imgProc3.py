from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from sklearn import neural_network, utils, discriminant_analysis
from sklearn.neighbors import KNeighborsClassifier

import cv2
import pickle



all_lines = []
line = []

im = Image.open('sample2.png').convert('L')
a = np.asarray(im)



for row in a:
    if np.sum(255-row) > 0:
        line.append(row)
    else:
        if line != []:
            all_lines.append(np.array(line))
            line = []

all_letters = []
letter = []

for l in all_lines:
    for col in l.T:
        if 500 < np.sum(255-col)  :
            letter.append(col)

        else:
            if letter != []:
                let = np.array(letter).T

                w = let.shape[0]
                h = let.shape[1]

        

                if(w>h):
                    s = w + w/10
                    
                else:
                    s = h + h/10

                let_fin = np.zeros((s, s))+255

                cw = (let_fin.shape[0] - w)/2
                ch = (let_fin.shape[1] - h)/2

                

                let_fin[cw:cw+w,ch:ch+h] = let

                
                #sigma = 25
                #gauss = np.random.normal(0,sigma,(s,s))
                #gauss = gauss.reshape(s,s)
                #noisy = let_fin + gauss
                
                
                all_letters.append(resize(let_fin,(60,60)))
                letter = []
       

plt.figure()
ln = len(all_letters)

flat = []
print "starting..."
for i in range(0,ln):
    p = plt.subplot(10, ln/10 + 1, i+1)

   
    new = cv2.resize(all_letters[i], (60, 60), interpolation=4)

    flat.append(255-new.reshape(3600,))
    plt.imshow(255-new.reshape(3600,).reshape(60,60),cmap='Greys')
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

model = pickle.load(open( "NN_model.p", "rb" ) )
		
for p in model.predict(flat):
    print l[int(p)],

plt.show()