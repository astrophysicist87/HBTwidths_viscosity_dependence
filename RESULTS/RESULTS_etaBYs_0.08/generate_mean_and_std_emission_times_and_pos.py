
m numpy import *
from pylab import *
import matplotlib.pyplot as plt
from sys import *
from scipy import interpolate
from subprocess import call

ebs = sys.argv[1]

nevs = 1000
initialevent = 1

def generate_flow_contour_plots(event):
	#set-up
	#plotfontsize = 18
	#fig = plt.figure()
	#ax = fig.add_axes([0.1,0.1,0.85,0.85])
	
	# load data
	direc = 'results-%(event)d' % {"event": event}
	cols = [1, 2, 3, 11, 12]
	commandstring = 'paste ' + direc + '/surface.dat ' + direc + '/decdat2.dat > temp.dat'
	#print 'Running:', commandstring
	return_code = call(commandstring, shell=True)
	fileToProcess = 'temp.dat'
	data = loadtxt(fileToProcess)[:,cols]
	
	vT = sqrt(data[:,3]**2+data[:,4]**2)
	tau = data[:,0]
	xT = data[:,1]
	yT = data[:,2]
	rT = sqrt(xT**2 + yT**2)
	
	cutoff = percentile(arctanh(vT),75)
	#cutoff = percentile(vT,50.78)
	#newdata = (vstack((tau, xT, yT, rT, vT, arctanh(vT))).transpose())[where(arctanh(vT) >= cutoff),:][0]
	newdata = (vstack((tau, rT)).transpose())[where(arctanh(vT) >= cutoff),:][0]
	#newdata = (vstack((tau, xT, yT, rT, vT, arctanh(vT))).transpose())[where(vT >= cutoff),:][0]
	#print mean(newdata[:,0])
	#print std(newdata[:,0])
	#return_code = call('rm temp.dat', shell=True)
	return array([[mean(newdata[:,0]), var(newdata[:,0]), mean(newdata[:,1]), var(newdata[:,1])]])







if __name__ == "__main__":
	results = generate_flow_contour_plots(initialevent)
	print 'Finished processing event 1'
	
	for ev in xrange(initialevent + 1, initialevent + nevs):
		results = append(results, generate_flow_contour_plots(ev), axis=0)
		#print results
		print 'Finished processing event', ev
	
	savetxt('mean_and_std_emission_times_and_pos_etaBYs_%(ebs)s.dat' % {"ebs": ebs}, results)
	print 'Finished all.'




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
