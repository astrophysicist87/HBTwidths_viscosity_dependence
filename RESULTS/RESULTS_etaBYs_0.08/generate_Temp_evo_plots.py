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
contours = np.array([0.24, 0.18, 0.12])

def generate_Temp_evo_plots(event, TdepVX):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.5)
	
	# first plot
	ax1 = fig.add_subplot(211)
	data1=np.loadtxt('NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d/Temp_evoX.dat' % {"event": event, "TV": TdepVX})
	points=np.vstack((data1[:,1],data1[:,0])).T
	vals=data1[:,3]
	mintau=min(data1[:,0])
	maxtau=max(data1[:,0])
	minx=min(data1[:,1])
	maxx=max(data1[:,1])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax1)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax1.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax1.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax1.set_title('Temperature evolution for %(ebsP)s at $y=z=0$ fm (single event)' % {"ebsP": etaBYsParams[TdepVX-1]})
	
	# second plot
	ax2 = fig.add_subplot(212)
	data2=np.loadtxt('NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-%(event)d/Temp_evoY.dat' % {"event": event, "TV": TdepVX})
	points=np.vstack((data2[:,2],data2[:,0])).T
	vals=data2[:,3]
	mintau=min(data2[:,0])
	maxtau=max(data2[:,0])
	minx=min(data2[:,2])
	maxx=max(data2[:,2])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax2)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax2.set_xlabel(r'$y$ (fm)', {'fontsize': plotfontsize})
	ax2.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax2.set_title('Temperature evolution for %(ebsP)s at $x=z=0$ fm (single event)' % {"ebsP": etaBYsParams[TdepVX-1]})
	#plt.show()
	plt.savefig('Temp_V%(TV)d_evo_transition_ev%(event)d.pdf' % {"event": event, "TV": TdepVX}, format='pdf')
	print 'Generated Temp_V%(TV)d_evo_transition_ev%(event)d.pdf' % {"event": event, "TV": TdepVX}




def generate_Temp_evo_avg_plots(TdepVX):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.5)
	ax1 = fig.add_subplot(211)
	#data1=np.loadtxt('NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1/Temp_evo.dat' % {"TV": TdepVX})
	data1=np.loadtxt('/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1/Temp_evoX.dat' % {"TV": TdepVX})
	#points=np.vstack((data1[:,1],data1[:,0])).T	# x directions
	points=np.vstack((data1[:,1],data1[:,0])).T	# y directions
	vals=data1[:,3]		# temperature T(x=0,y,z=0,t)
	#vals=data1[:,4]		# Knudsen number Kn(x,y=0,z=0,t)
	setmaskarray=np.zeros(len(data1[:,4]))
	setmaskarray[np.where(data1[:,4] >= 10.0)]=1.0
	setmaskarray[np.where(data1[:,4] < 0.0)]=1.0
	maskedvals=ma.masked_array(vals, mask=setmaskarray)
	maskedvals
	mintau=min(data1[:,0])
	maxtau=max(data1[:,0])
	minx=min(data1[:,1])	# col=1 corresponds to x, col=2 correspond to y
	maxx=max(data1[:,1])	# col=1 corresponds to x, col=2 correspond to y
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	#grid_T = griddata(points, maskedvals, (grid_x, grid_tau), method=interpolationmethod)
	#print min(grid_T), max(grid_T)
	#grid_T[np.where(grid_T >= 10.0)] = np.nan
	#grid_T[np.where(grid_T < 0.0)] = np.nan
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax1)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	#cb.set_label(r'$Kn \equiv \frac{\eta\, \theta}{s\, T}$', fontsize=plotfontsize)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax1.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax1.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	#ax1.set_title('Knudsen number for %(ebsP)s at $y=z=0$ fm (SSH)' % {"ebsP": etaBYsParams[TdepVX-1]})
	ax1.set_title('Temperature profile for %(ebsP)s at $y=z=0$ fm (SSH)' % {"ebsP": etaBYsParams[TdepVX-1]})


	# second plot
	ax2 = fig.add_subplot(212)
	data2=np.loadtxt('/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V%(TV)d/NEW_TDEP_V%(TV)d_results-avg-1/Temp_evoY.dat' % {"TV": TdepVX})
	points=np.vstack((data2[:,2],data2[:,0])).T
	vals=data2[:,3]
	mintau=min(data2[:,0])
	maxtau=max(data2[:,0])
	minx=min(data2[:,2])
	maxx=max(data2[:,2])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax2)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax2.set_xlabel(r'$y$ (fm)', {'fontsize': plotfontsize})
	ax2.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax2.set_title('Temperature evolution for $(\eta/s)(T) = 0.00$ at $x=z=0$ fm (SSH)')


	#plt.show()
	plt.savefig('Temp_V%(TV)d_evo_transition_SSHavg.pdf' % {"TV": TdepVX}, format='pdf')
	#plt.savefig('KN_TdepV%(TV)d_evo_SSHavg.pdf' % {"TV": TdepVX}, format='pdf')
	print 'Generated Temp_V%(TV)d_evo_transition_SSHavg.pdf' % {"TV": TdepVX}


def generate_ideal_Temp_evo_plots(event):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.5)
	
	# first plot
	ax1 = fig.add_subplot(211)
	data1=np.loadtxt('../RESULTS_etaBYs_0.00/results-%(event)d/Temp_evoX.dat' % {"event": event})
	points=np.vstack((data1[:,1],data1[:,0])).T
	vals=data1[:,3]
	mintau=min(data1[:,0])
	maxtau=max(data1[:,0])
	minx=min(data1[:,1])
	maxx=max(data1[:,1])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax1)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax1.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax1.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax1.set_title('Ideal temperature evolution for $(\eta/s)(T) = 0.00$ at $y=z=0$ fm (single event)')
	
	# second plot
	ax2 = fig.add_subplot(212)
	data2=np.loadtxt('../RESULTS_etaBYs_0.00/results-%(event)d/Temp_evoY.dat' % {"event": event})
	points=np.vstack((data2[:,2],data2[:,0])).T
	vals=data2[:,3]
	mintau=min(data2[:,0])
	maxtau=max(data2[:,0])
	minx=min(data2[:,2])
	maxx=max(data2[:,2])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax2)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax2.set_xlabel(r'$y$ (fm)', {'fontsize': plotfontsize})
	ax2.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax2.set_title('Ideal temperature evolution for $(\eta/s)(T) = 0.00$ at $x=z=0$ fm (single event)')
	#plt.show()
	plt.savefig('ideal_Temp_evo_transition_ev%(event)d.pdf' % {"event": event}, format='pdf')
	print 'Generated ideal_Temp_evo_transition_ev%(event)d.pdf' % {"event": event}



def generate_ideal_Temp_evo_avg_plots():
	# set-up
	plotfontsize = 18
	interpolationmethod = 'cubic'
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.5)
	
	# first plot
	ax1 = fig.add_subplot(211)
	data1=np.loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/Temp_evoX.dat')
	points=np.vstack((data1[:,1],data1[:,0])).T
	vals=data1[:,3]
	mintau=min(data1[:,0])
	maxtau=max(data1[:,0])
	minx=min(data1[:,1])
	maxx=max(data1[:,1])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax1)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax1.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax1.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax1.set_title('Ideal temperature evolution for $(\eta/s)(T) = 0.00$ at $y=z=0$ fm (SSH)')
	
	# second plot
	ax2 = fig.add_subplot(212)
	data2=np.loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/Temp_evoY.dat')
	points=np.vstack((data2[:,2],data2[:,0])).T
	vals=data2[:,3]
	mintau=min(data2[:,0])
	maxtau=max(data2[:,0])
	minx=min(data2[:,2])
	maxx=max(data2[:,2])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=3, linestyles='--', levels=contours)
	divider = make_axes_locatable(ax2)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	cb.set_label(r'$T$ (GeV)', fontsize=plotfontsize)
	ax2.set_xlabel(r'$y$ (fm)', {'fontsize': plotfontsize})
	ax2.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	ax2.set_title('Ideal temperature evolution for $(\eta/s)(T) = 0.00$ at $x=z=0$ fm (SSH)')
	#plt.show()
	plt.savefig('ideal_Temp_evo_transition_SSH.pdf', format='pdf')
	print 'Generated ideal_Temp_evo_transition_SSH.pdf'


if __name__ == "__main__":
	#for TVidx in range(5)[1:]:
	#	generate_Temp_evo_plots(759, TVidx)
	#	generate_Temp_evo_avg_plots(TVidx)
	generate_ideal_Temp_evo_plots(759)
	generate_ideal_Temp_evo_avg_plots()



# End of file
