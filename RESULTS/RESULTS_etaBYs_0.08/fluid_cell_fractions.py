from numpy import *
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

cols = [1, 2, 3, 11, 12]
vTcutoff = 0.3
taucutoff = 6.0
rTcutoff = 5.0

data=loadtxt(file1)[:,cols]
avgdata=loadtxt(file2)[:,cols]

vT = sqrt(data[:,3]**2+data[:,4]**2)
tau = data[:,0]
xT = data[:,1]
yT = data[:,2]
rT = sqrt(xT**2 + yT**2)
avT = arctanh(vT)
navT = ((avT-min(avT))/(max(avT)-min(avT)))

avgvT = sqrt(avgdata[:,3]**2+avgdata[:,4]**2)
avgtau = avgdata[:,0]
avgxT = avgdata[:,1]
avgyT = avgdata[:,2]
avgrT = sqrt(avgxT**2 + avgyT**2)
avgavT = arctanh(avgvT)
navgavT = ((avgavT-min(avgavT))/(max(avgavT)-min(avgavT)))

total_cells = len(tau)
total_low_pT_cells = len(tau[where(navT <= vTcutoff)])
total_early_low_pT_cells = len(tau[where(tau[where(navT <= vTcutoff)] < taucutoff)])
total_late_low_pT_cells = len(tau[where(tau[where(navT <= vTcutoff)] >= taucutoff)])
total_smallrT_low_pT_cells = len(rT[where(rT[where(navT <= vTcutoff)] < rTcutoff)])
total_bigrT_low_pT_cells = len(rT[where(rT[where(navT <= vTcutoff)] >= rTcutoff)])

avg_total_cells = len(avgtau)
avg_total_low_pT_cells = len(avgtau[where(navgavT <= vTcutoff)])
avg_total_early_low_pT_cells = len(avgtau[where(avgtau[where(navgavT <= vTcutoff)] < taucutoff)])
avg_total_late_low_pT_cells = len(avgtau[where(avgtau[where(navgavT <= vTcutoff)] >= taucutoff)])
avg_total_smallrT_low_pT_cells = len(avgrT[where(avgrT[where(navgavT <= vTcutoff)] < rTcutoff)])
avg_total_bigrT_low_pT_cells = len(avgrT[where(avgrT[where(navgavT <= vTcutoff)] >= rTcutoff)])

#print total_low_pT_cells
print '% of low-pT fluid cells =', (100.*total_low_pT_cells)/total_cells
print '% of early low-pT fluid cells =', (100.*total_early_low_pT_cells)/total_low_pT_cells
print '% of late low-pT fluid cells =', (100.*total_late_low_pT_cells)/total_low_pT_cells
print 'mean(rT) =', mean(rT), ', var(rT) =', var(rT)

print

#print avg_total_low_pT_cells
print '% of low-pT avg. fluid cells =', (100.*avg_total_low_pT_cells)/avg_total_cells
print '% of early low-pT avg. fluid cells =', (100.*avg_total_early_low_pT_cells)/avg_total_low_pT_cells
print '% of late low-pT avg. fluid cells =', (100.*avg_total_late_low_pT_cells)/avg_total_low_pT_cells
print 'mean(avgrT) =', mean(avgrT), ', var(avgrT) =', var(avgrT)

# End of file
