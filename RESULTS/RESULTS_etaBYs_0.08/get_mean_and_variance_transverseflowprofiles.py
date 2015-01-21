from math import *
import sys
from numpy import *
from scipy.interpolate import *
from scipy import stats

nevs = 1000						# number of events to use in averaging of transverse flow profiles
npts = 250						# number of points in tau at which to perform interpolation
interpolationmethod = 'linear'				# method of interpolation to use
cols = [0, 1, 2]					# columns of input files: tau, vT, X
eps = 0.000001

def vector_has_nans(v):					# returns number of NaN's in v
    return argwhere(isnan(v)).size

def find_nans_in_vector(v):				# returns the indices of any Nan's in v
    return argwhere(isnan(v))

def delete_endpoints(v):				# deletes endpoints of v
    return delete(v, [0, len(v)-1])

allXresults = empty([1, 3, npts])
allYresults = empty([1, 3, npts])

for event in xrange(1, nevs+1):
    print 'Incorporating files from results-%(event)d/...' % {"event": event}
    #surfXdatafile = 'results-%(event)d/vT_vs_X_INDEXED.out' % {"event": event}
    #surfXdatafile = 'results-%(event)d/SurfaceX.dat' % {"event": event}
    surfXdatafile = 'results-%(event)d/vT_vs_X_tauSORTED.out' % {"event": event}

    surfXdata=loadtxt(surfXdatafile)

    #print 'Read in data for event', event,'. . .'

    #conditionX = surfXdata[:,2]>=0			# select x >= 0

    #surfX_gt_0 = array([extract(conditionX, surfXdata[:,i]) for i in cols]).transpose()

    #print surfXdata.shape, surfX_gt_0.shape
    surfX_gt_0 = surfXdata

    #surfX_gt_0=surfX_gt_0[lexsort((surfX_gt_0[:,2],surfX_gt_0[:,1],surfX_gt_0[:,0]))]

    tauXpts=mgrid[(min(surfX_gt_0[:,0])+eps):(max(surfX_gt_0[:,0])-eps):(npts)*(1j)]	# the two extra points will be deleted
    #tauXpts = delete_endpoints(tauXpts)
    gridXrpts = griddata(surfX_gt_0[:,0],surfX_gt_0[:,2],tauXpts,method=interpolationmethod)
    gridXvpts = griddata(surfX_gt_0[:,0],surfX_gt_0[:,1],tauXpts,method=interpolationmethod)

    # delete interpolated endpoints, tends to cause problems
    #tauXpts = delete_endpoints(tauXpts)
    #gridXrpts = delete_endpoints(gridXrpts)
    #gridXvpts = delete_endpoints(gridXvpts)

    # check if there are any NaN's left
    if vector_has_nans(gridXrpts):
        numnans = find_nans_in_vector(gridXrpts).size
        print 'gridXrpts contains', numnans, 'nan(s) from event', event
        #print gridXrpts
        print find_nans_in_vector(gridXrpts)
        print find_nans_in_vector(surfX_gt_0[:,0]), find_nans_in_vector(surfX_gt_0[:,1]), find_nans_in_vector(tauXpts)
        raw_input("Press [enter] to continue.")

    if vector_has_nans(gridXvpts):
        numnans = find_nans_in_vector(gridXvpts).size
        print 'gridXvpts contains', numnans, 'nan(s) from event', event
        #print gridXvpts
        print find_nans_in_vector(gridXvpts)
        print find_nans_in_vector(surfX_gt_0[:,0]), find_nans_in_vector(surfX_gt_0[:,2]), find_nans_in_vector(tauXpts)
        raw_input("Press [enter] to continue.")

    #print '. . . finished interpolation for event', event

    #print '. . . generating interpolated points for event', event

    allXresults = vstack((allXresults, array([vstack((tauXpts, gridXrpts, gridXvpts))])))

    #print '. . . finished processing event', event

allXresults = delete(allXresults,0,0)

#print 'Finished processing all events --> statistics . . .'

finalXout = empty([1, 6])

Xmeans = mean(allXresults[:,1:3,:],axis=0)
Xsigmas = std(allXresults[:,1:3,:],axis=0)

for iX in xrange(npts):
    slope, intercept, r_value, p_value, std_err = stats.linregress(allXresults[:,1,iX],allXresults[:,2,iX])
    #print 'Found r =', r_value, 'at iX =', iX
    if isnan(r_value):
        print 'Found r = nan at iX =', iX
    if slope < 0:
        sigpts = array([-Xsigmas[0,iX], Xsigmas[1,iX], Xsigmas[0,iX], -Xsigmas[1,iX]])
    else:
        sigpts = array([Xsigmas[0,iX], Xsigmas[1,iX], -Xsigmas[0,iX], -Xsigmas[1,iX]])
    finalXout = vstack((finalXout,hstack((Xmeans[:,iX], sigpts))))

finalXout = delete(finalXout,0,0)

#for iX in xrange(npts):
#	for event in xrange(nevs):
#		print allXresults[event,1,iX], allXresults[event,2,iX]

savetxt('testfinalX.out_%(numpts)dpts' % {"numpts": npts},asarray(finalXout))

print 'Finished all.'
