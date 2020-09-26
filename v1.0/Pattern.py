#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.02.28 by GPoli
#..Last Version.....: 2013.03.12 by GPoli
#********************************************************************

import numpy as np
import Image as im
import math

from ImageTools import *
from GLCM       import *

class Pattern(GLCM):
    def __init__(self, img_rgb, pattern_name, threshold, probe_func_list):
        img_tools              = ImageTools()
        
        self.img_rgb           = img_rgb
        self.threshold         = threshold
        self.img_gray          = img_tools.rgb2gray(self.img_rgb,self.threshold)
        self.pattern_name      = pattern_name
        self.arr_image         = img_tools.img2arr(self.img_gray)
        
        self.probe_func_list   = probe_func_list
        
        self.lst_near_patterns = []
        self.ave_contrast      = 0
        self.ave_correlation   = 0
        self.ave_energy        = 0
        self.ave_entropy       = 0
        self.ave_homogeneity   = 0
        self.l2                = 0
        self.class_name        = 0

        if probe_func_list[0]:
            self.contrast     = self.calculateContrast(self.arr_image)
        if probe_func_list[1]:
            self.correlation  = self.calculateCorrelation(self.arr_image)
        if probe_func_list[2]:
            self.energy       = self.calculateEnergy(self.arr_image)
        if probe_func_list[3]:
            self.entropy      = self.calculateEntropy(self.arr_image)
        if probe_func_list[4]:
            self.homogeneity  = self.calculateHomogeneity(self.arr_image)
            
    def setLstNearPatterns(self,lst_near_patterns):
        self.lst_near_patterns = lst_near_patterns
        if self.probe_func_list[0] and len(self.lst_near_patterns) > 0:
            self.ave_contrast = self.averageContrast()
        if self.probe_func_list[0] and len(self.lst_near_patterns) == 0:
            self.ave_contrast = self.contrast
            
        if self.probe_func_list[1] and len(self.lst_near_patterns) > 0:
            self.ave_correlation = self.averageCorrelation()
        if self.probe_func_list[1] and len(self.lst_near_patterns) == 0:
            self.ave_correlation = self.correlation
            
        if self.probe_func_list[2] and len(self.lst_near_patterns) > 0:
            self.ave_energy = self.averageEnergy()
        if self.probe_func_list[2] and len(self.lst_near_patterns) == 0:
            self.ave_energy = self.energy
            
        if self.probe_func_list[3] and len(self.lst_near_patterns) > 0:
            self.ave_entropy = self.averageEntropy()
        if self.probe_func_list[3] and len(self.lst_near_patterns) == 0:
            self.ave_entropy = self.entropy
            
        if self.probe_func_list[4] and len(self.lst_near_patterns) > 0:
            self.ave_homogeneity = self.averageHomogeneity()
        if self.probe_func_list[4] and len(self.lst_near_patterns) == 0:
            self.ave_homogeneity = self.homogeneity
        
    def averageContrast(self):
        tmp_val = 0
        for pattern in self.lst_near_patterns:
            tmp_val = tmp_val + pattern.contrast
        return tmp_val/len(self.lst_near_patterns)
        
    def averageCorrelation(self):
        tmp_val = 0
        for pattern in self.lst_near_patterns:
            tmp_val = tmp_val + pattern.correlation
        return tmp_val/len(self.lst_near_patterns)
        
    def averageEnergy(self):
        tmp_val = 0
        for pattern in self.lst_near_patterns:
            tmp_val = tmp_val + pattern.energy
        return tmp_val/len(self.lst_near_patterns)
        
    def averageEntropy(self):
        tmp_val = 0
        for pattern in self.lst_near_patterns:
            tmp_val = tmp_val + pattern.entropy
        return tmp_val/len(self.lst_near_patterns)
        
    def averageHomogeneity(self):
        tmp_val = 0
        for pattern in self.lst_near_patterns:
            tmp_val = tmp_val + pattern.homogeneity
        return tmp_val/len(self.lst_near_patterns)

