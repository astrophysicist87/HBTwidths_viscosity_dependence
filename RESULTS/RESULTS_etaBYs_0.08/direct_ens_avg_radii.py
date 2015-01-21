from math import *
import sys
from numpy import *

dirvec = [2, 3, 4]
nevs = 1000
f1 = (nevs - 1.) / (nevs**2)
f2 = 2. / (nevs**2)

for direc in dirvec:
    meandata = zeros([21,14])
    vardata = zeros([21,14])
    runsumdata = zeros([21,14])
    sum2data = zeros([21,14])
    for event in xrange(1,nevs+1):
        infile = 'NEW_TDEP_V%(direcstring)d/NEW_TDEP_V%(direcstring)d_results-%(event)d/HBTradii_cfs_ev%(event)d.dat_cfs_0' % {"event": event, "direcstring": direc}
        newdata = delete(loadtxt(infile),0,1)
        meandata += newdata
        vardata -= newdata * runsumdata
        runsumdata += newdata
        sum2data += newdata**2
    
    meandata /= nevs
    vardata *= f2
    vardata += f1 * sum2data
    outfile = 'NEW_TDEP_V%(direcstring)d/HBTradii_direct_ens_avg_direc_%(direcstring)d_cfs_0_%(nevs)devs.dat' % {"direcstring": direc, "nevs": nevs}
    outfile2 = 'NEW_TDEP_V%(direcstring)d/HBTradii_direct_variance_direc_%(direcstring)d_cfs_0_%(nevs)devs.dat' % {"direcstring": direc, "nevs": nevs}
    savetxt(outfile, meandata)
    savetxt(outfile2, vardata)
    print 'Finished direc =', direc

print 'Finished all.'
