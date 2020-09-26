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

class Window(GLCM):
    def __init__(self,nro_line, nro_column, arr_window,probe_func_list):
        img_tools         = ImageTools()
        self.nro_line     = nro_line
        self.nro_column   = nro_column
        self.arr_image    = arr_window
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