#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.07 by GPoli
#..Last Version.....: 2013.03.13 by GPoli
#********************************************************************

import numpy as np

from pylab        import *
from dbImages     import *


db_images       = dbImages()

#file_in = np.loadtxt("input_plot.txt",skiprows=1)

lst_pcontrast     = []
lst_pcorrelation  = []
lst_penergy       = []
lst_pentropy      = []
lst_phomogeneity  = []

lst_wcontrast    = []
lst_wcorrelation = []
lst_wenergy      = []
lst_wentropy     = []
lst_whomogeneity = []

lst_ccontrast    = []
lst_ccorrelation = []
lst_cenergy      = []
lst_centropy     = []
lst_chomogeneity = []


for line in file_in:
   
    lst_wcontrast.append(line[0])
    lst_wcorrelation.append(line[1])
    lst_wenergy.append(line[2])
    lst_wentropy.append(line[3])
    lst_whomogeneity.append(line[4])

    lst_ccontrast.append(line[5])
    lst_ccorrelation.append(line[6])
    lst_cenergy.append(line[7])
    lst_centropy.append(line[8])
    lst_chomogeneity.append(line[9])

title('Probe Functions: Correlation by Contrast')
ylabel('Correlation')
xlabel('Contrast')
plot(lst_wcorrelation,lst_wcontrast,marker='*', linestyle='  ')
plot(lst_ccorrelation,lst_ccontrast,marker='+', linestyle='  ', color='r')
savefig(db_images.str_report_path+'Plot_Correlation_Contrast.png')

clf()

title('Probe Functions: Correlation by Energy')
ylabel('Correlation')
xlabel('Energy')
plot(lst_wcorrelation,lst_wenergy,marker='o', linestyle='  ')
plot(lst_wcorrelation,lst_wenergy,marker='+', linestyle='  ', color='r')
savefig(db_images.str_report_path+'Plot_Correlation_Energy.png')

clf()

title('Probe Functions: Correlation by Entropy')
ylabel('Correlation')
xlabel('Entropy')
plot(lst_wcorrelation,lst_wentropy,marker='o', linestyle='  ')
plot(lst_ccorrelation,lst_centropy,marker='+', linestyle='  ', color='r')
savefig(db_images.str_report_path+'Plot_Correlation_Entropy.png')

clf()

title('Probe Functions: Correlation by Homogeneity')
ylabel('Correlation')
xlabel('Homogeneity')
plot(lst_wcorrelation,lst_whomogeneity,marker='o', linestyle='  ')
plot(lst_ccorrelation,lst_chomogeneity,marker='+', linestyle='  ',color='r')
savefig(db_images.str_report_path+'Plot_Correlation_Homogeneity.png')

clf()

title('Probe Functions: Contrst by Energy')
ylabel('Contrast')
xlabel('Energy')
plot(lst_wcontrast,lst_wenergy,marker='o', linestyle='  ')
plot(lst_ccontrast,lst_cenergy,marker='+', linestyle='  ',color='r')
savefig(db_images.str_report_path+'Plot_Contrast_Energy.png')

clf()

title('Probe Functions: Contrst by Entropy')
ylabel('Contrast')
xlabel('Entropy')
plot(lst_wcontrast,lst_wentropy,marker='o', linestyle='  ')
plot(lst_ccontrast,lst_centropy,marker='+', linestyle='  ',color='r')
savefig(db_images.str_report_path+'Plot_Contrast_Entropy.png')

clf()

title('Probe Functions: Contrast by Homogeneity')
ylabel('Contrast')
xlabel('Homogeneity')
plot(lst_wcontrast,lst_whomogeneity,marker='o', linestyle='  ')
plot(lst_ccontrast,lst_chomogeneity,marker='+', linestyle='  ',color='r')
savefig(db_images.str_report_path+'Plot_Contrast_Homogeneity.png')

clf()

title('Probe Functions: Energy by Entropy')
ylabel('Energy')
xlabel('Entropy')
plot(lst_wenergy,lst_wentropy,marker='o', linestyle='  ')
plot(lst_cenergy,lst_centropy,marker='+', linestyle='  ',color='r')
savefig(db_images.str_report_path+'Plot_Energy_Entropy.png')

clf()

title('Probe Functions: Energy by Homogeneity')
ylabel('Energy')
xlabel('Homogeneity')
plot(lst_wenergy,lst_whomogeneity,marker='o', linestyle='  ')
plot(lst_cenergy,lst_chomogeneity,marker='+', linestyle='  ', color='r')
savefig(db_images.str_report_path+'Plot_Energy_Homogeneity.png')

clf()

title('Probe Functions: Entropy by Homogeneity')
ylabel('Entropy')
xlabel('Homogeneity')
plot(lst_wentropy,lst_whomogeneity,marker='o', linestyle='  ')
plot(lst_centropy,lst_chomogeneity,marker='+', linestyle='  ', color='r')
savefig(db_images.str_report_path+'Plot_Entropy_Homogeneity.png')

print ".|end application"