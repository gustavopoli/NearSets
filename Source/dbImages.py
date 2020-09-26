#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.04 by GPoli
#..Last Version.....: 2013.03.11 by GPoli
#********************************************************************

import os

class dbImages:

    def __init__(self):
        self.str_img_patters_path   = '../Input/patterns/'
        self.str_img_test_path      = '../Input/test/'
        self.str_report_path        = '../Output/'
        self.str_patter_prefix      = 'pat'
        self.str_sodisk_prefix      = 'ifa'
        self.lst_img_patterns       = self.load_img_patterns()
        self.lst_img_solar_disk     = self.load_img_solar_disk()

    def load_img_patterns(self):
        lst_img_patterns = []
        print ".|.load pattern files: solar flares"
        for r,d,f in os.walk(self.str_img_patters_path):
            for file in f:
                if file.endswith(".jpg"):
                    if file[:3] == self.str_patter_prefix:
                        print ".|..add pattern " + file
                        lst_img_patterns.append(file)
        return lst_img_patterns

    
    def load_img_solar_disk(self):
        lst_img_solar_disk = []
        print ".|.load solar disk files: solar flares"
        for r,d,f in os.walk(self.str_img_test_path):
            for file in f:
                if file.endswith(".jpg"):
                    if file[:3] == self.str_sodisk_prefix:
                        print ".|..add solar disk " + file
                        lst_img_solar_disk.append(file)
        return lst_img_solar_disk