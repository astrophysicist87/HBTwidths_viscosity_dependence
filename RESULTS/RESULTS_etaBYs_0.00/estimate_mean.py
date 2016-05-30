from math import *
import sys
from numpy import *
from numpy.linalg import *
from scipy.interpolate import *
import os.path as path

def get_wnk(multiplicities):
	temp = multiplicities**2
	return temp/sum(temp)

def get_Vnl(weights, l):
	return sum(weights**l)

def get_relativeBinWeight(binMultiplicities, totalMultiplicities):
	return sum(binMultiplicities**2)/sum(totalMultiplicities**2)

M = float(sys.argv[1])
Nev = 1000.
nb = float(sys.argv[2])
homeDirectory='/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.00'

Cavgdatafilename = homeDirectory + '/CavgHBTradii_osl_cfs_0_evs1to1000_no_df.dat'
Cavgdata = loadtxt(Cavgdatafilename)
KT = Cavgdata[:,0]
nKT = len(KT)
Cavgdata = Cavgdata[:,1:4]
#print KT
#print Cavgdata
runningsum = zeros(Cavgdata.shape)

#read in information about all subensembles
print 'Reading in information about all subensembles...'

multiplicitiesFile = homeDirectory + '/simulations/subensemble_nb2_indexfile.dat'
subensembleBinsAndEventIndices = loadtxt(multiplicitiesFile)[:,2:((Nev/nb) + 3)].reshape(M,nb,Nev/nb).astype(int)-1
# subtract one to convert results file indices to array indices

print 'Finished reading in multiplicities.'

#read in multiplicities and get weights...
eventByEventMultiplicities = zeros([Nev,nKT])
print 'Reading in multiplicities...'

for event in xrange(int(Nev)):
	multiplicitiesFile = homeDirectory + '/results-%(ev)d/Multiplicities_vs_KT_cfs_0.dat' % {"ev": event + 1}
	eventByEventMultiplicities[event,:] = loadtxt(multiplicitiesFile)[:,1]

print 'Finished reading in multiplicities.'

allMultiplicityWeights = 



#finalResults = hstack((reshape(KT,[nKT,1]),Cavgdata,relativeResults))

#outfile = homeDirectory + '/sigma_estimate_nb%(nb)d_nevs%(Nev)d_binnings%(Mval)d.dat' % {"nb": int(nb), "Nev": int(Nev), "Mval": int(M)}
#savetxt(outfile, finalResults, fmt='%2.1f' + 6*' %20.9f')

print 'Finished everything.'

# End of file
