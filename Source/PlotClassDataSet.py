#********************************************************************
#..University Federal of Sao Carlos
#..Author...........: PhD Student Gustavo Poli
#..Advisor..........: Prof. Dr. Jose Hiroki Saito
#..Colaboration.....: Prof. Dra. Maria do Carmos
#..First Version....: 2013.03.07 by GPoli
#..Last Version.....: 2013.03.13 by GPoli
#********************************************************************

import numpy as np
from matplotlib   import rc
from pylab        import *
from dbImages     import *


db_images       = dbImages()

lst_Acontrast,lst_Acorrelation,lst_Aenergy,lst_Aentropy,lst_Ahomogeneity = np.loadtxt("plot_class_A.txt",delimiter="\t", unpack=True)
lst_Bcontrast,lst_Bcorrelation,lst_Benergy,lst_Bentropy,lst_Bhomogeneity = np.loadtxt("plot_class_B.txt",delimiter="\t", unpack=True)
lst_Ccontrast,lst_Ccorrelation,lst_Cenergy,lst_Centropy,lst_Chomogeneity = np.loadtxt("plot_class_C.txt",delimiter="\t", unpack=True)
lst_Dcontrast,lst_Dcorrelation,lst_Denergy,lst_Dentropy,lst_Dhomogeneity = np.loadtxt("plot_class_D.txt",delimiter="\t", unpack=True)
lst_Econtrast,lst_Ecorrelation,lst_Eenergy,lst_Eentropy,lst_Ehomogeneity = np.loadtxt("plot_class_E.txt",delimiter="\t", unpack=True)
lst_Fcontrast,lst_Fcorrelation,lst_Fenergy,lst_Fentropy,lst_Fhomogeneity = np.loadtxt("plot_class_F.txt",delimiter="\t", unpack=True)

lst_wAcontrast,lst_wAcorrelation,lst_wAenergy,lst_wAentropy,lst_wAhomogeneity = np.loadtxt("plot_win_A.txt",delimiter="\t", unpack=True)
lst_wBcontrast,lst_wBcorrelation,lst_wBenergy,lst_wBentropy,lst_wBhomogeneity = np.loadtxt("plot_win_B.txt",delimiter="\t", unpack=True)
lst_wCcontrast,lst_wCcorrelation,lst_wCenergy,lst_wCentropy,lst_wChomogeneity = np.loadtxt("plot_win_C.txt",delimiter="\t", unpack=True)
lst_wDcontrast,lst_wDcorrelation,lst_wDenergy,lst_wDentropy,lst_wDhomogeneity = np.loadtxt("plot_win_D.txt",delimiter="\t", unpack=True)
lst_wEcontrast,lst_wEcorrelation,lst_wEenergy,lst_wEentropy,lst_wEhomogeneity = np.loadtxt("plot_win_E.txt",delimiter="\t", unpack=True)
lst_wFcontrast,lst_wFcorrelation,lst_wFenergy,lst_wFentropy,lst_wFhomogeneity = np.loadtxt("plot_win_F.txt",delimiter="\t", unpack=True)


lst_Nocontrast,lst_Nocorrelation,lst_Noenergy,lst_Noentropy,lst_Nohomogeneity = np.loadtxt("plot_win_no.txt",delimiter="\t", unpack=True)

rc('text', usetex=True)

title('Probe Functions: Contrast by Correlation')
ylabel('Contrast')
xlabel('Correlation')
plot(lst_Nocontrast,lst_Nocorrelation,marker='.', linestyle='  ', color='0.75')

plot(lst_Acontrast,lst_Acorrelation,marker='d', linestyle='  ', color='b')
plot(lst_Bcontrast,lst_Bcorrelation,marker='p', linestyle='  ', color='g')
plot(lst_Ccontrast,lst_Ccorrelation,marker='s', linestyle='  ', color='r')
plot(lst_Dcontrast,lst_Dcorrelation,marker='v', linestyle='  ', color='c')
plot(lst_Econtrast,lst_Ecorrelation,marker='o', linestyle='  ', color='m')
plot(lst_Fcontrast,lst_Fcorrelation,marker='D', linestyle='  ', color='y')

plot(lst_wAcontrast,lst_wAcorrelation,marker=7, linestyle='  ', color='b')
plot(lst_wBcontrast,lst_wBcorrelation,marker='*', linestyle='  ', color='g')
plot(lst_wCcontrast,lst_wCcorrelation,marker='*', linestyle='  ', color='r')
plot(lst_wDcontrast,lst_wDcorrelation,marker='*', linestyle='  ', color='c')
plot(lst_wEcontrast,lst_wEcorrelation,marker='*', linestyle='  ', color='m')
plot(lst_wFcontrast,lst_wFcorrelation,marker='*', linestyle='  ', color='y')


savefig(db_images.str_report_path+'Plot_Contrast_Correlation.png')

clf()

title('Probe Functions: Contrast by Energy')
ylabel('Contrast')
xlabel('Energy')
plot(lst_Nocontrast,lst_Noenergy,marker='.', linestyle='  ', color='0.75')

plot(lst_Acontrast,lst_Aenergy,marker='d', linestyle='  ', color='b')
plot(lst_Bcontrast,lst_Benergy,marker='p', linestyle='  ', color='g')
plot(lst_Ccontrast,lst_Cenergy,marker='s', linestyle='  ', color='r')
plot(lst_Dcontrast,lst_Denergy,marker='v', linestyle='  ', color='c')
plot(lst_Econtrast,lst_Eenergy,marker='o', linestyle='  ', color='m')
plot(lst_Fcontrast,lst_Fenergy,marker='D', linestyle='  ', color='y')

plot(lst_wAcontrast,lst_wAenergy,marker='*', linestyle='  ', color='b')
plot(lst_wBcontrast,lst_wBenergy,marker='*', linestyle='  ', color='g')
plot(lst_wCcontrast,lst_wCenergy,marker='*', linestyle='  ', color='r')
plot(lst_wDcontrast,lst_wDenergy,marker='*', linestyle='  ', color='c')
plot(lst_wEcontrast,lst_wEenergy,marker='*', linestyle='  ', color='m')
plot(lst_wFcontrast,lst_wFenergy,marker='*', linestyle='  ', color='y')


savefig(db_images.str_report_path+'Plot_Contrast_Energy.png')

clf()

title('Probe Functions: Contrast by Entropy')
ylabel('Contrast')
xlabel('Entropy')
plot(lst_Nocontrast,lst_Noentropy,marker='.', linestyle='  ', color='0.75')

plot(lst_Acontrast,lst_Aentropy,marker='d', linestyle='  ', color='b')
plot(lst_Bcontrast,lst_Bentropy,marker='p', linestyle='  ', color='g')
plot(lst_Ccontrast,lst_Centropy,marker='s', linestyle='  ', color='r')
plot(lst_Dcontrast,lst_Dentropy,marker='v', linestyle='  ', color='c')
plot(lst_Econtrast,lst_Eentropy,marker='o', linestyle='  ', color='m')
plot(lst_Fcontrast,lst_Fentropy,marker='D', linestyle='  ', color='y')

plot(lst_wAcontrast,lst_wAentropy,marker='*', linestyle='  ', color='b')
plot(lst_wBcontrast,lst_wBentropy,marker='*', linestyle='  ', color='g')
plot(lst_wCcontrast,lst_wCentropy,marker='*', linestyle='  ', color='r')
plot(lst_wDcontrast,lst_wDentropy,marker='*', linestyle='  ', color='c')
plot(lst_wEcontrast,lst_wEentropy,marker='*', linestyle='  ', color='m')
plot(lst_wFcontrast,lst_wFentropy,marker='*', linestyle='  ', color='y')


savefig(db_images.str_report_path+'Plot_Contrast_Entropy.png')

clf()

title('Probe Functions: Contrast by Homogeneity')
ylabel('Contrast')
xlabel('Homogeneity')
plot(lst_Nocontrast,lst_Nohomogeneity,marker='.', linestyle='  ', color='0.75')

plot(lst_Acontrast,lst_Ahomogeneity,marker='d', linestyle='  ', color='b')
plot(lst_Bcontrast,lst_Bhomogeneity,marker='p', linestyle='  ', color='g')
plot(lst_Ccontrast,lst_Chomogeneity,marker='s', linestyle='  ', color='r')
plot(lst_Dcontrast,lst_Dhomogeneity,marker='v', linestyle='  ', color='c')
plot(lst_Econtrast,lst_Ehomogeneity,marker='o', linestyle='  ', color='m')
plot(lst_Fcontrast,lst_Fhomogeneity,marker='D', linestyle='  ', color='y')

plot(lst_wAcontrast,lst_wAhomogeneity,marker='*', linestyle='  ', color='b')
plot(lst_wBcontrast,lst_wBhomogeneity,marker='*', linestyle='  ', color='g')
plot(lst_wCcontrast,lst_wChomogeneity,marker='*', linestyle='  ', color='r')
plot(lst_wDcontrast,lst_wDhomogeneity,marker='*', linestyle='  ', color='c')
plot(lst_wEcontrast,lst_wEhomogeneity,marker='*', linestyle='  ', color='m')
plot(lst_wFcontrast,lst_wFhomogeneity,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Contrast_Homogeneity.png')

clf()

title('Probe Functions: Correlation by Homogeneity')
ylabel('Correlation')
xlabel('Homogeneity')
plot(lst_Nocorrelation,lst_Nohomogeneity,marker='.', linestyle='  ', color='0.75')

plot(lst_Acorrelation,lst_Ahomogeneity,marker='d', linestyle='  ', color='b')
plot(lst_Bcorrelation,lst_Bhomogeneity,marker='p', linestyle='  ', color='g')
plot(lst_Ccorrelation,lst_Chomogeneity,marker='s', linestyle='  ', color='r')
plot(lst_Dcorrelation,lst_Dhomogeneity,marker='v', linestyle='  ', color='c')
plot(lst_Ecorrelation,lst_Ehomogeneity,marker='o', linestyle='  ', color='m')
plot(lst_Fcorrelation,lst_Fhomogeneity,marker='D', linestyle='  ', color='y')

plot(lst_wAcorrelation,lst_wAhomogeneity,marker='*', linestyle='  ', color='b')
plot(lst_wBcorrelation,lst_wBhomogeneity,marker='*', linestyle='  ', color='g')
plot(lst_wCcorrelation,lst_wChomogeneity,marker='*', linestyle='  ', color='r')
plot(lst_wDcorrelation,lst_wDhomogeneity,marker='*', linestyle='  ', color='c')
plot(lst_wEcorrelation,lst_wEhomogeneity,marker='*', linestyle='  ', color='m')
plot(lst_wFcorrelation,lst_wFhomogeneity,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Correlation_Homogeneity.png')

clf()


title('Probe Functions: Correlation by Energy')
ylabel('Correlation')
xlabel('Energy')
plot(lst_Nocorrelation,lst_Noenergy,marker='.', linestyle='  ', color='0.75')

plot(lst_Acorrelation,lst_Aenergy,marker='d', linestyle='  ', color='b')
plot(lst_Bcorrelation,lst_Benergy,marker='p', linestyle='  ', color='g')
plot(lst_Ccorrelation,lst_Cenergy,marker='s', linestyle='  ', color='r')
plot(lst_Dcorrelation,lst_Denergy,marker='v', linestyle='  ', color='c')
plot(lst_Ecorrelation,lst_Eenergy,marker='o', linestyle='  ', color='m')
plot(lst_Fcorrelation,lst_Fenergy,marker='D', linestyle='  ', color='y')

plot(lst_wAcorrelation,lst_wAenergy,marker='*', linestyle='  ', color='b')
plot(lst_wBcorrelation,lst_wBenergy,marker='*', linestyle='  ', color='g')
plot(lst_wCcorrelation,lst_wCenergy,marker='*', linestyle='  ', color='r')
plot(lst_wDcorrelation,lst_wDenergy,marker='*', linestyle='  ', color='c')
plot(lst_wEcorrelation,lst_wEenergy,marker='*', linestyle='  ', color='m')
plot(lst_wFcorrelation,lst_wFenergy,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Correlation_Energy.png')

clf()

title('Probe Functions: Correlation by Entropy')
ylabel('Correlation')
xlabel('Entropy')
plot(lst_Nocorrelation,lst_Noentropy,marker='.', linestyle='  ', color='0.75')

plot(lst_Acorrelation,lst_Aentropy,marker='d', linestyle='  ', color='b')
plot(lst_Bcorrelation,lst_Bentropy,marker='p', linestyle='  ', color='g')
plot(lst_Ccorrelation,lst_Centropy,marker='s', linestyle='  ', color='r')
plot(lst_Dcorrelation,lst_Dentropy,marker='v', linestyle='  ', color='c')
plot(lst_Ecorrelation,lst_Eentropy,marker='o', linestyle='  ', color='m')
plot(lst_Fcorrelation,lst_Fentropy,marker='D', linestyle='  ', color='y')

plot(lst_wAcorrelation,lst_wAentropy,marker='*', linestyle='  ', color='b')
plot(lst_wBcorrelation,lst_wBentropy,marker='*', linestyle='  ', color='g')
plot(lst_wCcorrelation,lst_wCentropy,marker='*', linestyle='  ', color='r')
plot(lst_wDcorrelation,lst_wDentropy,marker='*', linestyle='  ', color='c')
plot(lst_wEcorrelation,lst_wEentropy,marker='*', linestyle='  ', color='m')
plot(lst_wFcorrelation,lst_wFentropy,marker='*', linestyle='  ', color='y')


savefig(db_images.str_report_path+'Plot_Correlation_Entropy.png')

clf()

title('Probe Functions: Energy by Entropy')
ylabel('Energy')
xlabel('Entropy')
plot(lst_Noenergy,lst_Noentropy,marker='.', linestyle='  ', color='0.75')

plot(lst_Aenergy,lst_Aentropy,marker='d', linestyle='  ', color='b')
plot(lst_Benergy,lst_Bentropy,marker='p', linestyle='  ', color='g')
plot(lst_Cenergy,lst_Centropy,marker='s', linestyle='  ', color='r')
plot(lst_Denergy,lst_Dentropy,marker='v', linestyle='  ', color='c')
plot(lst_Eenergy,lst_Eentropy,marker='o', linestyle='  ', color='m')
plot(lst_Fenergy,lst_Fentropy,marker='D', linestyle='  ', color='y')

plot(lst_wAenergy,lst_wAentropy,marker='*', linestyle='  ', color='b')
plot(lst_wBenergy,lst_wBentropy,marker='*', linestyle='  ', color='g')
plot(lst_wCenergy,lst_wCentropy,marker='*', linestyle='  ', color='r')
plot(lst_wDenergy,lst_wDentropy,marker='*', linestyle='  ', color='c')
plot(lst_wEenergy,lst_wEentropy,marker='*', linestyle='  ', color='m')
plot(lst_wFenergy,lst_wFentropy,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Energy_Entropy.png')

clf()


title('Probe Functions: Energy by Homogeneity')
ylabel('Energy')
xlabel('Homogeneity')
plot(lst_Noenergy,lst_Nohomogeneity,marker='.', linestyle='  ', color='0.75')

plot(lst_Aenergy,lst_Ahomogeneity,marker='d', linestyle='  ', color='b')
plot(lst_Benergy,lst_Bhomogeneity,marker='p', linestyle='  ', color='g')
plot(lst_Cenergy,lst_Chomogeneity,marker='s', linestyle='  ', color='r')
plot(lst_Denergy,lst_Dhomogeneity,marker='v', linestyle='  ', color='c')
plot(lst_Eenergy,lst_Ehomogeneity,marker='o', linestyle='  ', color='m')
plot(lst_Fenergy,lst_Fhomogeneity,marker='D', linestyle='  ', color='y')

plot(lst_wAenergy,lst_wAhomogeneity,marker='*', linestyle='  ', color='b')
plot(lst_wBenergy,lst_wBhomogeneity,marker='*', linestyle='  ', color='g')
plot(lst_wCenergy,lst_wChomogeneity,marker='*', linestyle='  ', color='r')
plot(lst_wDenergy,lst_wDhomogeneity,marker='*', linestyle='  ', color='c')
plot(lst_wEenergy,lst_wEhomogeneity,marker='*', linestyle='  ', color='m')
plot(lst_wFenergy,lst_wFhomogeneity,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Energy_Homogeneity.png')

clf()


title('Probe Functions: Entropy by Homogeneity')
ylabel('Entropy')
xlabel('Homogeneity')
plot(lst_Noentropy,lst_Nohomogeneity,marker='.', linestyle='  ', color='0.75')

plot(lst_Aentropy,lst_Ahomogeneity,marker='d', linestyle='  ', color='b')
plot(lst_Bentropy,lst_Bhomogeneity,marker='p', linestyle='  ', color='g')
plot(lst_Centropy,lst_Chomogeneity,marker='s', linestyle='  ', color='r')
plot(lst_Dentropy,lst_Dhomogeneity,marker='v', linestyle='  ', color='c')
plot(lst_Eentropy,lst_Ehomogeneity,marker='o', linestyle='  ', color='m')
plot(lst_Fentropy,lst_Fhomogeneity,marker='D', linestyle='  ', color='y')

plot(lst_wAentropy,lst_wAhomogeneity,marker='*', linestyle='  ', color='b')
plot(lst_wBentropy,lst_wBhomogeneity,marker='*', linestyle='  ', color='g')
plot(lst_wCentropy,lst_wChomogeneity,marker='*', linestyle='  ', color='r')
plot(lst_wDentropy,lst_wDhomogeneity,marker='*', linestyle='  ', color='c')
plot(lst_wEentropy,lst_wEhomogeneity,marker='*', linestyle='  ', color='m')
plot(lst_wFentropy,lst_wFhomogeneity,marker='*', linestyle='  ', color='y')

savefig(db_images.str_report_path+'Plot_Entropy_Homogeneity.png')

clf()

print ".|end application"