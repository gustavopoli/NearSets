#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.02.28 by GPoli
#..Last Version.....: 2013.03.04 by GPoli
#********************************************************************

import numpy as np
import Image as im
import math

class GLCM:
    
    def __init__(self):
        self.img_gray     = 0
        self.arr_image    = 0
        self.contrast     = 0
        self.correlation  = 0
        self.energy       = 0
        self.entropy      = 0
        self.homogeneity  = 0
    
    
    def calculateContrast(self,ds_array):
        print ".|....calculating contrast"
        contrast = 0
        for i in range(ds_array.shape[0]):
            for j in range(ds_array.shape[1]):
                contrast = contrast + (ds_array[i][j] * math.pow((i-j),2))
        return contrast
    
    def calculateHomogeneity(self,ds_array):
        print ".|....calculating homogeneity"
        homogeneity = 0
        for i in range(ds_array.shape[0]):
            for j in range(ds_array.shape[1]):
                homogeneity = homogeneity + (ds_array[i][j] /(1+math.pow((i-j),2)))
        return homogeneity
    
    def calculateEnergy(self,ds_array):
        print ".|....calculating energy"
        asm = 0
        for i in range(ds_array.shape[0]):
            for j in range(ds_array.shape[1]):
                asm = asm + ds_array[i][j]
        return math.sqrt(asm)
    
    def calculateEntropy(self,ds_array):
        print ".|....calculating entropy"
        entropy = 0
        for i in range(ds_array.shape[0]):
            for j in range(ds_array.shape[1]):
                if ds_array[i][j] == 0:
                    val_tmp = 0
                else:
                    val_log = math.log(ds_array[i][j],10)
                    val_tmp = -val_log * ds_array[i][j]
                entropy = entropy + val_tmp
        return entropy
    
    def calculateCorrelation(self,ds_array):
        print ".|....calculating correlation"
        correlation = 0
        for i in range(ds_array.shape[0]):
            row = ds_array[i]
            mean_i = i * sum(row)
            vari_i = 0
            for r in row:
                vari_i = vari_i + math.pow((r-mean_i),2)
            for j in range(ds_array.shape[1]):
                col = ds_array.transpose()[j]
                mean_j = j * sum(col)
                vari_j = 0
                for c in col:
                    vari_j = vari_j + math.pow((c-mean_j),2)
                tmp_mean = (i-mean_i)*(j-mean_j)
                tmp_vari = math.sqrt(math.sqrt(vari_i)*math.sqrt(vari_j))
                if tmp_vari != 0:
                    correlation = correlation + (ds_array[i][j]*(tmp_mean/tmp_vari))
        return correlation
