
import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image
import math

check = 0
count = 0
imgs = []

userinput = float(input("Enter a threshold value between 1 to 254 : "))
if (userinput <=254) and (userinput >=1 ):
    for x in range (0, 200):
        img = img = Image.open("rebelmrkt\\rebelmrkt_{}.jpg".format(x))
        img = np.float64(img)
        for height in range(0, len(img)):
            for width in range(0, len(img[height])):
               if (img[height][0][0] == img[height][width][0]) and (img[height][0][1] == img[height][width][1]) and (img[height][0][2] == img[height][width][2]):
                   count = count +1
            if count > 700:
                #new.append(str(x))
                count = 0
                check = 1
                break
            else:
                count = 0
        if (check==1):
            check = 0
            continue
        imgs.append(img)
        
     #to calculate average images   
    avg_img = imgs[0]
    
    for x in range(1, len(imgs)):
        avg_img += imgs[x]
    
    avg_img /= len(imgs)
    
    
    #to calculate standard deviation
    sd = ((imgs[0]-avg_img)**2)
    for x in range(1, len(imgs)):
        sd = sd + ((imgs[x]-avg_img)**2)
        
    sd = sd/(len(imgs)-1)
    sd = sd**(1/2)
    
    # ask threshold for user

    for height in range(0, len(avg_img)):
        for width in range(0, len(avg_img[height])):
            if (sd[height][width] > [userinput, userinput, userinput]).any() :
                avg_img[height][width] = [255.0, 0.0, 0.0]
                
    avg_img = np.clip(avg_img, 0 ,255)
    avg_img = np.uint8(avg_img)
    
    mplot.imshow(avg_img)
    mplot.show()
else:
    print("The threshold value is unresonable")

