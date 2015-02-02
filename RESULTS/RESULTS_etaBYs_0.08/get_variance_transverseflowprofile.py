from math import *
import sys
from numpy import *
from scipy.interpolate import *
from numpy.linalg import *
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

def find_nearest_neighbor(x, v):			# x is point, v is list of point of same dimension
    d = norm(v-x,axis=1)				# returns point in v closest to x
    minidx = argmin(d)
    return minidx, v[minidx]

def get_normal_2D(v, idx):				# v is a n x 2 column vector
    slope = get_slope_2D(v, idx)
    return -1./slope

def get_slope_2D(v, idx):
    n = len(v)
    if ( idx == 0 ):
        slope = (v[idx+1,1] - v[idx,1])/(v[idx+1,0] - v[idx,0])		# if idx at beginning of v, just return forward slope
    elif ( idx == n-1 ):
        slope = (v[idx,1] - v[idx-1,1])/(v[idx,0] - v[idx-1,0])		# if idx at end of v, just return backward slope
    else:
        slope1 = (v[idx,1] - v[idx-1,1])/(v[idx,0] - v[idx-1,0])	# backward slope
        slope2 = (v[idx+1,1] - v[idx,1])/(v[idx+1,0] - v[idx,0])	# forward slope
        slope = 0.5*(slope1+slope2)					# average the two slopes
    
    return slope

allXresults = empty([1, 2, npts])
processingStem = 'nnINDEXED'				# tauSORTED, tauINDEXED, nnSORTED, or nnINDEXED

meansurfXdatafile = 'mean_transverseflowprofile_%(pStem)s_%(numpts)dpts.out' % {"numpts": npts, "pStem": processingStem}
meansurfXdata = loadtxt(meansurfXdatafile)[:, 1:3]

runningsum = zeros(npts)
runningsum2 = zeros(npts)
nn_count = zeros(npts) + 1.e-15
vardists = zeros(npts)

for event in xrange(1, nevs+1):
    print 'Incorporating files from results-%(event)d/...' % {"event": event}
    #surfXdatafile = 'results-%(event)d/vT_vs_X_INDEXED.out' % {"event": event}
    surfXdatafile = 'results-%(event)d/vT_vs_X_%(pStem)s.out' % {"event": event, "pStem": processingStem}
    surfXdata = loadtxt(surfXdatafile)[:, cols]

    indicesX=mgrid[(min(surfXdata[:,0])+eps):(max(surfXdata[:,0])-eps):(npts)*(1j)]	# the two extra points will be deleted
    gridXrpts = griddata(surfXdata[:,0], surfXdata[:,2], indicesX, method=interpolationmethod)
    gridXvpts = griddata(surfXdata[:,0], surfXdata[:,1], indicesX, method=interpolationmethod)

    # check if there are any NaN's left
    if vector_has_nans(gridXrpts):
        numnans = find_nans_in_vector(gridXrpts).size
        print 'gridXrpts contains', numnans, 'nan(s) from event', event
        print find_nans_in_vector(gridXrpts)
        print find_nans_in_vector(surfXdata[:,0]), find_nans_in_vector(surfXdata[:,2]), find_nans_in_vector(indicesX)
        raw_input("Press [enter] to continue.")

    if vector_has_nans(gridXvpts):
        numnans = find_nans_in_vector(gridXvpts).size
        print 'gridXvpts contains', numnans, 'nan(s) from event', event
        print find_nans_in_vector(gridXvpts)
        print find_nans_in_vector(surfXdata[:,0]), find_nans_in_vector(surfXdata[:,1]), find_nans_in_vector(indicesX)
        raw_input("Press [enter] to continue.")

    allXresults = vstack((allXresults, array([vstack((gridXrpts, gridXvpts))])))
    if event==1:
        allXresults = delete(allXresults,0,0)

    #print allXresults.shape

    for pt in xrange(npts):
        # find nearest neighbor along mean surface transverse flow profile to given point along particular event curve
        # store point and distance
        locpt = allXresults[event-1, :, pt]
        pt_nn_idx, pt_nn = find_nearest_neighbor(locpt, meansurfXdata)
        dist = norm(pt_nn - locpt)
	if isnan(dist):
            print 'Found dist = NaN at pt = %(pt)d!!' % {"pt": pt}
            print pt_nn_idx, pt_nn, locpt
        
        runningsum[pt_nn_idx] += dist
        runningsum2[pt_nn_idx] += dist**2
        nn_count[pt_nn_idx] += 1.
        vardists[pt_nn_idx] -= dist*runningsum[pt_nn_idx]


# now, compute means, variances and standard deviations over every point along mean curve
meandists = runningsum/nn_count
vardists *= 2./(nn_count**2)
vardists += ((nn_count-1.)/(nn_count**2))*runningsum2
sigmadists = sqrt(vardists)

# get normals along meansurfXdata
meannormals = zeros(npts)
print 'Computing normals along mean surface curve...'
for i in xrange(npts):
    meannormals[i] = get_normal_2D(meansurfXdata, i)

phivec = arctan(meannormals)

possigma = nan_to_num(vstack((sigmadists*cos(phivec),sigmadists*sin(phivec))).transpose())

print possigma

finalXout = hstack((meansurfXdata, meansurfXdata+possigma, meansurfXdata-possigma))

outfile = 'variance_transverseflowprofile_%(pStem)s_%(numpts)dpts.out' % {"numpts": npts, "pStem": processingStem}

#savetxt('REPROCESSED_testfinalX.out_%(numpts)dpts' % {"numpts": npts},asarray(finalXout))
savetxt(outfile,asarray(finalXout))

print 'Finished all.'
