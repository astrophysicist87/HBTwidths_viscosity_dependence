#!/usr/bin/env python
import numpy as np
import scipy.ndimage.interpolation as sni
import glob
from numpy.linalg import det

nevs = 1000
rotateorder=2.
randomrotate=False

if randomrotate:
	anglerange=360.
else:
	anglerange=0.

anglemin=0.

gridsize = 261
dx, dy = 0.1, 0.1
xmin, ymin = -13.0, -13.0
xmax, ymax = 13.0, 13.0

xpts = np.linspace(xmin, xmax, gridsize)
ypts = np.linspace(ymin, ymax, gridsize)
xgrid, ygrid = np.meshgrid(xpts, ypts)
#r2 = np.sqrt(xgrid**2+ygrid**2)
#phi = np.arctan2(ygrid,xgrid)
#exp2iphi = np.exp((2.j)*phi)

def xbar(data):
	return np.sum(xgrid*data)

def ybar(data):
	return np.sum(ygrid*data)

def r2(data,xbar,ybar):
	return (xgrid-xbar)**2+(ygrid-ybar)**2

def exp2iphi(data,xbar,ybar):
	return np.exp((rotateorder*(1j))*(np.arctan2(ygrid-ybar,xgrid-xbar)))

def get_eccentricity_phase(data):
	xbar, ybar = xbar(data), ybar(data)
	r2 = r2(data,xbar,ybar)
	exp2iphi = exp2iphi(data,xbar,ybar)
	return np.angle(-np.sum(r2*exp2iphi*data)/np.sum(r2*data))/rotateorder


#filename=glob.glob('/home/plumberg.1/HBTwidths_viscosity_dependence/ICs/results-1/sd*dat')[0]
#sumdata=np.loadtxt(filename)
sumdata=np.zeros([gridsize,gridsize])
#print 'Opened results-1/sd*dat'

for i in xrange(1,nevs+1):
	filename=glob.glob('/home/plumberg.1/HBTwidths_viscosity_dependence/ICs/results-%(ev)d/sd*dat' % {"ev": i})[0]
	data=np.loadtxt(filename)
	#print sum(sum(np.loadtxt(filename))), sum(sum(sni.rotate(np.loadtxt(filename), anglerange*np.random.random_sample()+anglemin,reshape=False,order=0)))
	if rotateorder != 0:
		angle = get_eccentricity_phase(data)
	else:
		angle = anglerange*np.random.random_sample()+anglemin
	#print angle
	sumdata+=sni.rotate(data, np.rad2deg(angle), reshape=False, order=0)
	print 'Included results-%(ev)d/sd*dat' % {"ev": i}



sumdata/=float(nevs)
np.savetxt('/home/plumberg.1/HBTwidths_viscosity_dependence/ICs/results-avg-rotated/sd_shifted_and_rotated_w_ecc_phases_avg_1000evs_block.dat', sumdata, fmt='%0.9f')
#np.savetxt('/home/plumberg.1/HBTwidths_viscosity_dependence/ICs/results-avg/sd_avg_1000evs_block.dat', sumdata, fmt='%0.9f')

# End of file