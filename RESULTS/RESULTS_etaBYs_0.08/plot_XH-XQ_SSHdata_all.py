#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid.inset_locator as inloc

#df_stem = ''
df_stem = '_no_df'
#neq_stem = ''
neq_stem = '_neq0'

def relf(a,b):
	return 100.*(a-b)/b

def generate_all_plots():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	cols = [1,3,5,9,13]	# KT, R2s, R2o, R2l, R2ol
	R2oscols = [1,8]	# KT, R2os (picks out column of sine coefficients)
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	idealdata=loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/HBTradii_cfs_ev1_no_df.dat_neqn_cfs_0')[:,cols]
	LHLQdata=loadtxt('../RESULTS_etaBYs_LHLQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_0')[:,cols]
	LHHQdata=loadtxt('../RESULTS_etaBYs_LHHQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_0')[:,cols]
	HHLQdata=loadtxt('../RESULTS_etaBYs_HHLQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_0')[:,cols]
	HHHQdata=loadtxt('../RESULTS_etaBYs_HHHQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_0')[:,cols]

	#R2os files
	idealR2osdata=loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/HBTradii_cfs_ev1_no_df.dat_neqn_cfs_2')[:,R2oscols]
	LHLQR2osdata=loadtxt('../RESULTS_etaBYs_LHLQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_2')[:,R2oscols]
	LHHQR2osdata=loadtxt('../RESULTS_etaBYs_LHHQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_2')[:,R2oscols]
	HHLQR2osdata=loadtxt('../RESULTS_etaBYs_HHLQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_2')[:,R2oscols]
	HHHQR2osdata=loadtxt('../RESULTS_etaBYs_HHHQ/results-avg-1/HBTradii_cfs_ev1' + df_stem + '.dat_neqn_cfs_2')[:,R2oscols]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 2.5, 13.0
	pclower, pcupper = -10.0, 100.0
	
	ax1 = fig.add_subplot(221)
	#ax1inset = fig.add_axes([0.175, 0.55, relativesubplotsize, relativesubplotsize])
	#ax1inset = inloc.inset_axes(ax1, width="40%", height="40%", loc=1)

	#ax1.plot(idealdata2[:,0], idealdata2[:,1]+0.1, linestyle='solid', color='blue', linewidth=2, label='ideal2')	
	ax1.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax1.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax1.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax1.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	ax1.plot(idealdata[:,0], idealdata[:,1], linestyle='solid', color='black', linewidth=1, label='ideal')	
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$\overline{R}^2_s$ (fm$^2\!$)', {'fontsize': plotfontsize + 5})
	ax1.text(0.85, 0.85,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	#ax1.legend(loc=1)
	# end of R2s
	
	# R2o
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 4.0, 33.5
	pclower, pcupper = -25.0, 25.0
	
	ax2 = fig.add_subplot(222)
	
	ax2.plot(LHLQdata[:,0], LHLQdata[:,2], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax2.plot(LHHQdata[:,0], LHHQdata[:,2], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax2.plot(HHLQdata[:,0], HHLQdata[:,2], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax2.plot(HHHQdata[:,0], HHHQdata[:,2], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	ax2.plot(idealdata[:,0], idealdata[:,2], linestyle='solid', color='black', linewidth=1, label='ideal')	
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	ax2.set_xticklabels([])
	ax2.set_ylabel(r'$\overline{R}^2_o$ (fm$^2\!$)', {'fontsize': plotfontsize + 5})
	ax2.yaxis.set_label_position('right')
	ax2.yaxis.tick_right()
	ax2.yaxis.set_ticks_position('both')
	ax2.text(0.85, 0.85,'(b)', transform=ax2.transAxes, fontsize=plotfontsize + 5)
	
	#ax2.legend(loc=1)
	# end of R2o
	
	# R2l
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -0.5, 159.0
	pclower, pcupper = -40.0, 10.0
	
	ax3 = fig.add_subplot(223)
	
	ax3.plot(LHLQdata[:,0], LHLQdata[:,3], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax3.plot(LHHQdata[:,0], LHHQdata[:,3], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax3.plot(HHLQdata[:,0], HHLQdata[:,3], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax3.plot(HHHQdata[:,0], HHHQdata[:,3], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	ax3.plot(idealdata[:,0], idealdata[:,3], linestyle='solid', color='black', linewidth=1, label='ideal')	
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$\overline{R}^2_l$ (fm$^2\!$)', {'fontsize': plotfontsize + 5})
	ax3.text(0.85, 0.1,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	ax3.legend(loc='upper center')
	
	#ax3.legend(loc=1)
	# end of R2l
	
	# R2os
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -0.01, 0.65
	pclower, pcupper = -20.0, 5.0
	
	ax4 = fig.add_subplot(224)

	ax4.plot(LHLQR2osdata[:,0], LHLQR2osdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax4.plot(LHHQR2osdata[:,0], LHHQR2osdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax4.plot(HHLQR2osdata[:,0], HHLQR2osdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax4.plot(HHHQR2osdata[:,0], HHHQR2osdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	ax4.plot(idealR2osdata[:,0], idealR2osdata[:,1], linestyle='solid', color='black', linewidth=1, label='ideal')	
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	# update axes limits and axes labels
	ax4.axis([xlower, xupper, ylower, yupper])
	ax4.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax4.set_ylabel(r'$\overline{R}^2_{os,2}$ (fm$^2\!$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	ax4.text(0.85, 0.1,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	#ax4.legend(loc='center right')
	# end of R2ol
	
	#plt.show()
	plt.savefig('R2ijSSH_vs_TDEPVX' + df_stem + '.pdf', format='pdf')




if __name__ == "__main__":
	generate_all_plots()




# End of file
