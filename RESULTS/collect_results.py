#!/usr/bin/env python

# first command-line argument: directory containing results sub-directories for processing
# (assumed to being with 'RESULTS_')

from numpy import *
import sys
from subprocess import call

nevs = 1000
#ebs = float(sys.argv[1])
TDEPebs = ''
maxorder = 3
nKT = 21
eps = 0.000001
#df_stem = ''
#df_stem = '_no_df'
#VEC_df_stem = ['_no_df']
VEC_df_stem = ['']
abs_stem = ''
#abs_stem = '_w_abs'
HBTcolsC = [3, 5, 7, 9, 11, 13]
HBTcolsS = [4, 6, 8, 10, 12, 14]

def collect_HBTandSV_coefficients_fromDirec(path, allCOScoefficients, allSINcoefficients, df_stem):
	for ev in xrange(1,nevs+1):
		# define filenames
		infile1=path + '%(ev)d/HBTradii_cfs_ev%(ev)d' % {"ev": ev} + df_stem + '.dat_neqn'
		infile2=path + '%(ev)d/Sourcefunction_variances_cfs_COS' % {"ev": ev} + df_stem + '.dat_neqn'
		infile3=path + '%(ev)d/Sourcefunction_variances_cfs_SIN' % {"ev": ev} + df_stem + '.dat_neqn'
		
		# load data
		data1=loadtxt(infile1)
		data2=loadtxt(infile2)
		data3=loadtxt(infile3)
		
		for order in xrange(maxorder+1):
			# select interesting data
			tempdata1 = data1[(where(abs(data1[:,2]-order) <= eps))]
			tempdata2 = data2[(where(abs(data2[:,2]-order) <= eps))]
			tempdata3 = data3[(where(abs(data3[:,2]-order) <= eps))]
			
			# select KT slices
			iKT = 0
			for KT in linspace(0,2,nKT):
				KTslice1a = tempdata1[(where(abs(tempdata1[:,1]-KT) <= eps))][:,HBTcolsC]
				KTslice1b = tempdata1[(where(abs(tempdata1[:,1]-KT) <= eps))][:,HBTcolsS]
				KTslice2a = tempdata2[(where(abs(tempdata2[:,1]-KT) <= eps))][:,3:]		# discard event number, KT and order
				KTslice2b = tempdata3[(where(abs(tempdata3[:,1]-KT) <= eps))][:,3:]		# discard event number, KT and order
				#KTslice1 = sign(KTslice1a+KTslice1b)*sqrt(KTslice1a**2 + KTslice1b**2)	# keep overall sign of harmonic component with larger magnitude
				#KTslice2 = sign(KTslice2a+KTslice2b)*sqrt(KTslice2a**2 + KTslice2b**2)	# keep overall sign of harmonic component with larger magnitude
				
				#if abs_stem == '_w_abs':
				#	KTslice1 = abs(KTslice1)
				#	KTslice2 = abs(KTslice2)
				
				allCOScoefficients[ev-1, order, iKT] = hstack((KTslice1a, KTslice2a))
				allSINcoefficients[ev-1, order, iKT] = hstack((KTslice1b, KTslice2b))
				iKT += 1
	
		#print '  --> TV =', TVidx,': Finished slicing event =', ev

def collect_HBTandSV_coefficients(df_stem, direc):
	#direc='RESULTS_etaBYs_%(ebs)0.2f' % {"ebs": ebs}
	subdirec="results"
	path=direc + '/' + subdirec + '-'
	allCOScoefficients = empty([nevs, maxorder+1, nKT, 16])
	allSINcoefficients = empty([nevs, maxorder+1, nKT, 16])
	collect_HBTandSV_coefficients_fromDirec(path, allCOScoefficients, allSINcoefficients, df_stem)
	
	for order in xrange(maxorder+1):
		iKT = 0
		for KT in linspace(0,2,nKT):
			outfileCOS = direc + '/EbE_HBT_and_SV_KT_%(KT)0.1f_GeV_%(nevs)devs_COSneq%(ord)d' % {"KT": KT, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
			outfileSIN = direc + '/EbE_HBT_and_SV_KT_%(KT)0.1f_GeV_%(nevs)devs_SINneq%(ord)d' % {"KT": KT, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
			#print 'Saving *neq%(ord)d.dat files' % {"ord": order}
			outCOSdata = allCOScoefficients[:, order, iKT, :]
			outSINdata = allSINcoefficients[:, order, iKT, :]
			savetxt(outfileCOS, outCOSdata, fmt='%f')
			savetxt(outfileSIN, outSINdata, fmt='%f')
			iKT += 1





def generate_complete_FOsurface_properties(df_stem, direc):
	# outputs magnitudes of given harmonics in format:
	# K_T, R^2_s, R^2_o, R^2_{os}, R^2_l, R^2_{ls}, R^2_{ol}, <x_s t>, <x_o t>, <x_l t>, <x_o x_s>, <x_l x_s>, <x_o x_l>, <x^2_s>, <x^2_o>, <x^2_l>, <t^2>
	#direc='RESULTS_etaBYs_%(ebs)0.2f' % {"ebs": ebs}
	allCOSresults = empty([nKT, 33])
	allSINresults = empty([nKT, 33])
	for order in xrange(maxorder+1):
		iKT = 0
		for KT in linspace(0,2,nKT):
			inCOSfile = direc + '/EbE_HBT_and_SV_KT_%(KT)0.1f_GeV_%(nevs)devs_COSneq%(ord)d' % {"KT": KT, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
			inSINfile = direc + '/EbE_HBT_and_SV_KT_%(KT)0.1f_GeV_%(nevs)devs_SINneq%(ord)d' % {"KT": KT, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
			COSdata = loadtxt(inCOSfile)
			SINdata = loadtxt(inSINfile)
			allCOSresults[iKT, :] = hstack((KT, mean(COSdata,0), var(COSdata,0)))
			allSINresults[iKT, :] = hstack((KT, mean(SINdata,0), var(SINdata,0)))
			iKT += 1
		outCOSfile = direc + '/complete_FOsurface_properties_%(resultsTag)s_%(nevs)devs_COSneq%(ord)d' % {"resultsTag": TDEPebs, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
		outSINfile = direc + '/complete_FOsurface_properties_%(resultsTag)s_%(nevs)devs_SINneq%(ord)d' % {"resultsTag": TDEPebs, "nevs": nevs, "ord": order} + df_stem + abs_stem + '.dat'
		print 'Saving to', outCOSfile
		savetxt(outCOSfile, allCOSresults, fmt='%f')
		print 'Saving to', outSINfile
		savetxt(outSINfile, allSINresults, fmt='%f')



def cleanup(df_stem, direc):
	print 'Cleaning up', direc
	filePattern = direc + '/EbE_HBT_and_SV_KT_*_GeV_1000evs_*neq[0-9]' + df_stem + abs_stem + '.dat'
	cleanCommandString = 'rm ' + filePattern
	return_code = call(cleanCommandString, shell=True)
	print 'Cleaned up', direc
		


if __name__ == "__main__":
	direc = sys.argv[1]
	TDEPebs = direc.replace('RESULTS_','')
	for iDFSTEM in VEC_df_stem:
		collect_HBTandSV_coefficients(iDFSTEM, direc)
		generate_complete_FOsurface_properties(iDFSTEM, direc)
		cleanup(iDFSTEM, direc)
	


# End of file
