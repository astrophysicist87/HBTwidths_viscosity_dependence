#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid.inset_locator as inloc

mpi = 0.13957
#df_stem = ''
df_stem = '_no_df'
abs_stem = ''
#abs_stem = '_w_abs'
#neq_stem = ''
neq_stem = '_COSneq0'
eps = 1.e-15

def relf(a,b):
	return 100.*(a-b)/b

def bT(kT):
	return kT/sqrt(mpi**2+kT**2)
	#return 1.

def plot_relative_sigmas():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	#cols = [0,1,2,3,4,11,12,13,14]		# KT, R2s, R2o, R2l, R2ol, sig^2_s, sig^2_o, sig^2_l, sig^2_ol, in that order
	cols = [0,1,2,4,6,17,18,20,22]		# KT, R2s, R2o, R2l, R2ol, sig^2_s, sig^2_o, sig^2_l, sig^2_ol, in that order
	R2oscols = [0,3,19]			# KT, R2os, sig^2_{os}
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	idealdata=loadtxt('../RESULTS_etaBYs_0.00/complete_FOsurface_properties_etaBYs_0.00_1000evs' + neq_stem + '_no_df' + abs_stem + '.dat')[:,cols]
	LHLQdata=loadtxt('../RESULTS_etaBYs_LHLQ/complete_FOsurface_properties_etaBYs_LHLQ_1000evs' + neq_stem + df_stem + '.dat')[:,cols]
	LHHQdata=loadtxt('../RESULTS_etaBYs_LHHQ/complete_FOsurface_properties_etaBYs_LHHQ_1000evs' + neq_stem + df_stem + '.dat')[:,cols]
	HHLQdata=loadtxt('../RESULTS_etaBYs_HHLQ/complete_FOsurface_properties_etaBYs_HHLQ_1000evs' + neq_stem + df_stem + '.dat')[:,cols]
	HHHQdata=loadtxt('../RESULTS_etaBYs_HHHQ/complete_FOsurface_properties_etaBYs_HHHQ_1000evs' + neq_stem + df_stem + '.dat')[:,cols]

	#R2os files
	idealR2osdata=loadtxt('../RESULTS_etaBYs_0.00/complete_FOsurface_properties_etaBYs_0.00_1000evs' + '_SINneq2' + '_no_df' + abs_stem + '.dat')[:,R2oscols]
	LHLQR2osdata=loadtxt('../RESULTS_etaBYs_LHLQ/complete_FOsurface_properties_etaBYs_LHLQ_1000evs' + '_SINneq2' + df_stem + '.dat')[:,R2oscols]
	LHHQR2osdata=loadtxt('../RESULTS_etaBYs_LHHQ/complete_FOsurface_properties_etaBYs_LHHQ_1000evs' + '_SINneq2' + df_stem + '.dat')[:,R2oscols]
	HHLQR2osdata=loadtxt('../RESULTS_etaBYs_HHLQ/complete_FOsurface_properties_etaBYs_HHLQ_1000evs' + '_SINneq2' + df_stem + '.dat')[:,R2oscols]
	HHHQR2osdata=loadtxt('../RESULTS_etaBYs_HHHQ/complete_FOsurface_properties_etaBYs_HHHQ_1000evs' + '_SINneq2' + df_stem + '.dat')[:,R2oscols]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99-1., 1.15-1.
	#ylower, yupper = 1.07, 1.12
	pclower, pcupper = -10.0, 100.0
	
	ax1 = fig.add_subplot(221)
	
	ax1.axhline(0.0, color='black', linewidth=1)
	ax1.plot(idealdata[:,0], sqrt(idealdata[:,5])/idealdata[:,1], linestyle='solid', color='black', linewidth=2, label='ideal')
	ax1.plot(LHLQdata[:,0], sqrt(LHLQdata[:,5])/LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax1.plot(LHHQdata[:,0], sqrt(LHHQdata[:,5])/LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax1.plot(HHLQdata[:,0], sqrt(HHLQdata[:,5])/HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax1.plot(HHHQdata[:,0], sqrt(HHHQdata[:,5])/HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$\sigma_s / \left< R^2_s \!\right>$', {'fontsize': plotfontsize + 5})
	ax1.text(0.05, 0.15,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	# end of R2s
	
	# R2o
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99-1., 1.2-1.
	pclower, pcupper = -25.0, 25.0
	
	ax2 = fig.add_subplot(222)
	
	ax2.axhline(0.0, color='black', linewidth=1)
	ax2.plot(idealdata[:,0], sqrt(idealdata[:,6])/idealdata[:,2], linestyle='solid', color='black', linewidth=2, label='ideal')
	ax2.plot(LHLQdata[:,0], sqrt(LHLQdata[:,6])/LHLQdata[:,2], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax2.plot(LHHQdata[:,0], sqrt(LHHQdata[:,6])/LHHQdata[:,2], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax2.plot(HHLQdata[:,0], sqrt(HHLQdata[:,6])/HHLQdata[:,2], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax2.plot(HHHQdata[:,0], sqrt(HHHQdata[:,6])/HHHQdata[:,2], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	ax2.set_xticklabels([])
	ax2.set_ylabel(r'$\sigma_o / \left< R^2_o \!\right>$', {'fontsize': plotfontsize + 5})
	ax2.yaxis.set_label_position('right')
	ax2.yaxis.tick_right()
	ax2.yaxis.set_ticks_position('both')
	ax2.text(0.05, 0.15,'(b)', transform=ax2.transAxes, fontsize=plotfontsize + 5)
	ax2.legend(loc='best')
	
	# end of R2o
	
	# R2l
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.99-1., 0.15
	pclower, pcupper = -40.0, 10.0
	
	ax3 = fig.add_subplot(223)
	
	ax3.axhline(0.0, color='black', linewidth=1)
	ax3.plot(idealdata[:,0], sqrt(idealdata[:,7])/idealdata[:,3], linestyle='solid', color='black', linewidth=2, label='ideal')
	ax3.plot(LHLQdata[:,0], sqrt(LHLQdata[:,7])/LHLQdata[:,3], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax3.plot(LHHQdata[:,0], sqrt(LHHQdata[:,7])/LHHQdata[:,3], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax3.plot(HHLQdata[:,0], sqrt(HHLQdata[:,7])/HHLQdata[:,3], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax3.plot(HHHQdata[:,0], sqrt(HHHQdata[:,7])/HHHQdata[:,3], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$\sigma_l / \left< R^2_l \!\right>$', {'fontsize': plotfontsize + 5})
	ax3.text(0.05, 0.15,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -0.005, 0.085
	pclower, pcupper = -20.0, 5.0
	
	ax4 = fig.add_subplot(224)
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax4.axhline(0.0, color='black', linewidth=1)
	ax4.plot(idealR2osdata[:,0], sqrt(idealR2osdata[:,2])/(idealdata[:,1]+eps), linestyle='solid', color='black', linewidth=2, label='ideal')
	ax4.plot(LHLQR2osdata[:,0], sqrt(LHLQR2osdata[:,2])/(LHLQdata[:,1]+eps), linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax4.plot(LHHQR2osdata[:,0], sqrt(LHHQR2osdata[:,2])/(LHHQdata[:,1]+eps), linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax4.plot(HHLQR2osdata[:,0], sqrt(HHLQR2osdata[:,2])/(HHLQdata[:,1]+eps), linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax4.plot(HHHQR2osdata[:,0], sqrt(HHHQR2osdata[:,2])/(HHHQdata[:,1]+eps), linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	# update axes limits and axes labels
	ax4.axis([xlower, xupper, ylower, yupper])
	ax4.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax4.set_ylabel(r'$\sigma_{os,2} / \left< R^2_{os,2} \right>$', {'fontsize': plotfontsize + 5, 'rotation': 90})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	ax4.text(0.05, 0.15,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	#ax4.legend(loc=4)
	
	# end of R2os
	
	#plt.show()
	plt.savefig('R2ij_relsig_DEA_vs_TDEPVX' + df_stem + abs_stem + '.pdf', format='pdf')






if __name__ == "__main__":
	plot_relative_sigmas()





# End of file
