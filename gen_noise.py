import cv2
import glob
import os 
import matplotlib.pyplot as plt

name = "Alp_rot"
path = os.getcwd()+"/"+name


def make_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)

xTrain = []



make_dir(path)
for i in range(0,79):
    make_dir(path+"/"+str(i+1))
    c = 0 
    for f in glob.iglob("Alphabet/"+str(i+1)+"/*"):
        c+=1

        for d in range(-10,11):
            
            if d == 0:
                continue

            img = cv2.imread(f,0)
            img = 255-img

            # get image height, width
            (h, w) = img.shape[:2]
            # calculate the center of the image
            center = (w / 2, h / 2)

            M = cv2.getRotationMatrix2D(center, d, 1.0)
            rotated = cv2.warpAffine(img, M, (h, w))

            filename = path+"/"+str(i+1)+"/"+str(d)+'_'+str(c)+'.png'
  
            # Using cv2.imwrite() method 
            # Saving the image 
            cv2.imwrite(filename, 255-rotated) 


            
print "hi" 
plt.show()

