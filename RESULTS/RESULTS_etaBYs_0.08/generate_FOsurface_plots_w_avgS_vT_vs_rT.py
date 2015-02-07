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
scale = 25.0
TdepV = 1
etaBYsParams = ['LH-LQ', 'LH-HQ', 'HH-LQ', 'HH-HQ']

def generate_FOsurface_plots(event, localpT, TdepV):
	# set-up
	plotfontsize = 18
	fig1 = plt.figure()
	#ax = fig1.add_axes([0.1,0.1,0.8,0.8])
	#ax1 = fig1.add_subplot(131, projection='3d')
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	rTlower, rTupper = 0.0, 10.0
	vTlower, vTupper = 0.0, 0.85
	taulower, tauupper = 0.0, 12.5
	
	# load data
	#direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_%(ebs)0.2f/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d' % {"event": event, "ebs": ebs, "TV": TdepV}
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_%(ebs)0.2f/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"event": event, "ebs": ebs, "TV": TdepV}
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev1.dat'
	decdatFileToProcess = direc + '/decdat2.dat'
	interpSurfaceFileToProcess = direc + '/vT_vs_X_nnSORTED.out'
	data = loadtxt(fileToProcess)
	decdatdata = loadtxt(decdatFileToProcess)[:,[4,5]]	# vx, vy
	interpSurfaceData = loadtxt(interpSurfaceFileToProcess)	# tau, xT, vx, yT(==0), vy
	
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
	
	smoothtau = interpSurfaceData[:,0]
	smoothxT = interpSurfaceData[:,1]
	smoothvx = interpSurfaceData[:,2]
	smoothyT = interpSurfaceData[:,3]
	smoothvy = interpSurfaceData[:,4]
	
	smoothrT = sqrt(smoothxT**2 + smoothyT**2)
	smoothvT = sqrt(smoothvx**2 + smoothvy**2)
	
	# plot results
	#print min(avgS), max(avgS)
	#plt.scatter(rT, tau, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	#ax1.scatter(xT, yT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	#ax.scatter(xT, yT, s=50.0*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	#ax1.axis([xlower, xupper, ylower, yupper])
	#ax1.set_aspect('equal')
	#plt.colorbar()
	#fig1.show()

	#fig3 = plt.figure()
	#ax3 = fig3.add_axes([0.1,0.1,0.8,0.8])
	ax3 = fig1.add_subplot(211)
	ax3.plot(smoothrT, smoothtau, linestyle='-', color='black', linewidth=1.0)
	ax3.scatter(rT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	ax3.set_xticklabels([])
	ax3.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
	ax3.axis([rTlower, rTupper, taulower, tauupper])
	#ax3.set_aspect('equal')

	#fig2 = plt.figure()
	#ax2 = fig2.add_axes([0.1,0.1,0.8,0.8])
	ax2 = fig1.add_subplot(212, sharex=ax3)
	fig1.subplots_adjust(wspace=0.0, hspace=0.0)
	ax2.plot(smoothrT, smoothvT, linestyle='-', color='black', linewidth=1.0)
	ax2.scatter(rT, vT, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS))), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	ax2.set_xlabel(r'$r$ (fm)', {'fontsize': plotfontsize + 5})
	ax2.set_ylabel(r'$v_T/c$', {'fontsize': plotfontsize + 5, 'rotation': 90})
	ax2.axis([rTlower, rTupper, vTlower, vTupper])
	#ax2.set_aspect('equal')
	#fig2.show()
	KTstring = "%0.1f" % localpT
	outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_%(ebs)0.2f_TV%(TV)d.pdf' % {"ebs": ebs, "TV": TdepV}
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile
	fig1.show()
	#plt.savefig(outfile, format='pdf')
	print 'Generated', outfile
	


def generate_avgFOsurface_plots():
	# set-up
	plotfontsize = 18
	#fig = plt.figure()
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	rTlower, rTupper = -1.0, 10.0
	vTlower, vTupper = 0.0, 0.85
	taulower, tauupper = 0.0, 13.9
	
	#fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(12,12))
	fig, axs = plt.subplots(3, 2, sharex=True, sharey=True, figsize=(6,10))
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	for TVidx in xrange(1,3):
		# load data
		direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_%(ebs)0.2f/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"ebs": ebs, "TV": TVidx}
		fileToProcess = direc + '/averaged_S_on_FOsurface_ev1.dat'
		data = loadtxt(fileToProcess)
		pT = data[:,0]
		
		for KTidx in xrange(3):	# i.e., for KT = 0.0, 1.0, and 2.0 GeV
			# set-up data
			localpT = linspace(0,2,3)[KTidx]
			pTdataslice = data[(where(abs(pT-localpT) <= eps))[0]]
			pTdataslice = pTdataslice[pTdataslice[:,4].argsort()]
			tau = pTdataslice[:,1]
			xT = pTdataslice[:,2]
			yT = pTdataslice[:,3]
			avgS = pTdataslice[:,4]
			rT = sqrt(xT**2 + yT**2)
			
			# plot results
			#axs[TVidx-1, KTidx].scatter(rT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS))+0.01), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			#axs[TVidx-1, KTidx].scatter(rT, tau, s=10.0, c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			#axs[TVidx-1, KTidx].set_aspect('equal')
			#axs[TVidx-1, KTidx].axis([rTlower, rTupper, taulower, tauupper])
			#axs[TVidx-1, KTidx].text(0.1, 0.9,'%(ebsP)s, $K_T = $%(KTval)0.1f GeV' % {"ebsP": etaBYsParams[TVidx-1], "KTval": localpT}, transform=axs[TVidx-1, KTidx].transAxes, fontsize=plotfontsize - 5)
			#axs[KTidx, TVidx-1].scatter(rT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS))+0.01), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			axs[KTidx, TVidx-1].scatter(rT, tau, s=10.0, c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			#axs[KTidx, TVidx-1].set_aspect('equal')
			#axs[KTidx, TVidx-1].set(aspect=1.0)
			axs[KTidx, TVidx-1].axis([rTlower, rTupper, taulower, tauupper])
			axs[KTidx, TVidx-1].text(0.1, 0.9,'%(ebsP)s, $K_T = $%(KTval)0.1f GeV' % {"ebsP": etaBYsParams[TVidx-1], "KTval": localpT}, transform=axs[KTidx, TVidx-1].transAxes, fontsize=plotfontsize - 5)
			#if TVidx==2:
			#	axs[TVidx-1, KTidx].set_xlabel(r'$r$ (fm)', {'fontsize': plotfontsize + 5})
			#if KTidx==0:
			#	axs[TVidx-1, KTidx].set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
			if TVidx==1:
				axs[KTidx, TVidx-1].set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
			if KTidx==2:
				axs[KTidx, TVidx-1].set_xlabel(r'$r$ (fm)', {'fontsize': plotfontsize + 5})
			#ax1.axis([xlower, xupper, ylower, yupper])
			#ax1.set_aspect('equal')
			#plt.colorbar()
			#fig1.show()


	KTstring = "%0.1f" % localpT
	outfile = 'out.pdf'
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile
	fig.colorbar()
	fig.show()
	try:
		input("Press [enter] to continue...")
	except SyntaxError:
		pass
	#plt.savefig(outfile, format='pdf')
	#print 'Generated', outfile



def generate_avgFOsurface_plots2():
	# set-up
	plotfontsize = 18
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	rTlower, rTupper = -1.0, 10.0
	vTlower, vTupper = 0.0, 0.85
	taulower, tauupper = 0.0, 13.9
	
	fig, axs = plt.subplots(3, 2, sharex=True, sharey=True, figsize=(6,10))
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	for TVidx in xrange(1,3):
		# load data
		direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_%(ebs)0.2f/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"ebs": ebs, "TV": TVidx+2}
		fileToProcess = direc + '/averaged_S_on_FOsurface_ev1.dat'
		data = loadtxt(fileToProcess)
		pT = data[:,0]
		
		for KTidx in xrange(3):	# i.e., for KT = 0.0, 1.0, and 2.0 GeV
			# set-up data
			localpT = linspace(0,2,3)[KTidx]
			pTdataslice = data[(where(abs(pT-localpT) <= eps))[0]]
			pTdataslice = pTdataslice[pTdataslice[:,4].argsort()]
			tau = pTdataslice[:,1]
			xT = pTdataslice[:,2]
			yT = pTdataslice[:,3]
			avgS = pTdataslice[:,4]
			rT = sqrt(xT**2 + yT**2)
			
			# plot results
			im = axs[KTidx, TVidx-1].scatter(rT, tau, s=10.0, c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			axs[KTidx, TVidx-1].axis([rTlower, rTupper, taulower, tauupper])
			axs[KTidx, TVidx-1].text(0.1, 0.9,'%(ebsP)s, $K_T = $%(KTval)0.1f GeV' % {"ebsP": etaBYsParams[TVidx-1+2], "KTval": localpT}, transform=axs[KTidx, TVidx-1].transAxes, fontsize=plotfontsize - 5)
			if TVidx==1:
				axs[KTidx, TVidx-1].set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
			if KTidx==2:
				axs[KTidx, TVidx-1].set_xlabel(r'$r$ (fm)', {'fontsize': plotfontsize + 5})


	KTstring = "%0.1f" % localpT
	outfile = 'out.pdf'
	# Make an axis for the colorbar on the right side
	cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
	fig.colorbar(im, cax=cax)
	fig.show()
	try:
		input("Press [enter] to continue...")
	except SyntaxError:
		pass






if __name__ == "__main__":
	for KT in linspace(0,2,5):	# i.e., for KT = 0.0, 0.5, 1.0, 1.5, and 2.0 GeV
		for TVidx in range(5)[1:]:
			generate_FOsurface_plots(759, KT, TVidx)
			#try:
			#	input("Press [enter] to continue...")
			#except SyntaxError:
			#	pass
	#generate_avgFOsurface_plots2()



# End of file
