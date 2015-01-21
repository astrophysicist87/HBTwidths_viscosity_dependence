from math import *
import sys
from numpy import *
data = loadtxt(sys.argv[1])	#decdat2.dat

data=vstack((data[:,0],sqrt(data[:,4]**2+data[:,5]**2))).transpose()

FOcells = len(data[:,1])
nslices = 10
percentilestep = 100./nslices
binedges = [percentile(data[:,1], i*percentilestep) for i in range(nslices+1)]

for i in xrange(FOcells):
    if data[i,1] > binedges[-2]:
        print data[i,0]
