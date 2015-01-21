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
#cols=[0,1,9,10,11,12,13,14,15]
cols=[0,1,9]


def generate_Temp_evo_avg_plots(TdepVX):
	# set-up
	plotfontsize = 18
	interpolationmethod = 'nearest'
	fig = plt.figure()
	ax = fig.add_subplot(111)
	data=np.loadtxt('/home/plumberg.1/HBTwidths_viscosity_dependence/PlayGround/copy10/VISHNew/TV%(TV)d_results-smooth/TV%(TV)d_OSCAR_y_eq_0.dat' % {"TV": TdepVX})[:20880,cols]
	data[:,0] = 0.02*data[:,0]+0.6
	data[:,1] = 0.1*data[:,1]-13.0
	points=np.vstack((data[:,1],data[:,0])).T
	vals=data[:,2]
	mintau=min(data[:,0])
	maxtau=max(data[:,0])
	minx=min(data[:,1])
	maxx=max(data[:,1])
	npts=1000
	grid_x, grid_tau = np.mgrid[minx:maxx:npts*(1j), mintau:maxtau:npts*(1j)]
	grid_T = griddata(points, vals, (grid_x, grid_tau), method=interpolationmethod)
	#print np.arange(0.2,max(vals),0.01)
	cs=plt.imshow(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower')
	plt.contour(grid_T.T, extent=(minx,maxx,mintau,maxtau), origin='lower', colors='black', linewidths=1, linestyles='solid', levels=np.arange(-max(vals),max(vals),max(vals)/5.))
	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	cb = plt.colorbar(cs, orientation = 'vertical', cax=cax)
	#ax.set_aspect(100.0)
	cb.set_label(r'$\pi_{12}$', fontsize=plotfontsize)
	ax.set_xlabel(r'$x$ (fm)', {'fontsize': plotfontsize})
	ax.set_ylabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize})
	plt.show()



if __name__ == "__main__":
	generate_Temp_evo_avg_plots(1)
	generate_Temp_evo_avg_plots(2)



# End of file
