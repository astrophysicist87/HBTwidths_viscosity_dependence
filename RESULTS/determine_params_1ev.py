from math import *
import sys
from numpy import *

block = loadtxt(sys.argv[1])  #use decdat2.dat
block2 = loadtxt(sys.argv[2])  #use surface.dat
tau = block[:,0]
da0 = block[:,1]
da1 = block[:,2]
da2 = block[:,3]
vx = block[:,4]
vy = block[:,5]
xpt = block2[:,2]
ypt = block2[:,3]
vT = map(lambda x,y:x*x+y*y,vx,vy)
vT = [sqrt(i) for i in vT]  #this is the actual magnitude of the transverse fluid velocity
gammaT = map(lambda x:1./sqrt(1-x*x),vT)
measure = [gammaT[i] * (da0[i] + vx[i] * da1[i] + vy[i] * da2[i]) for i in range(len(gammaT))]
r = map(lambda x,y:x*x+y*y,xpt,ypt)
r = [sqrt(i) for i in r]  #this is the actual magnitude of the position vector in the transverse plane
#compute r^2 from FO surface
r2 = [i**2 for i in r]
r2_num_integ = [r2[i]*measure[i]*tau[i] for i in range(len(r2))]
r2_denom_integ = [measure[i]*tau[i] for i in range(len(r2))]
r2_num = sum(r2_num_integ)
r2_denom = sum(r2_denom_integ)
#compute vT^2 from FO surface
vT2 = [i**2 for i in vT]
vT2_num_integ = [vT2[i]*measure[i]*tau[i] for i in range(len(vT2))]
vT2_denom_integ = [measure[i]*tau[i] for i in range(len(vT2))]
vT2_num = sum(vT2_num_integ)
vT2_denom = sum(vT2_denom_integ)
#print "r^2:",r2_num/r2_denom
#print "vT^2:",vT2_num/vT2_denom
print r2_num/r2_denom, vT2_num/vT2_denom
