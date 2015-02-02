from math import *
import sys
from numpy import *
from numpy.linalg import *
from scipy.interpolate import *
import os.path as path

def find_nearest_neighbor(x, v):			# x is point, v is list of points of same dimension
	d = norm(v-x,axis=1)				# returns point in v closest to x
	minidx = argmin(d)
	return minidx, v[minidx]

def my_interp(p1,p2,z0,zidx):
	scale = (z0-p1[zidx])/(p2[zidx]-p1[zidx])
	res=p1 + scale*(p2-p1)
	return res

def longer(v1, v2):
	if len(v1) >= len(v2):
		return v1
	else:
		return v2

def shorter(v1, v2):
	if len(v1) < len(v2):
		return v1
	else:
		return v2

surfXdatafile = sys.argv[1]

nevs = 1
cols = [0, 3, 4, 5, 6]					# columns of Surface*.dat files: tau, vT, X, Y

#surfXdatafile = 'NEW_TDEP_V1/NEW_TDEP_V1_results-%(event)d/Surface_posX.dat' % {"event": event}
surfX_gt_0 = loadtxt(surfXdatafile)[:,cols]
#surfX_gt_0 = surfXdata[where(surfXdata[:,1]>=0)]			# yes, this is correct, only interpolate for positive (or negative) X
surfXdataBINNED = surfX_gt_0
surfXdataBINNEDnegY = surfXdataBINNED[where(surfXdataBINNED[:,3]<0)]	# in the sliced array, column three is now the y-coordinate
surfXdataBINNEDposY = surfXdataBINNED[where(surfXdataBINNED[:,3]>0)]	# (again) in the sliced array, column three is now the y-coordinate

interpresults1 = empty(len(cols))
interpresults2 = empty(len(cols))

longervec = longer(surfXdataBINNEDposY, surfXdataBINNEDnegY)
shortervec = shorter(surfXdataBINNEDposY, surfXdataBINNEDnegY)

#for i in xrange(len(longervec)):
#	ith_entry = longervec[i,:]
#	ith_nn_idx, ith_nn = find_nearest_neighbor(ith_entry, shortervec)
#	interpresults1 = vstack((interpresults1, my_interp(longervec[i], shortervec[ith_nn_idx], 0, 3)))	# interpolate over column 3 to value 0

for i in xrange(len(shortervec)):
	ith_entry = shortervec[i,:]
	ith_nn_idx, ith_nn = find_nearest_neighbor(ith_entry, longervec)
	interpresults2 = vstack((interpresults2, my_interp(shortervec[i], longervec[ith_nn_idx], 0, 3)))	# interpolate over column 3 to value 0
	#longervec = delete(longervec, ith_nn_idx, 0)

#interpresults1 = delete(interpresults1,0,0)
interpresults2 = delete(interpresults2,0,0)
#interpresultsALL = vstack((interpresults1, interpresults2))
interpresultsALL = interpresults2

interpresultsallCOPY = interpresultsALL

# SORTING BEGINS HERE...
# start with first point, delete from the copy, look for the nearest neighbor, delete, etc...
interpALLSORTED = empty(len(cols))

sortslice = where(max(interpresultsALL[:,1]**2 + interpresultsALL[:,2]**2 - 100.*(interpresultsALL[:,3]**2 + interpresultsALL[:,4]**2)))
#print interpALLSORTED.shape, interpresultsALL[sortslice].shape

interpALLSORTED = vstack((interpALLSORTED,interpresultsALL[sortslice]))

interpresultsALLCOPY = delete(interpresultsallCOPY,sortslice,0)

interpALLSORTED = delete(interpALLSORTED,0,0)

templenALL = len(interpresultsALLCOPY)

# sort on proximity in tau-rT-vT space (i.e., nearest-neighbor)
rTvTcols = [0, 1, 2, 3]

while templenALL > 0:
	NN_pt_idx, NN_pt = find_nearest_neighbor(interpALLSORTED[-1,:], interpresultsALLCOPY)
	interpALLSORTED = vstack((interpALLSORTED,interpresultsALLCOPY[NN_pt_idx]))
	interpresultsALLCOPY = delete(interpresultsALLCOPY,NN_pt_idx,0)
	templenALL-=1

#print asarray(interp1SORTED).shape
#print asarray(interp2SORTED).shape

#outfileALL = 'NEW_TDEP_V1/NEW_TDEP_V1_results-%(event)d/vT_vs_X_nnSORTED.out' % {"event": event}
outfileALL = path.dirname(surfXdatafile) + '/vT_vs_X_nnSORTED.out'

savetxt(outfileALL, asarray(interpALLSORTED), fmt='%15.10f')

print 'Finished interpolating and nearest-neighbor sorting', surfXdatafile, 'into', outfileALL
