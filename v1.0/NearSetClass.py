#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.07 by GPoli
#..Last Version.....: 2013.03.07 by GPoli
#********************************************************************

import numpy as np
import Image as im
import math

class NearSetClass:
    
    def __init__(self,class_name,lst_patterns,probe_func_list):
        self.class_name   = class_name
        self.lst_patterns = lst_patterns
        if probe_func_list[0]:
            self.contrast     = self.calculateContrast(self.lst_patterns)
        if probe_func_list[1]:
            self.correlation  = self.calculateCorrelation(self.lst_patterns)
        if probe_func_list[2]:
            self.energy       = self.calculateEnergy(self.lst_patterns)
        if probe_func_list[3]:
            self.entropy      = self.calculateEntropy(self.lst_patterns)
        if probe_func_list[4]:
            self.homogeneity  = self.calculateHomogeneity(self.lst_patterns)

    def calculateContrast(self, lst_patterns):
        val = 0
        for pattern in lst_patterns:
            val = val + pattern.contrast
        return val/len(lst_patterns)

    def calculateCorrelation(self, lst_patterns):
        val = 0
        for pattern in lst_patterns:
            val = val + pattern.correlation
        return val/len(lst_patterns)

    def calculateEnergy(self, lst_patterns):
        val = 0
        for pattern in lst_patterns:
            val = val + pattern.energy
        return val/len(lst_patterns)

    def calculateEntropy(self, lst_patterns):
        val = 0
        for pattern in lst_patterns:
            val = val + pattern.entropy
        return val/len(lst_patterns)

    def calculateHomogeneity(self, lst_patterns):
        val = 0
        for pattern in lst_patterns:
            val = val + pattern.homogeneity
        return val/len(lst_patterns)
