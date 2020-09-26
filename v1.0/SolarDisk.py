#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.04 by GPoli
#..Last Version.....: 2013.03.04 by GPoli
#********************************************************************

import numpy as np
import Image as im
import math

from ImageTools import *
from GLCM       import *
from Window     import *

class SolarDisk:
    def __init__(self, img_rgb, solar_disk_name, threshold, size,probe_func_list):
        img_tools         = ImageTools()
        self.size         = size
        self.img_rgb      = img_rgb
        self.threshold    = threshold
        self.img_gray     = img_tools.rgb2gray(self.img_rgb,self.threshold)
        self.pattern_name = solar_disk_name
        self.arr_image    = img_tools.img2arr(self.img_gray)
        self.lst_windows  = self.generateFixedWindows(self.arr_image,self.size,probe_func_list)
    
    def generateFixedWindows(self,arr_image,size,probe_func_list):
        lst_windows = []
        count = 0
        for begin_l in xrange(0, arr_image.shape[0], size[0]):
            for begin_c in xrange(0, arr_image.shape[1], size[1]):
                arr_window = np.zeros(size)
                for i in range(begin_l,begin_l+size[0]):
                    for j in range(begin_c,begin_c+size[1]):
                        if i >= arr_image.shape[0]:
                            break
                        if j >= arr_image.shape[1]:
                            break
                        arr_window[i-begin_l][j-begin_c] = arr_image[i][j]
                tmp_window = Window(begin_l, begin_c, arr_window,probe_func_list)
                lst_windows.append(tmp_window)
                #im.fromarray(np.uint8(arr_window)).save(path_save+prefix+"_win_"+str(begin_l)+"_"+str(begin_c)+".jpg")
                #print ".|..save window # " + str(count)
                count = count + 1
        return lst_windows
