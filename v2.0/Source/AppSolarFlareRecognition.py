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
L2              = 0.14 #...distance L2
L2_learning     = 0.07 #...distance L2 used by learning phase
theshold        = 0    #...thashold by the read color (on the grayscale image)
size            = (50,50)
#...chosse what of the probe functions will be used by on the process
#..[Contrast,Correlation,Energy,Entropy,Homogeneity]
probe_func_list = [True,True,True,True,True]            #..All (Contrast, Correlation, Energy, Entropy, Homogeneity)
#probe_func_list = [True,False,False,False,False]       #..(Contrast)
#probe_func_list = [True,True,False,False,False]        #..(Contrast,Correlation)
#probe_func_list = [True,True,True,True,False]          #..(Contrast,Correlation, Energy,Entropy)
#probe_func_list = [True,True,True,False,True]          #..(Contrast,Correlation, Energy,Homogeneity)
#probe_func_list = [False,True,False,False,False]       #..(Correlation)
#probe_func_list = [False,True,True,False,False]        #..(Correlation,Energy)
#probe_func_list = [False,True,False,False,True]        #..(Correlation,Homogeneity)
#probe_func_list = [False,True,True,True,False]         #..(Correlation,Energy,Entropy)
#probe_func_list = [False,True,True,True,True]          #..(Correlation,Energy,Entropy,Homogeneity)
#probe_func_list = [False,True,False,True,False]        #..(Correlation,Entropy)
#probe_func_list = [False,True,False,True,False]        #..(Correlation,Entropy,Homogeneity)
#probe_func_list = [True,True,False,True,False]         #..(Contrast,Correlation,Entropy)
#probe_func_list = [True,True,False,True,True]          #..(Contrast,Correlation,Entropy,Homogeneity)
#probe_func_list = [True,False,True,Fale,False]         #..(Contrast,Energy)
#probe_func_list = [True,False,True,True,True]          #..(Contrast,Energy,Entropy,Homogeneity)
#probe_func_list = [True,False,False,True,False]        #..(Contrast,Entropy)
#probe_func_list = [True,False,False,False,True]        #..(Contrast,Homogeneity)
#probe_func_list = [False,False,True,False,False]       #..(Energy)
#probe_func_list = [False,False,True,True,False]        #..(Energy,Entropy)
#probe_func_list = [False,False,True,False,True]        #..(Energy,Homogeneity)
#probe_func_list = [False,False,False,True,False]       #..(Entropy)
#probe_func_list = [False,False,False,True,True]        #..(Entropy,Homogeneity)
#probe_func_list = [False,False,False,False,True]       #..(Homogeneity)

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
    if probe_func_list[0]:
        if pattern.contrast > max_contrast:
            max_contrast = pattern.contrast
    if probe_func_list[1]:
        if pattern.correlation > max_correlation:
            max_correlation = pattern.correlation
    if probe_func_list[2]:
        if pattern.energy > max_energy:
            max_energy = pattern.energy
    if probe_func_list[3]:
        if pattern.entropy < min_entropy:
            min_entropy = pattern.entropy
    if probe_func_list[4]:
        if pattern.homogeneity > max_homogeneity:
            max_homogeneity = pattern.homogeneity

    lst_patterns.append(pattern)

#...load and process the solar disk images
#...for each solar disk image is segmentaed on windows for the processing
for image in db_images.lst_img_solar_disk:
    solar_disk = SolarDisk(im.open(db_images.str_img_test_path+image), image[:-4], theshold, size,probe_func_list)
    solar_disk.img_gray.save(db_images.str_report_path+image[:-4]+"_gray.jpg")
    lst_solar_disk.append(solar_disk)
#..check the max values to calculate the normalization
for solar_disk in lst_solar_disk:
    for window in solar_disk.lst_windows:
        
        if probe_func_list[0]:
            if window.contrast > max_contrast:
                max_contrast = window.contrast
        if probe_func_list[1]:
            if window.correlation > max_correlation:
                max_correlation = window.correlation
        if probe_func_list[2]:
            if window.energy > max_energy:
                max_energy = window.energy
        if probe_func_list[3]:
            if window.entropy < min_entropy:
                min_entropy = window.entropy
        if probe_func_list[4]:
            if window.homogeneity > max_homogeneity:
                max_homogeneity = window.homogeneity

#...open file will be save the max values used by the normalization process
file_name = "GLCM_Max_Values_"
if probe_func_list[0]:
    file_name = file_name+"Con"
if probe_func_list[1]:
    file_name = file_name + "Cor"
if probe_func_list[2]:
    file_name = file_name + "Ene"
if probe_func_list[3]:
    file_name = file_name + "Ent"
if probe_func_list[4]:
    file_name = file_name + "Hom"
file_name = file_name + ".txt"
file_out = open(db_images.str_report_path+file_name,"w")
str_line = ""
if probe_func_list[0]:
    print ".|.max_contrast......: " + str(max_contrast)
    str_line = str_line + "contrast \t"+str(max_contrast)+"\n"
if probe_func_list[1]:
    print ".|.max_correlation...: " + str(max_correlation)
    str_line = str_line + "correlation \t"+str(max_correlation)+"\n"
if probe_func_list[2]:    
    print ".|.max_energy........: " + str(max_energy)
    str_line = str_line + "energy \t"+str(max_energy)+"\n"
if probe_func_list[3]:    
    print ".|.min_entropy.......: " + str(min_entropy)
    str_line = str_line + "entropy \t"+str(min_entropy)+"\n"
if probe_func_list[4]:
    print ".|.max_homogeneity...: " + str(max_homogeneity)
    str_line = str_line+ "homogeneity \t"+str(max_homogeneity)+"\n"
           
file_out.write(str_line)
file_out.close()

#...open file where the GLCM Patterns data will be saved
file_name = "GLCM_Patterns_Values_"
if probe_func_list[0]:
    file_name = file_name+"Con"
if probe_func_list[1]:
    file_name = file_name + "Cor"
if probe_func_list[2]:
    file_name = file_name + "Ene"
if probe_func_list[3]:
    file_name = file_name + "Ent"
if probe_func_list[4]:
    file_name = file_name + "Hom"
file_name = file_name + ".txt"
file_out = open(db_images.str_report_path+file_name,"w")
file_01  = open("plot_pattern.txt","w")
str_line = "Pattner Name \t"
if probe_func_list[0]:
    str_line = str_line + "Contrast \t \t"
if probe_func_list[1]:
    str_line = str_line  + "Correlation \t \t"
if probe_func_list[2]:
    str_line = str_line + "Energy \t \t"
if probe_func_list[3]:
    str_line = str_line + "Entropy \t \t"
if probe_func_list[4]:
    str_line = str_line  + "Homogeneity"
str_line = str_line     + "\n"
file_out.write(str_line)
str_line = " \t"
if probe_func_list[0]:
    str_line = str_line + "Current \t Normalized \t"
if probe_func_list[1]:
    str_line = str_line  + "Current \t Normalized \t"
if probe_func_list[2]:
    str_line = str_line + "Current \t Normalized \t"
if probe_func_list[3]:
    str_line = str_line + "Current \t Normalized \t"
if probe_func_list[4]:
    str_line = str_line  + "Current \t Normalized \t"
str_line = str_line     + "\n"
file_out.write(str_line)

for pattern in lst_patterns:
    str_line  = pattern.pattern_name 
    str_line2 = ""
    if probe_func_list[0]:
        str_line  = str_line  +"\t"+str(pattern.contrast)+"\t"+str(pattern.contrast/max_contrast)
        str_line2 = str_line2 +"\t"+str(pattern.contrast/max_contrast)
    if probe_func_list[1]:
        str_line  = str_line  +"\t"+str(pattern.correlation)+"\t"+str(pattern.correlation/max_correlation)
        str_line2 = str_line2 +"\t"+str(pattern.correlation/max_correlation)
    if probe_func_list[2]:
        str_line  = str_line  +"\t"+str(pattern.energy)+"\t"+str(pattern.energy/max_energy)
        str_line2 = str_line2 +"\t"+str(pattern.energy/max_energy)
    if probe_func_list[3]:
        str_line  = str_line  +"\t"+str(pattern.entropy)+"\t"+str(pattern.entropy/min_entropy)
        str_line2 = str_line2 +"\t"+str(pattern.entropy/min_entropy)
    if probe_func_list[4]:
        str_line  = str_line  +"\t"+str(pattern.homogeneity)+"\t"+str(pattern.homogeneity/max_homogeneity)
        str_line2 = str_line2 +"\t"+str(pattern.homogeneity/max_homogeneity)
    str_line  = str_line  + "\n"
    str_line2 = str_line2 + "\n"
    file_out.write(str_line)
    file_01.write(str_line2)
file_out.close()
file_01.close()

#...process the GLCM data patterns to compose the classes
print ".|.compute distance between pattern classes"
file_name = "NearSet_L2_Patterns_"
if probe_func_list[0]:
    file_name = file_name+"Con"
if probe_func_list[1]:
    file_name = file_name + "Cor"
if probe_func_list[2]:
    file_name = file_name + "Ene"
if probe_func_list[3]:
    file_name = file_name + "Ent"
if probe_func_list[4]:
    file_name = file_name + "Hom"
file_name = file_name + ".txt"
file_out = open(db_images.str_report_path+file_name,"w")

str_line = "Pattern Base \t Pattern Reference \t "
if probe_func_list[0]:
    str_line = str_line + "Contrast \t "
if probe_func_list[1]:
    str_line = str_line + "Correlation \t"
if probe_func_list[2]:
    str_line = str_line + "Energy \t"
if probe_func_list[3]:
    str_line = str_line + "Entropy \t"
if probe_func_list[4]:
    str_line = str_line + "Homogeneity \t"
str_line = str_line + "SUM \t SQRT(SUM):L2\n"
file_out.write(str_line)

class_name  = 65
class_index = 0
for pat_base in lst_patterns:
    lst_tmp_patterns = []
    lst_tmp_distance = []
    
    if probe_func_list[0]:
        bas_contrast    = pat_base.contrast/max_contrast
    if probe_func_list[1]:
        bas_correlation = pat_base.correlation/max_correlation
    if probe_func_list[2]:
        bas_energy      = pat_base.energy/max_energy
    if probe_func_list[3]:
        bas_entropy     = pat_base.entropy/min_entropy
    if probe_func_list[4]:
        bas_homogeneity = pat_base.homogeneity/max_homogeneity
    
    
    for pat_reference in lst_patterns:
        val_sum         = 0
        str_line        = pat_base.pattern_name+"\t"+pat_reference.pattern_name       
        if probe_func_list[0]:
            ref_contrast    = pat_reference.contrast/max_contrast
            contrast        = math.pow((bas_contrast-ref_contrast),2)
            val_sum         = val_sum + contrast
            str_line        = str_line +"\t" + str(contrast)
        if probe_func_list[1]:
            ref_correlation = pat_reference.correlation/max_correlation
            correlation     = math.pow((bas_correlation-ref_correlation),2)
            val_sum         = val_sum + correlation
            str_line        = str_line +"\t" + str(correlation)
        if probe_func_list[2]:
            ref_energy      = pat_reference.energy/max_energy
            energy          = math.pow((bas_energy-ref_energy),2)
            val_sum         = val_sum + energy
            str_line        = str_line +"\t" + str(energy)
        if probe_func_list[3]:
            ref_entropy     = pat_reference.entropy/min_entropy
            entropy         = math.pow((bas_entropy-ref_entropy),2)
            val_sum         = val_sum + entropy
            str_line        = str_line +"\t" + str(entropy)
        if probe_func_list[4]:
            ref_homogeneity = pat_reference.homogeneity/max_homogeneity
            homogeneity     = math.pow((bas_homogeneity-ref_homogeneity),2)
            val_sum         = val_sum + homogeneity
            str_line        = str_line +"\t" + str(homogeneity)
        str_line        = str_line +"\t" + str(val_sum)
        distance        = math.sqrt(val_sum)
        str_line        = str_line +"\t" + str(distance) + "\n"
        file_out.write(str_line)
        
        if distance <= L2_learning and distance > 0:
            lst_tmp_distance.append(distance)
            lst_tmp_patterns.append(pat_reference)
    pat_base.setLstNearPatterns(lst_tmp_patterns)  
    pat_base.lst_L2 = lst_tmp_distance
    
    pat_base.class_name = chr(class_name)
    pat_base.class_index = class_index
    class_name = class_name + 1
    class_inex = class_index + 1

file_out.close()


#...load the distance between the patterns and mount the classes group


print str(len(lst_classes))
file_name = "GLCM_Class_Average_"
if probe_func_list[0]:
    file_name = file_name+"Con"
if probe_func_list[1]:
    file_name = file_name + "Cor"
if probe_func_list[2]:
    file_name = file_name + "Ene"
if probe_func_list[3]:
    file_name = file_name + "Ent"
if probe_func_list[4]:
    file_name = file_name + "Hom"
file_name = file_name + ".txt"
file_out = open(db_images.str_report_path+file_name,"w")
str_line = "Class Name \t Pattern Reference \t Patterns <= L2"
if probe_func_list[0]:
    str_line = str_line + " \t Contrast Average"
if probe_func_list[1]:
    str_line = str_line + " \t Correlation Average"
if probe_func_list[2]:
    str_line = str_line + " \t Energy Average"
if probe_func_list[3]:
    str_line = str_line + " \t Entropy Average"
if probe_func_list[4]:
    str_line = str_line + " \t Homogeneity Averiage"
str_line = str_line + "\n"
for item in lst_patterns:
    str_line = str(item.class_name) + "\t" 
    str_line = str_line + item.pattern_name + "\t"
    if len(item.lst_near_patterns) > 0:
        str_line = str_line 
        for pat in item.lst_near_patterns:
            str_line = str_line + pat.pattern_name +", "
        str_line = str_line 
    else:
        str_line = str_line + "[ - ]"
    if probe_func_list[0]:
        str_line = str_line + "\t" + str(item.ave_contrast)
    if probe_func_list[1]:
        str_line = str_line +"\t"+str(item.ave_correlation)
    if probe_func_list[2]:
        str_line = str_line+"\t"+str(item.ave_energy)
    if probe_func_list[3]:
        str_line = str_line+"\t"+str(item.ave_entropy)
    if probe_func_list[4]:
        str_line = str_line+"\t"+str(item.ave_homogeneity)
    str_line = str_line + "\n"
    file_out.write(str_line)
file_out.close()


#......I am working in the treining/leaning phase
#quit() #...exit the application
print ".|leaning phase is completed!"
#------------------------------------------------


#...solar flare recognition
file_name = "GLCM_SolarFlareRecognition_"
if probe_func_list[0]:
    file_name = file_name+"Con"
if probe_func_list[1]:
    file_name = file_name + "Cor"
if probe_func_list[2]:
    file_name = file_name + "Ene"
if probe_func_list[3]:
    file_name = file_name + "Ent"
if probe_func_list[4]:
    file_name = file_name + "Hom"
file_name = file_name + ".txt"
file_out = open(db_images.str_report_path+file_name,"w")
file_02  = open("plot_win_ok.txt","w'")
file_03  = open("plot_win_no.txt","w")

str_line = "Solar Disk \t Lin \t Col "
if probe_func_list[0]:
    str_line = str_line + "\t Contrast"
if probe_func_list[1]:
    str_line = str_line + "\t Correlation "
if probe_func_list[2]:
    str_line = str_line + "\t Energy"
if probe_func_list[3]:
    str_line = str_line + "\t Entropy"
if probe_func_list[4]:
    str_line = str_line + "\t Homogeneity"
str_line = str_line + "\t Class Name "
if probe_func_list[0]:
    str_line = str_line + "\t Contrast"
if probe_func_list[1]:
    str_line = str_line + "\t Correlation "
if probe_func_list[2]:
    str_line = str_line + "\t Energy"
if probe_func_list[3]:
    str_line = str_line + "\t Entropy"
if probe_func_list[4]:
    str_line = str_line + "\t Homogeneity"
str_line = str_line + " \t SUN \t Distance (L2) \n"
file_out.write(str_line)
count = 0
for solar_disk in lst_solar_disk:
    for window in solar_disk.lst_windows:
        if probe_func_list[0]:
            win_contrast    = window.contrast/max_contrast
        if probe_func_list[1]:
            win_correlation = window.correlation/max_correlation
        if probe_func_list[2]:
            win_energy      = window.energy/max_energy
        if probe_func_list[3]:
            win_entropy     = window.entropy/min_entropy
        if probe_func_list[4]:
            win_homogeneity = window.homogeneity/max_homogeneity
        
        count_count = True
        
        for pattern in lst_patterns:
            
            val_sum = 0
            if probe_func_list[0]:
                contrast    = (pattern.ave_contrast/max_contrast)-win_contrast
                val_sum     = val_sum + math.pow(contrast,2)
            if probe_func_list[1]:
                correlation = (pattern.ave_correlation/max_correlation)-win_correlation
                val_sum     = val_sum + math.pow(correlation,2)
            if probe_func_list[2]:
                energy      = (pattern.ave_energy/max_energy)-win_energy
                val_sum     = val_sum + math.pow(energy,2)
            if probe_func_list[3]:
                entropy     = (pattern.ave_entropy/min_entropy)-win_entropy
                val_sum     = val_sum + math.pow(entropy,2)
            if probe_func_list[4]:
                homogeneity = (pattern.ave_homogeneity/max_homogeneity)-win_homogeneity
                val_sum     = val_sum + math.pow(homogeneity,2)
            
            distance    = math.sqrt(val_sum)
            str_line = solar_disk.pattern_name +"\t"+ str(window.nro_line)+"\t"+str(window.nro_column)
            str_line2 = ""
           
            if probe_func_list[0]:
                str_line = str_line + "\t"+str(win_contrast)
                str_line2 = str_line2 + "\t"+str(win_contrast)
             
            if probe_func_list[1]:
                str_line = str_line +"\t"+str(win_correlation)
                str_line2 = str_line2 +"\t"+str(win_correlation)
                
            if probe_func_list[2]:
                str_line = str_line +"\t"+str(win_energy)
                str_line2 = str_line2 +"\t"+str(win_energy)
             
            if probe_func_list[3]:
                str_line = str_line +"\t"+str(win_entropy)
                str_line2 = str_line2 +"\t"+str(win_entropy)
               
            if probe_func_list[4]:
                str_line = str_line +"\t"+str(win_homogeneity)
                str_line2 = str_line2 +"\t"+str(win_homogeneity)
                
            str_line = str_line +"\t"+str(pattern.class_name)
            if probe_func_list[0]:
                str_line = str_line +"\t"+str((pattern.ave_contrast/max_contrast))
            if probe_func_list[1]:
                str_line = str_line +"\t"+str((pattern.ave_correlation/max_correlation))
            if probe_func_list[2]:
                str_line = str_line +"\t"+str((pattern.ave_energy/max_energy))
            if probe_func_list[3]:
                str_line = str_line +"\t"+str((pattern.ave_entropy/min_entropy))
            if probe_func_list[4]:
                str_line = str_line +"\t"+str((pattern.ave_homogeneity/max_homogeneity))
            str_line = str_line +"\t"+str(val_sum)+"\t"+str(distance)+"\n"
            str_line2 = str_line2 + "\n"
            
            print ".|... "+ str(distance)
            
            #win_name = db_images.str_report_path+solar_disk.pattern_name+"_win_"+str(window.nro_line)+"_"+str(window.nro_column)+\
            #           "_"+str(pattern.class_name)+"_("+str(distance)+").jpg"
            #image_tools.arr2img(window.arr_image).save(win_name)
            if distance <= L2:
                if count_count:
                    count = count + 1
                    count_count = False
                file_out.write(str_line)
                file_02.write(str_line2)
            else:
                file_03.write(str_line2)
            
file_out.close()
file_02.close()
file_03.close()
print ".|...>>>> "+str(count) +" <<<<"
print ".|end application..."
