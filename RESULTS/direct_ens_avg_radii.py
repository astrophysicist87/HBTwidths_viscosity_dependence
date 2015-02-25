from math import *
import sys
from numpy import *

#df_stem = ''
df_stem = '_no_df'
#neq_stem = ''
neq_stem = '_neq0'
#ebsvec = ['0.00','0.05','0.08','0.10','0.15','0.20']
#TVidx = int(sys.argv[1])
ebsvec = ['0.00']
nevs = 250
f1 = (nevs - 1.) / (nevs**2)
f2 = 2. / (nevs**2)
initev = 1		#initial event to start with...

for ebs in ebsvec:
    meandata = zeros([21,14])
    vardata = zeros([21,14])
    runsumdata = zeros([21,14])
    sum2data = zeros([21,14])
    for event in xrange(initev,nevs+initev):
        #infile = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d/HBTradii_cfs_ev%(event)d%(df)s.dat_cfs_0' % {"event": event, "ebsstring": ebs, "TV": TVidx, "df": df_stem}
        infile = 'RESULTS_etaBYs_%(ebsstring)s/results-%(event)d/HBTradii_cfs_ev%(event)d%(df)s.dat_cfs_0' % {"event": event, "ebsstring": ebs, "df": df_stem}
        newdata = delete(loadtxt(infile),0,1)
        meandata += newdata
        vardata -= newdata * runsumdata
        runsumdata += newdata
        sum2data += newdata**2
    
    meandata /= nevs
    vardata *= f2
    vardata += f1 * sum2data
    #outfile = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)d/HBTradii_direct_ens_avg_ebs_%(ebsstring)s_cfs_0_%(nevs)devs%(df)s.dat' % {"ebsstring": ebs, "nevs": nevs, "TV": TVidx, "df": df_stem}
    #outfile2 = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)d/HBTradii_direct_variance_ebs_%(ebsstring)s_cfs_0_%(nevs)devs%(df)s.dat' % {"ebsstring": ebs, "nevs": nevs, "TV": TVidx, "df": df_stem}
    outfile = 'RESULTS_etaBYs_%(ebsstring)s/HBTradii_direct_ens_avg_ebs_%(ebsstring)s_cfs_0_%(nevs)devs%(df)s.dat' % {"ebsstring": ebs, "nevs": nevs, "df": df_stem}
    outfile2 = 'RESULTS_etaBYs_%(ebsstring)s/HBTradii_direct_variance_ebs_%(ebsstring)s_cfs_0_%(nevs)devs%(df)s.dat' % {"ebsstring": ebs, "nevs": nevs, "df": df_stem}
    savetxt(outfile, meandata)
    savetxt(outfile2, vardata)
    #print 'Finished eta/s =', ebs, ', TV =', TVidx

print 'Finished all.'
