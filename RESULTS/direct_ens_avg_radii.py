from math import *
import sys
from numpy import *

#ebsvec = ['0.00','0.05','0.08','0.10','0.15','0.20']
ebsvec = ['0.08']
nevs = 10
f1 = (nevs - 1.) / (nevs**2)
f2 = 2. / (nevs**2)
initev = 11		#initial event to start with...

for ebs in ebsvec:
    meandata = zeros([21,14])
    vardata = zeros([21,14])
    runsumdata = zeros([21,14])
    sum2data = zeros([21,14])
    for event in xrange(initev,nevs+initev):
        infile = 'RESULTS_etaBYs_%(ebsstring)s/results-%(event)d/HBTradii_cfs_ev%(event)d.dat_cfs_0' % {"event": event, "ebsstring": ebs}
        newdata = delete(loadtxt(infile),0,1)
        meandata += newdata
        vardata -= newdata * runsumdata
        runsumdata += newdata
        sum2data += newdata**2
    
    meandata /= nevs
    vardata *= f2
    vardata += f1 * sum2data
    outfile = 'RESULTS_etaBYs_%(ebsstring)s/HBTradii_direct_ens_avg_ebs_%(ebsstring)s_cfs_0_%(nevs)devs.dat_initev_%(inev)d' % {"ebsstring": ebs, "nevs": nevs, "inev": initev}
    outfile2 = 'RESULTS_etaBYs_%(ebsstring)s/HBTradii_direct_variance_ebs_%(ebsstring)s_cfs_0_%(nevs)devs.dat' % {"ebsstring": ebs, "nevs": nevs, "inev": initev}
    savetxt(outfile, meandata)
    savetxt(outfile2, vardata)
    print 'Finished eta/s =', ebs

print 'Finished all.'
