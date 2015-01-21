from math import *
#import sys
from numpy import *
from numpy.linalg import *
from scipy.interpolate import *

def find_nearest_neighbor(x, v):			# x is point, v is list of point of same dimension
	d = norm(v-x,axis=1)				# returns point in v closest to x
	minidx = argmin(d)
	return minidx, v[minidx]

def my_interp(p1,p2,z0):
	scale = (z0-p1[-1])/(p2[-1]-p1[-1])
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

nevs = 1
nbins = 10000
cols = [0, 2, 3, 5]					# columns of Surface*.dat files: tau, vT, X, Y
eps = 0.000001

slicestring = 'X'					# X or Y

#for event in xrange(1, nevs+1):
for event in [3]:
	surfXdatafile = 'results-%(event)d/Surface%(slicestring)s.dat' % {"event": event, "slicestring": slicestring}
	surfXdata = loadtxt(surfXdatafile)
	surfX_gt_0 = surfXdata[where(surfXdata[:,3]>=0)][:,cols]
	taumin = min(surfX_gt_0[:,0]) - eps
	taumax = max(surfX_gt_0[:,0]) + eps
	vTmin = min(surfX_gt_0[:,1]) - eps
	vTmax = max(surfX_gt_0[:,1]) + eps
	xmin = min(surfX_gt_0[:,2]) - eps
	xmax = max(surfX_gt_0[:,2]) + eps
	taubins = linspace(taumin,taumax,nbins+1)
	vTbins = linspace(vTmin,vTmax,nbins+1)
	xbins = linspace(xmin,xmax,nbins+1)
	tauinds = digitize(surfX_gt_0[:,0],taubins)-1
	vTinds = digitize(surfX_gt_0[:,1],vTbins)-1
	xinds = digitize(surfX_gt_0[:,2],xbins)-1
	taubincenters = 0.5*(delete(taubins,0)+delete(taubins,-1))
	vTbincenters = 0.5*(delete(vTbins,0)+delete(vTbins,-1))
	xbincenters = 0.5*(delete(xbins,0)+delete(xbins,-1))
	surfXdataBINNED = vstack((taubincenters[tauinds],vTbincenters[vTinds],xbincenters[xinds],surfX_gt_0[:,3])).transpose()
	surfXdataBINNEDnegY = surfXdataBINNED[where(surfXdataBINNED[:,3]<0)]
	surfXdataBINNEDposY = surfXdataBINNED[where(surfXdataBINNED[:,3]>0)]

	print surfXdataBINNED.shape

	interpresults1 = empty(4)
	interpresults2 = empty(4)

	# N.B. - CURRENTLY DOING NEAREST NEIGHBOR SEARCH IN VT SPACE ALSO!
	# N.B. - MAY NEED TO CHANGE THIS!
	# N.B. - SEEMS TO BE WORKING FINE HERE, LEAVING AS IS FOR NOW

	for i in longer(surfXdataBINNEDposY, surfXdataBINNEDnegY):
		ith_nn_idx, ith_nn = find_nearest_neighbor(i, shorter(surfXdataBINNEDposY, surfXdataBINNEDnegY))
		interpresults1 = vstack((interpresults1, my_interp(i, ith_nn, 0)))

	for i in shorter(surfXdataBINNEDposY, surfXdataBINNEDnegY):
		ith_nn_idx, ith_nn = find_nearest_neighbor(i, longer(surfXdataBINNEDposY, surfXdataBINNEDnegY))
		interpresults2 = vstack((interpresults2, my_interp(i, ith_nn, 0)))

	interpresults1 = delete(interpresults1,0,0)
	interpresults2 = delete(interpresults2,0,0)
	interpresultsALL = vstack((interpresults1, interpresults2))

	interpresults1COPY = interpresults1
	interpresults2COPY = interpresults2
	interpresultsallCOPY = interpresultsALL

	# start with first point, delete from the copy, look for the nearest neighbor, delete, etc...
	#interp1SORTED = interpresults1[0]
	#interp2SORTED = interpresults2[0]
	#interpALLSORTED = interpresultsALL[0]
	interp1SORTED = empty(4)
	interp2SORTED = empty(4)
	interpALLSORTED = empty(4)
	interp1SORTED = vstack((interp1SORTED,interpresults1[0]))
	interp2SORTED = vstack((interp2SORTED,interpresults2[0]))
	interpALLSORTED = vstack((interpALLSORTED,interpresultsALL[0]))
	interpresults1COPY = delete(interpresults1COPY,0,0)
	interpresults2COPY = delete(interpresults2COPY,0,0)
	interpresultsALLCOPY = delete(interpresultsallCOPY,0,0)

	interp1SORTED = delete(interp1SORTED,0,0)
	interp2SORTED = delete(interp2SORTED,0,0)
	interpALLSORTED = delete(interpALLSORTED,0,0)

	templen1 = len(interpresults1COPY)
	templen2 = len(interpresults2COPY)
	templenALL = len(interpresultsALLCOPY)

	# sort on proximity in tau-rT-vT space
	rTvTcols = [0, 1, 2, 3]
	while templen1 > 0:
		NN_pt_idx, NN_pt = find_nearest_neighbor(interp1SORTED[-1,rTvTcols], interpresults1COPY[:,rTvTcols])
		interp1SORTED = vstack((interp1SORTED,interpresults1COPY[NN_pt_idx]))
		interpresults1COPY = delete(interpresults1COPY,NN_pt_idx,0)
		templen1-=1
		#NN_pt_idx, NN_pt = find_nearest_neighbor(interp1SORTED[-1], interpresults1COPY)
		#interp1SORTED = vstack((interp1SORTED,NN_pt))
		#interpresults1COPY = delete(interpresults1COPY,NN_pt_idx,0)
		#templen1-=1

	while templen2 > 0:
		NN_pt_idx, NN_pt = find_nearest_neighbor(interp2SORTED[-1,rTvTcols], interpresults2COPY[:,rTvTcols])
		interp2SORTED = vstack((interp2SORTED,interpresults2COPY[NN_pt_idx]))
		interpresults2COPY = delete(interpresults2COPY,NN_pt_idx,0)
		templen2-=1
		#NN_pt_idx, NN_pt = find_nearest_neighbor(interp2SORTED[-1], interpresults2COPY)
		#interp2SORTED = vstack((interp2SORTED,NN_pt))
		#interpresults2COPY = delete(interpresults2COPY,NN_pt_idx,0)
		#templen2-=1

	while templenALL > 0:
		NN_pt_idx, NN_pt = find_nearest_neighbor(interpALLSORTED[-1,rTvTcols], interpresultsALLCOPY[:,rTvTcols])
		interpALLSORTED = vstack((interpALLSORTED,interpresultsALLCOPY[NN_pt_idx]))
		interpresultsALLCOPY = delete(interpresultsALLCOPY,NN_pt_idx,0)
		templenALL-=1
		#NN_pt_idx, NN_pt = find_nearest_neighbor(interpALLSORTED[-1], interpresultsALLCOPY)
		#interpALLSORTED = vstack((interpALLSORTED,NN_pt))
		#interpresultsALLCOPY = delete(interpresultsALLCOPY,NN_pt_idx,0)
		#templenALL-=1	

	outfile1 = 'results-%(event)d/interplist%(slicestring)s1.out' % {"event": event, "slicestring": slicestring}
	outfile2 = 'results-%(event)d/interplist%(slicestring)s2.out' % {"event": event, "slicestring": slicestring}
	outfileALL = 'results-%(event)d/interplist%(slicestring)s_all.out' % {"event": event, "slicestring": slicestring}

	savetxt(outfile1,asarray(interp1SORTED))
	savetxt(outfile2,asarray(interp2SORTED))
	savetxt(outfileALL,asarray(interpALLSORTED))

	print 'Finished event', event
