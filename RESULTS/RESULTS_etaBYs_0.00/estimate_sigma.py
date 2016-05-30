from math import *
import sys
from numpy import *
from numpy.linalg import *
from scipy.interpolate import *
import os.path as path

def get_wnk(multiplicities):
	temp = multiplicities**2
	# sum(xxx,0) gives sum of xxx over first dimension only (i.e., events)
	return temp/sum(temp)

def get_Vnl(weights, l):
	# sum(xxx,0) gives sum of xxx over first dimension only (i.e., events)
	return sum(weights**l)

def get_relativeBinWeight(binMultiplicities, totalMultiplicities):
	# sum(xxx,0) gives sum of xxx over first dimension only (i.e., events)
	return sum(binMultiplicities**2)/sum(totalMultiplicities**2)

M = float(sys.argv[1])
nb = float(sys.argv[2])
Nev = float(sys.argv[3])
homeDirectory='/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.00'

#Cavgdatafilename = homeDirectory + '/CavgHBTradii_osl_cfs_0_evs1to1000_no_df.dat'
Cavgdatafilename = homeDirectory + '/CavgHBTradii_azavg_evs1to1000_no_df.dat'
Cavgdata = loadtxt(Cavgdatafilename)
KT = Cavgdata[:,0]
nKT = len(KT)
Cavgdata = Cavgdata[:,[1,2,4]]
#print KT
#print Cavgdata
bigsum = zeros(Cavgdata.shape)
runningsum = zeros(Cavgdata.shape)

#load DEA data as well!!!
DEAavgdatafilename = homeDirectory + '/HBTradii_direct_ens_avg_ebs_0.00_azavg_1000evs_no_df.dat'
DEAavgdata = loadtxt(DEAavgdatafilename)[:,[1,2,4]]

#read in information about all subensembles
print 'Reading in information about all subensembles...'

multiplicitiesFile = homeDirectory + '/az_avg_simulations/subensemble_nb2_indexfile.dat'
subensembleBinsAndEventIndices = loadtxt(multiplicitiesFile)[0:(nb*M),2:((Nev/nb) + 3)].reshape(M,nb,Nev/nb).astype(int)-1
# subtract one to convert results file indices to array indices
#print subensembleBinsAndEventIndices[0,0,:]
#sys.exit(0)

print 'Finished reading in information about all subensembles.'

#read in multiplicities and get weights...
eventByEventMultiplicities = zeros([Nev,nKT])
print 'Reading in multiplicities...'

for event in xrange(int(Nev)):
	multiplicitiesFile = homeDirectory + '/results-%(ev)d/Multiplicities_vs_KT_cfs_0.dat' % {"ev": event + 1}
	eventByEventMultiplicities[event,:] = loadtxt(multiplicitiesFile)[:,1]

print 'Finished reading in multiplicities.'

print 'eventByEventMultiplicities.shape = ', eventByEventMultiplicities.shape

relativeBinWeights = zeros([nb,nKT])

#now run through Cavg results for each binning/bin and compute sigma estimate
for iKT in xrange(int(nKT)):
	for binningIteration in xrange(int(M)):
		for binIndex in xrange(int(nb)):
			filename = homeDirectory + '/az_avg_simulations/binning_%(binit)d/CavgHBTradii_binning%(binit)d_nb%(nb)d_bin%(binid)d_no_df.dat' % {"nb": nb, "binit": binningIteration, "binid": binIndex}
			data = loadtxt(filename)[:,1:4]
			binMultiplicities = eventByEventMultiplicities[subensembleBinsAndEventIndices[binningIteration,binIndex,:],iKT]
			#print 'binMultiplicities.shape = ', binMultiplicities.shape
			binWeights = get_wnk(binMultiplicities)
			#print 'binWeights.shape = ', binWeights.shape
			Vn2 = get_Vnl(binWeights, 2)
			#print 'Vn2 = ', Vn2
			relativeBinWeights[binIndex,iKT] = get_relativeBinWeight(binMultiplicities, eventByEventMultiplicities[:,iKT])
			#print 'relativeBinWeights.shape = ', relativeBinWeights.shape
			runningsum[iKT,:] += (relativeBinWeights[binIndex,iKT]*(data[iKT,:]-Cavgdata[iKT,:])**2)/Vn2
			#runningsum += (data-Cavgdata)**2
			#print 'runningsum.shape = ', runningsum.shape
		Vtildenb2 = get_Vnl(relativeBinWeights[:,iKT], 2)
		#print "Check:", get_Vnl(relativeBinWeights[:,iKT], 1)
		#print 'Vtildenb2 = ', Vtildenb2
		bigsum[iKT,:] += runningsum[iKT,:]/(1.-Vtildenb2)
		runningsum = zeros(Cavgdata.shape)
	print 'Finished binning iteration = %(binit)d' % {"binit": binningIteration}

factor = 1./M
print 'eventByEventMultiplicities.shape = ', eventByEventMultiplicities.shape
#factor = Nev / (M*nb*(nb-1.))
absoluteResults = factor * bigsum
sqrtAbsoluteResults = sqrt(absoluteResults)
relativeResults = sqrtAbsoluteResults / DEAavgdata

finalResults = hstack((reshape(KT,[nKT,1]),DEAavgdata,sqrtAbsoluteResults,relativeResults))

outfile = homeDirectory + '/az_avg_simulations/sigma_estimate_nb%(nb)d_nevs%(Nev)d_binnings%(Mval)d_with_weights.dat' % {"nb": int(nb), "Nev": int(Nev), "Mval": int(M)}
savetxt(outfile, finalResults, fmt='%2.1f' + 9*' %20.9f')

print 'Finished everything.'

# End of file
