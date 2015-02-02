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

processingStem = 'nnINDEXED'				# tauSORTED, tauINDEXED, nnSORTED, or nnINDEXED
#processStem = sys.argv[1]				# get it from command-line

for event in xrange(1, nevs+1):
    print 'Incorporating files from results-%(event)d/...' % {"event": event}
    #surfXdatafile = 'results-%(event)d/vT_vs_X_tauINDEXED.out' % {"event": event}
    surfXdatafile = 'results-%(event)d/vT_vs_X_%(pStem)s.out' % {"event": event, "pStem": processingStem}

    surfXdata=loadtxt(surfXdatafile)

    surfX_gt_0 = surfXdata

    tauXpts=mgrid[(min(surfX_gt_0[:,0])+eps):(max(surfX_gt_0[:,0])-eps):(npts)*(1j)]	# the two extra points will be deleted
    gridXrpts = griddata(surfX_gt_0[:,0],surfX_gt_0[:,2],tauXpts,method=interpolationmethod)
    gridXvpts = griddata(surfX_gt_0[:,0],surfX_gt_0[:,1],tauXpts,method=interpolationmethod)

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

    allXresults = vstack((allXresults, array([vstack((tauXpts, gridXrpts, gridXvpts))])))

allXresults = delete(allXresults,0,0)

Xmeans = mean(allXresults,axis=0)

outfile = 'mean_transverseflowprofile_%(pStem)s_%(numpts)dpts.out' % {"numpts": npts, "pStem": processingStem}

savetxt(outfile,asarray(Xmeans))

print 'Finished all.'
