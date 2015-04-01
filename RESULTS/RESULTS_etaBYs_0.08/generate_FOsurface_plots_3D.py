#!/usr/bin/env python
from numpy import *
from numpy.linalg import norm
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
#TdepV = 1
dirs = ['RESULTS_etaBYs_0.00/results', 'RESULTS_etaBYs_0.08/NEW_TDEP_V1/NEW_TDEP_V1_results', 'RESULTS_etaBYs_0.20/results']
#dirs = ['RESULTS_etaBYs_0.00/results', 'RESULTS_etaBYs_0.08/NEW_TDEP_V1/NEW_TDEP_V1_results']
#dirs = ['RESULTS_etaBYs_0.00/results']
ebs = ['0.00', '0.08', '0.20']
ebss = ['0_00', '0_08', '0_20']
KTvec = [0.0, 1.0, 2.0]
scale = 5.0

def generate_FOsurface_plots(TdepV, event, localpT):
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
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d' % {"event": event, "TV": TdepV}
	#direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"TV": TdepV}
	#cols = [1, 2, 3, 11, 12]
	#commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > NEW_TDEP_V4_generate_FOsurface_plots_w_avgS_ev' + event + '.temp'
	#commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > generate_FOsurface_plots_w_avgS_ev' + str(event) + '.temp'
	#print 'Running:', commandstring
	#return_code = call(commandstring, shell=True)
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
	#fileToProcess = direc + '/averaged_S_on_FOsurface_ev1.dat'
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
	ax.view_init(elev=20, azim=135)
	#plt.colorbar()
	plt.show()
	KTstring = "%0.1f" % localpT
	outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_0.20.pdf'
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile




def generate_FOsurface_plots(event, localpT):
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	
	# load data
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.00/results-%(event)d' % {"event": event}
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
	data = loadtxt(fileToProcess)
	
	# set-up data
	pT = data[:,0]
	tau = data[(where(abs(pT-localpT) <= eps))[0],1]
	xT = data[(where(abs(pT-localpT) <= eps))[0],2]
	yT = data[(where(abs(pT-localpT) <= eps))[0],3]
	avgS = data[(where(abs(pT-localpT) <= eps))[0],4]
	norm = sum(avgS)
	rT = sqrt(xT**2 + yT**2)
	
	# plot results
	ax.scatter(xT, yT, tau, s=25.0*((avgS-min(avgS))/(max(avgS)-min(avgS)))+5.0, c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
	ax.axis([xlower, xupper, ylower, yupper])
	ax.view_init(elev=20, azim=135)
	#plt.colorbar()
	plt.show()
	KTstring = "%0.1f" % localpT
	#outfile = direc + '/FOsurface_w_avgS_KT_' + KTstring + '_etaBYs_0.20.pdf'
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile





def generate_FOsurface_plots(event):
	# set-up
	plotfontsize = 18
	#fig = plt.figure()
	#ax = fig.add_subplot(111, projection='3d')
	fig, axs = plt.subplots(len(dirs), len(KTvec), figsize=(10,7))
	fig.subplots_adjust(wspace=0.0, hspace=0.1)
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = -10.0, 10.0
	
	azimuth=135
	elevation=20
	rpt = 10
	xpt = rpt*cos(azimuth)*cos(elevation)
	ypt = rpt*sin(azimuth)*cos(elevation)
	taupt = rpt*sin(elevation)
	refpt = array([xpt, ypt, taupt])
	
	for diridx in xrange(len(dirs)):
		# load data
		direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/%(localdir)s-%(event)d' % {"localdir": dirs[diridx], "event": event}
		fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
		data = loadtxt(fileToProcess)
		
		for KTidx in xrange(len(KTvec)):
			# set-up data
			localpT = KTvec[KTidx]
			pT = data[:,0]
			pTdataslice = data[(where(abs(pT-localpT) <= eps))[0]]
			#pTdataslice = pTdataslice[norm((pTdataslice[:,[2,3,1]]-refpt),axis=1).argsort()[::-1]]
			pTdataslice = pTdataslice[pTdataslice[:,4].argsort()]
			tau = pTdataslice[:,1]
			xT = pTdataslice[:,2]
			yT = pTdataslice[:,3]
			avgS = pTdataslice[:,4]
			#norm = sum(avgS)
			rT = sqrt(xT**2 + yT**2)
			
			# plot results
			axs[diridx,KTidx] = fig.add_subplot(len(dirs), len(KTvec), len(dirs)*KTidx+diridx+1, projection='3d')
			axs[diridx,KTidx].scatter(xT, yT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS)))+1.0, c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
			axs[diridx,KTidx].axis([xlower, xupper, ylower, yupper])
			axs[diridx,KTidx].view_init(elev=elevation, azim=azimuth)
			axs[diridx,KTidx].set_xticks([-8.0,-4.0,0.0,4.0,8.0])
			axs[diridx,KTidx].set_yticks([-8.0,-4.0,0.0,4.0,8.0])
			axs[diridx,KTidx].set_xlabel('x (fm)', {'fontsize': plotfontsize-5})
			axs[diridx,KTidx].set_ylabel('y (fm)', {'fontsize': plotfontsize-5})
			#axs[diridx,KTidx].set_zlabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize-5})
			axs[diridx,KTidx].xaxis._axinfo['label']['space_factor'] = 2.8
			axs[diridx,KTidx].yaxis._axinfo['label']['space_factor'] = 2.8
			#axs[diridx,KTidx].zaxis._axinfo['label']['space_factor'] = 2.8
			axs[diridx,KTidx].w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
			axs[diridx,KTidx].w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
			axs[diridx,KTidx].w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
			axs[diridx,KTidx].w_xaxis.gridlines.set_color('black')
			axs[diridx,KTidx].w_yaxis.gridlines.set_color('black')
			axs[diridx,KTidx].w_zaxis.gridlines.set_color('black')
			axs[diridx,KTidx].set_aspect(1.0)
			axs[diridx,KTidx].text2D(-0.1, 0.9,'$\eta/s$ = %(ebs)s, $K_T = $%(KTval)0.1f GeV' % {"ebs": ebs[diridx], "KTval": localpT}, transform=axs[diridx,KTidx].transAxes, fontsize=plotfontsize - 5)
			if diridx==2:
				axs[diridx,KTidx].set_zlabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
				axs[diridx,KTidx].zaxis._axinfo['label']['space_factor'] = 2.8
			#plt.colorbar()
	

	
	#plt.tight_layout()
	#plt.show()
	#KTstring = "%0.1f" % localpT
	outfile = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/FOsurface_w_avgS_all.eps'
	plt.savefig(outfile, format='eps')
	#print 'Generated and saved', outfile




def generate_FOsurface_plots_for_dir(event, diridx):
	# set-up
	plotfontsize = 18
	#fig = plt.figure()
	#ax = fig.add_subplot(111, projection='3d')
	fig, axs = plt.subplots(len(KTvec), 1, figsize=(4,10))
	fig.subplots_adjust(wspace=0.0, hspace=0.1)
	
	# set axes limits
	#xlower, xupper = -10.0, 10.0
	#ylower, yupper = -10.0, 10.0
	xlower, xupper = -7.0, 7.0
	ylower, yupper = -7.0, 7.0
	
	azimuth=135
	#azimuth=315
	elevation=20
	rpt = 10
	xpt = rpt*cos(azimuth)*cos(elevation)
	ypt = rpt*sin(azimuth)*cos(elevation)
	taupt = rpt*sin(elevation)
	refpt = array([xpt, ypt, taupt])
	
	# load data
	direc = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/%(localdir)s-%(event)d' % {"localdir": dirs[diridx], "event": event}
	fileToProcess = direc + '/averaged_S_on_FOsurface_ev%(event)d.dat' % {"event": event}
	data = loadtxt(fileToProcess)
	
	for KTidx in xrange(len(KTvec)):
		# set-up data
		localpT = KTvec[KTidx]
		pT = data[:,0]
		pTdataslice = data[(where(abs(pT-localpT) <= eps))[0]]
		#pTdataslice = pTdataslice[norm((pTdataslice[:,[2,3,1]]-refpt),axis=1).argsort()[::-1]]
		pTdataslice = pTdataslice[pTdataslice[:,4].argsort()]
		tau = pTdataslice[:,1]
		xT = pTdataslice[:,2]
		yT = pTdataslice[:,3]
		avgS = pTdataslice[:,4]
		#norm = sum(avgS)
		rT = sqrt(xT**2 + yT**2)
		
		# plot results
		axs[KTidx] = fig.add_subplot(len(KTvec), 1, KTidx+1, projection='3d')
		#axs[KTidx].scatter(xT, yT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS)))+2.5, c=log(0.1+(avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=0.5, edgecolor='')
		axs[KTidx].scatter(xT, yT, tau, s=scale*((avgS-min(avgS))/(max(avgS)-min(avgS)))+2.5, c=(avgS-min(avgS))/(max(avgS)-min(avgS)), alpha=0.5, edgecolor='')
		axs[KTidx].axis([xlower, xupper, ylower, yupper])
		axs[KTidx].view_init(elev=elevation, azim=azimuth)
		#axs[KTidx].set_xticks([-8.0,-4.0,0.0,4.0,8.0])
		#axs[KTidx].set_yticks([-8.0,-4.0,0.0,4.0,8.0])
		axs[KTidx].set_xticks([-6.0,-3.0,0.0,3.0,6.0])
		axs[KTidx].set_yticks([-6.0,-3.0,0.0,3.0,6.0])
		axs[KTidx].set_xlabel('x (fm)', {'fontsize': plotfontsize-5})
		axs[KTidx].set_ylabel('y (fm)', {'fontsize': plotfontsize-5})
		#axs[KTidx].set_zlabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize-5})
		axs[KTidx].xaxis._axinfo['label']['space_factor'] = 2.8
		axs[KTidx].yaxis._axinfo['label']['space_factor'] = 2.8
		#axs[KTidx].zaxis._axinfo['label']['space_factor'] = 2.8
		axs[KTidx].w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
		axs[KTidx].w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
		axs[KTidx].w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
		axs[KTidx].w_xaxis.gridlines.set_color('black')
		axs[KTidx].w_yaxis.gridlines.set_color('black')
		axs[KTidx].w_zaxis.gridlines.set_color('black')
		axs[KTidx].set_aspect(1.0)
		axs[KTidx].text2D(0.05, 0.9,'$\eta/s$ = %(ebs)s, $K_T = $%(KTval)0.1f GeV' % {"ebs": ebs[diridx], "KTval": localpT}, transform=axs[KTidx].transAxes, fontsize=plotfontsize - 5)
		if diridx==2:
			axs[KTidx].set_zlabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize, 'rotation': 90})
			axs[KTidx].zaxis._axinfo['label']['space_factor'] = 2.8
		#plt.colorbar()
	

	
	#plt.tight_layout()
	plt.show()
	#outfile = '/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/FOsurface_w_avgS_ebs_%(ebs)s.pdf' % {"ebs": ebss[diridx]}
	#plt.savefig(outfile, format='pdf')
	#print 'Generated and saved', outfile




if __name__ == "__main__":
	#for KT in linspace(0,2,5):
		#generate_FOsurface_plots(1, 759, KT)
		#generate_FOsurface_plots(759, KT)
	#for TVidx in range(5)[1:]:
	#	generate_FOsurface_plots(TVidx, 759, 0.0)
	#generate_FOsurface_plots(1, 759, 0.0)
	for diridx in xrange(len(dirs)):
		generate_FOsurface_plots_for_dir(759, diridx)



# End of file
