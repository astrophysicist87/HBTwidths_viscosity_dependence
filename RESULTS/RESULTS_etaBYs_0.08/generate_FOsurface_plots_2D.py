#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from sys import *
from scipy import interpolate
from subprocess import call

#ebs = sys.argv[1]

nevs = 1000
initialevent = 1
TdepV = 2

def generate_FOsurface_plots(event):
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = 0.0, 12.0
	
	# load data
	direc = 'NEW_TDEP_V4/NEW_TDEP_V4_results-%(event)d' % {"event": event}
	cols = [1, 2, 3, 11, 12]
	commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > NEW_TDEP_V4_generate_FOsurface_plots.temp'
	#print 'Running:', commandstring
	return_code = call(commandstring, shell=True)
	fileToProcess = 'NEW_TDEP_V4_generate_FOsurface_plots.temp'
	data = loadtxt(fileToProcess)[:,cols]
	
	# set-up data
	vT = sqrt(data[:,3]**2+data[:,4]**2)
	tau = data[:,0]
	xT = data[:,1]
	yT = data[:,2]
	rT = sqrt(xT**2 + yT**2)
	avT = arctanh(vT)
	
	# plot results
	plt.scatter(xT, tau, s=50.0, c=((avT-min(avT))/(max(avT)-min(avT))), alpha=0.5, edgecolor='')
	ax.axis([xlower, xupper, ylower, yupper])
	plt.colorbar()
	plt.show()
	#plt.savefig(direc + '/FOsurface.pdf', format='pdf')



def generate_avgFOsurface_plots():
	# set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	
	# set axes limits
	xlower, xupper = -10.0, 10.0
	ylower, yupper = 0.0, 12.0
	
	# load data
	direc = 'NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1' % {"TV": TdepV}
	cols = [1, 2, 3, 11, 12]
	commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > NEW_TDEP_V%(TV)d_generate_avgFOsurface_plots.temp' % {"TV": TdepV}
	#print 'Running:', commandstring
	return_code = call(commandstring, shell=True)
	fileToProcess = 'NEW_TDEP_V%(TV)d_generate_avgFOsurface_plots.temp' % {"TV": TdepV}
	data = loadtxt(fileToProcess)[:,cols]
	
	vT = sqrt(data[:,3]**2+data[:,4]**2)
	tau = data[:,0]
	xT = data[:,1]
	yT = data[:,2]
	rT = sqrt(xT**2 + yT**2)
	avT = arctanh(vT)
	
	# plot results
	plt.scatter(xT, tau, s=50.0, c=((avT-min(avT))/(max(avT)-min(avT))), alpha=0.5, edgecolor='')
	ax.axis([xlower, xupper, ylower, yupper])
	plt.colorbar()
	plt.show()
	#plt.savefig('NEW_TDEP_V%(TV)d/avg_FOsurface.pdf' % {"TV": TdepV}, format='pdf')







if __name__ == "__main__":
	#generate_FOsurface_plots(759)
	generate_avgFOsurface_plots()




####################################################################
########################### OLD STUFF ##############################
####################################################################

#nvTbins = 5
#ntaubins = 5
#minvT = min(vT) - eps
#maxvT = max(vT) + eps
#mintau = min(tau) - eps
#maxtau = max(tau) + eps
#vTbinedges = linspace(minvT, maxvT, nvTbins + 1)
#taubinedges = linspace(mintau, maxtau, ntaubins + 1)
#vTbincenters = delete(vTbinedges,-1) + (0.5*(maxvT-minvT)/nvTbins)
#taubincenters = delete(taubinedges,-1) + (0.5*(maxtau-mintau)/ntaubins)

#P, taubinedges, vTbinedges = np.histogram2d(tau, vT, bins=(taubinedges, vTbinedges))
#print P
#Ptau = array([sum(P[i,:]) for i in range(ntaubins)])
#PvT = array([sum(P[:,i]) for i in range(nvTbins)])
#print Ptau
#print PvT
#print sum(P.transpose())
#P /= sum(sum(P))
#P = P.transpose()
#print P
#print taubincenters
#print vTbincenters
#plt.hist2d(tau, vT, bins=[nvTbins, ntaubins])

#set axes limits
#xlower, xupper = min(data[:,1]), max(data[:,1])
#ylower, yupper = min(data[:,0]), max(data[:,0])

#plt.scatter(xT, tau, s=20.0, c=arctanh(vT), alpha=0.25, edgecolor='')
#plt.scatter(newdata[:,1], newdata[:,0], s=20.0, c='black', alpha=1.)
#meantau = array([sum(P[:,i]*taubincenters)/PvT[i] for i in range(nvTbins)])
#meantau2 = array([sum(P[:,i]*(taubincenters**2))/PvT[i] for i in range(nvTbins)])
#sig2tau = meantau2 - meantau**2
#print vTbincenters
#print meantau
#print meantau2
#print sqrt(sig2tau)

#tautau, vTvT = meshgrid(taubincenters, vTbincenters)
#print tautau
#print vTvT
#P = P.transpose()
#print P
#f = interpolate.interp2d(taubincenters, vTbincenters, P, kind='cubic')
#taunew = np.arange(mintau, maxtau, 1e-2)
#vTnew = np.arange(minvT, maxvT, 1e-2)
#Pnew = f(taunew, vTnew)
#print P.shape
#print Pnew.shape
#print taunew.shape
#plt.plot(vTnew, Pnew[:, -1], 'b-', vTbincenters, P[:, -1], 'r-')
#PvTnew = array([sum(Pnew[i,:]) for i in range(len(vTnew))])
#meantaunew = array([sum(Pnew[i,:]*taunew)/PvTnew[i] for i in range(len(vTnew))])
#meantau2new = array([sum(Pnew[i,:]*(taunew**2))/PvTnew[i] for i in range(len(vTnew))])
#sig2taunew = meantau2new - meantaunew**2
#print meantaunew
#print meantau2new
#print sqrt(sig2taunew)	

#update axes limits and axes labels
#ax.axis([xlower, xupper, ylower, yupper])
#ax.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize + 5})
#ax.set_ylabel(r'$\tau$ (fm/c)', {'fontsize': plotfontsize + 5})

#ax.legend(loc=1)

#plt.colorbar()
#plt.savefig('R2sSSH_vs_TDEPVX_w_inset.pdf', format='pdf')
#plt.show()


# End of file
