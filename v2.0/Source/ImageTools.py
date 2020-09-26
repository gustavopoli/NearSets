#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.02.28 by GPoli
#..Last Version.....: 2013.02.28 by GPoli
#********************************************************************

import numpy as np
import Image as im
import math

class ImageTools:
    
    def img2arr(self,img_gray):
        return np.asarray(img_gray)
    
    def arr2img(self, arr_image):
        return im.fromarray(np.uint8(arr_image))

    
    def rgb2gray(self, image, max_val):
        print ".|....converting image RGB to Grayscale"
        val     = 0
        img_gray = im.new("L",image.size)
        pixels = img_gray.load()
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                R, G, B = image.getpixel((i,j))
                val = 0.3*R + 0.59*G + 0.11*B
                if max_val > 0:
                    if val < max_val:
                        val = 0
                pixels[i,j] = val - max_val
        return img_gray