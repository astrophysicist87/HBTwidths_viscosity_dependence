from math import *
import sys
from numpy import *

block = loadtxt(sys.argv[1])
xgrid = linspace(-13,13,261)
ygrid = linspace(-13,13,261)

x2sum=0
y2sum=0
sum=0

for i in xrange(261):
	for j in xrange(261):
		x2sum+=xgrid[i]**2*block[i,j]
		y2sum+=ygrid[j]**2*block[i,j]
		sum+=block[i,j]

x2avg=x2sum/sum
y2avg=y2sum/sum
#Rbar=1./sqrt((1./x2avg) + (1./y2avg))
#Rbar=0.5*sqrt(r2avg)

print 0.5*sqrt(x2avg+y2avg)
