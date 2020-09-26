#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.04 by GPoli
#..Last Version.....: 2013.03.12 by GPoli
#********************************************************************


import Image as im
import math

from dbImages     import *
from Pattern      import *
from ImageTools   import *
from SolarDisk    import *

#..Parameters
L2              = 0.19 #...distance L2
L2_learning     = 0.1 #...distance L2 used by learning phase
theshold        = 0    #...thashold by the read color (on the grayscale image)
size            = (50,50)
probe_func_list = [True,True,True,True,True]            #..All (Contrast,
lst_patterns    = []   #...patterns object list
lst_classes     = []   #...solar flare classes
lst_solar_disk  = []   #...solar disk images for test

image_tools     = ImageTools()
db_images       = dbImages()

if probe_func_list[0]:
    max_contrast    = 0
if probe_func_list[1]:
    max_correlation = 0
if probe_func_list[2]:
    max_energy      = 0
if probe_func_list[3]:
    min_entropy     = 0
if probe_func_list[4]:    
    max_homogeneity = 0

print ".|begin application..."


#...load and process the patterns images
for image in db_images.lst_img_patterns:
    pattern     = Pattern(im.open(db_images.str_img_patters_path+image), image[:-4],theshold,probe_func_list)
    pattern.img_gray.save(pattern.pattern_name+"_gray.jpg")

print ".|end application..."
