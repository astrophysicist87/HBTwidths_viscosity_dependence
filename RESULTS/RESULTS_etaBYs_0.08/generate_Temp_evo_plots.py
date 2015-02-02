#!/usr/bin/env python
import numpy as np
#from pylab import *
import matplotlib.pyplot as plt
#from sys import *
from scipy.interpolate import griddata
#from subprocess import call
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy.ma as ma

#ebs = sys.argv[1]

#nevs = 1000
#initialevent = 1
etaBYsParams = ['LH-LQ', 'LH-HQ', 'HH-LQ', 'HH-HQ']

def generate_Temp_evo_plots(event, TdepVX):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	ax = fig.add_subplot(111)
	data=np.loadtxt('NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d/Temp_evo.dat' % {"event": event, "TV": TdepVX})
	points=np.vstack((data[:,1],data[:,0])).T
	vals=data[:,3]
	mintau=min(data[:,0])
	maxtau=max(data[:,0])
	minx=min(data[:,1])
	maxx=max(data[:,1])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=np.array([0.18]))
	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax.set_title('Temperature evolution for %(ebsP)s at $y=z=0$ fm (single event)' % {"ebsP": etaBYsParams[TdepVX-1]})
	#plt.show()
	plt.savefig('Temp_V%(TV)d_evo_transition_ev%(event)d.pdf' % {"event": event, "TV": TdepVX}, format='pdf')
	print 'Generated Temp_V%(TV)d_evo_transition_ev%(event)d.pdf' % {"event": event, "TV": TdepVX}




def generate_Temp_evo_avg_plots(TdepVX):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	ax = fig.add_subplot(111)
	#data=np.loadtxt('NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1/Temp_evo.dat' % {"TV": TdepVX})
	data=np.loadtxt('/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1/Temp_evoY.dat' % {"TV": TdepVX})
	#points=np.vstack((data[:,1],data[:,0])).T	# x directions
	points=np.vstack((data[:,2],data[:,0])).T	# y directions
	vals=data[:,3]		# temperature T(x=0,y,z=0,t)
	#vals=data[:,4]		# Knudsen number Kn(x,y=0,z=0,t)
	setmaskarray=np.zeros(len(data[:,4]))
	setmaskarray[np.where(data[:,4] >= 10.0)]=1.0
	setmaskarray[np.where(data[:,4] < 0.0)]=1.0
	maskedvals=ma.masked_array(vals, mask=setmaskarray)
	maskedvals
	mintau=min(data[:,0])
	maxtau=max(data[:,0])
	minx=min(data[:,2])	# col=1 corresponds to x, col=2 correspond to y
	maxx=max(data[:,2])	# col=1 corresponds to x, col=2 correspond to y
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	#grid_T = griddata(points, maskedvals, (grid_x, grid_tau), method=interpolationmethod)
	#print min(grid_T), max(grid_T)
	#grid_T[np.where(grid_T >= 10.0)] = np.nan
	#grid_T[np.where(grid_T < 0.0)] = np.nan
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=np.array([0.18]))
	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	#cb.set_label(r'$Kn \equiv \frac{\eta\, \theta}{s\, T}$', fontsize=plotfontsize)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax.set_xlabel(r'$y$ (fm)', {'fontsize': plotfontsize})
	ax.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	#ax.set_title('Knudsen number for %(ebsP)s at $y=z=0$ fm (SSH)' % {"ebsP": etaBYsParams[TdepVX-1]})
	ax.set_title('Temperature profile for %(ebsP)s at $x=z=0$ fm (SSH)' % {"ebsP": etaBYsParams[TdepVX-1]})
	#plt.show()
	plt.savefig('Temp_V%(TV)d_evo_transition_SSHavg.pdf' % {"TV": TdepVX}, format='pdf')
	#plt.savefig('KN_TdepV%(TV)d_evo_SSHavg.pdf' % {"TV": TdepVX}, format='pdf')
	print 'Generated Temp_V%(TV)d_evo_transition_SSHavg.pdf' % {"TV": TdepVX}



if __name__ == "__main__":
	for TVidx in range(5)[1:]:
		generate_Temp_evo_plots(759, TVidx)
		#generate_Temp_evo_avg_plots(TVidx)



# End of file
