#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import *
from scipy import interpolate
from subprocess import call

#ebs = sys.argv[1]
ebs = 0.08

#nevs = 1000
initialevent = 1
eps = 0.000001

def generate_FOsurface_plots(event, localpT):
	# set-up
	plotfontsize = 18
	fig1 = plt.figure()
	#ax = fig1.add_axes([0.1,0.1,0.8,0.8])
	ax = fig1.add_subplot(111, projection='3d')
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	
	# load data
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_%(ebs)0.2f/NEW_TDEP_V1/NEW_TDEP_V1_results-%(event)d' % {"event": event, "ebs": ebs}
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
	decdatFileToProcess = direc + '/decdat2.dat'
	data = loadtxt(fileToProcess)
	decdatdata = loadtxt(decdatFileToProcess)[:,[4,5]]	# vx, vy
	
	# set-up data
	pT = data[:,0]
	tau = data[(where(abs(pT-localpT) <= eps))[0],1]
	xT = data[(where(abs(pT-localpT) <= eps))[0],2]
	yT = data[(where(abs(pT-localpT) <= eps))[0],3]
	vx = decdatdata[:,0]
	vy = decdatdata[:,1]
	avgS = data[(where(abs(pT-localpT) <= eps))[0],4]
	rT = sqrt(xT**2 + yT**2)
	vT = sqrt(vx**2 + vy**2)
	
	# plot results
	#print min(avgS), max(avgS)
	#plt.scatter(rT, tau, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	ax.scatter(xT, yT, tau, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	#ax.scatter(xT, yT, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	ax.axis([xlower, xupper, ylower, yupper])
	#plt.colorbar()
	fig1.show()

	fig2 = plt.figure()
	ax2 = fig2.add_axes([0.1,0.1,0.8,0.8])
	ax2.scatter(rT, vT, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	fig2.show()
	KTstring = "%0.1f" % localpT
	outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_%(ebs)d.pdf' % {"ebs": ebs}
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile





if __name__ == "__main__":
	for KT in linspace(0,2,5):	# i.e., for KT = 0.0, 0.5, 1.0, 1.5, and 2.0 GeV
		generate_FOsurface_plots(759, KT)
		try:
			input("Press enter to continue")
		except SyntaxError:
			pass



# End of file
