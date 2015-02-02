#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import *
from scipy import interpolate
from subprocess import call

#ebs = sys.argv[1]

#nevs = 1000
initialevent = 1
eps = 0.000001
TdepV = 2

def generate_FOsurface_plots(event, localpT):
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	#ax = fig.add_axes([0.1,0.1,0.8,0.8])
	ax = fig.add_subplot(111, projection='3d')
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	
	# load data
	#direc = 'NEW_TDEP_V3/NEW_TDEP_V3_results-avg-%(event)d' % {"event": event}
	#direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d' % {"event": event, "TV": TdepV}
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"TV": TdepV}
	#cols = [1, 2, 3, 11, 12]
	#commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > NEW_TDEP_V4_generate_FOsurface_plots_w_avgS_ev' + event + '.temp'
	#commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > generate_FOsurface_plots_w_avgS_ev' + str(event) + '.temp'
	#print 'Running:', commandstring
	#return_code = call(commandstring, shell=True)
	#fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev1.dat'
	data = loadtxt(fileToProcess)
	
	# set-up data
	pT = data[:,0]
	#print data.shape, localpT, pT, where(abs(pT-localpT) <= eps), (where(abs(pT-localpT) <= eps))[0]
	tau = data[(where(abs(pT-localpT) <= eps))[0],1]
	xT = data[(where(abs(pT-localpT) <= eps))[0],2]
	yT = data[(where(abs(pT-localpT) <= eps))[0],3]
	avgS = data[(where(abs(pT-localpT) <= eps))[0],4]
	norm = sum(avgS)
	rT = sqrt(xT**2 + yT**2)
	
	# plot results
	#print norm, min(avgS), max(avgS)
	ax.scatter(xT, yT, tau, s=20.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	#ax.scatter(xT, yT, tau, s=50000.0*avgS/norm, c=avgS/norm, alpha=0.5, edgecolor='')
	ax.axis([xlower, xupper, ylower, yupper])
	#plt.colorbar()
	plt.show()
	KTstring = "%0.1f" % localpT
	outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_0.20.pdf'
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile





if __name__ == "__main__":
	for KT in linspace(0,2,5):
		generate_FOsurface_plots(759, KT)



# End of file
