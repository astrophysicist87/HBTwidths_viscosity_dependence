#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid.inset_locator as inloc

def relf(a,b):
	return 100.*(a-b)/b

def generate_all_plots():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	cols = [1,3,5,9,13]	# KT, R2s, R2o, R2l, R2ol
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 3.5, 12.5
	pclower, pcupper = -10.0, 100.0
	
	ax1 = fig.add_subplot(221)
	#ax1inset = fig.add_axes([0.175, 0.55, relativesubplotsize, relativesubplotsize])
	#ax1inset = inloc.inset_axes(ax1, width="40%", height="40%", loc=1)
	
	ax1.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax1.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax1.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax1.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	#ax1inset.axhline(0.0, color='red', linewidth=2)
	#ax1inset.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=2)
	#ax1inset.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=2)
	#ax1inset.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	#ax1inset.axis([xlower, xupper, pclower, pcupper])
	#ax1inset.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	#ax1inset.set_ylabel(r'', {'fontsize': plotfontsize})
	#ax1inset.tick_params(labelsize=plotfontsize - 5)
	#ax1.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$\overline{R}^2_s$ (fm$^2\!$)', {'fontsize': plotfontsize + 5})
	ax1.text(0.85, 0.85,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	#ax1.legend(loc=1)
	# end of R2s
	
	# R2o
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 4.5, 32.5
	pclower, pcupper = -25.0, 25.0
	
	ax2 = fig.add_subplot(222)
	#ax2inset = fig.add_axes([0.65, 0.65, relativesubplotsize, relativesubplotsize])
	#ax2inset = inloc.inset_axes(ax2, width="40%", height="40%", loc=1)
	
	ax2.plot(LHLQdata[:,0], LHLQdata[:,2], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax2.plot(LHHQdata[:,0], LHHQdata[:,2], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax2.plot(HHLQdata[:,0], HHLQdata[:,2], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax2.plot(HHHQdata[:,0], HHHQdata[:,2], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	#ax2inset.axhline(0.0, color='red', linewidth=2)
	#ax2inset.plot(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdata[:,2]), linestyle=':', color='blue', linewidth=2)
	#ax2inset.plot(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdata[:,2]), linestyle='-.', color='black', linewidth=2)
	#ax2inset.plot(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdata[:,2]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	#ax2inset.axis([xlower, xupper, pclower, pcupper])
	#ax2inset.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	#ax2inset.set_ylabel(r'', {'fontsize': plotfontsize})
	#ax2inset.tick_params(labelsize=plotfontsize - 5)
	#ax2.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
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
	ylower, yupper = -0.5, 75.0
	pclower, pcupper = -40.0, 10.0
	
	ax3 = fig.add_subplot(223)
	#ax3inset = fig.add_axes([0.25, 0.25, relativesubplotsize, relativesubplotsize])
	#ax3inset = inloc.inset_axes(ax3, width="40%", height="40%", loc=1)
	
	ax3.plot(LHLQdata[:,0], LHLQdata[:,3], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax3.plot(LHHQdata[:,0], LHHQdata[:,3], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax3.plot(HHLQdata[:,0], HHLQdata[:,3], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax3.plot(HHHQdata[:,0], HHHQdata[:,3], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	#ax3inset.axhline(0.0, color='red', linewidth=2)
	#ax3inset.plot(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdata[:,3]), linestyle=':', color='blue', linewidth=2)
	#ax3inset.plot(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdata[:,3]), linestyle='-.', color='black', linewidth=2)
	#ax3inset.plot(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdata[:,3]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	#ax3inset.axis([xlower, xupper, pclower, pcupper])
	#ax3inset.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	#ax3inset.set_ylabel(r'', {'fontsize': plotfontsize})
	#ax3inset.tick_params(labelsize=plotfontsize - 5)
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$\overline{R}^2_l$ (fm$^2\!$)', {'fontsize': plotfontsize + 5})
	ax3.text(0.85, 0.85,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	
	#ax3.legend(loc=1)
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -0.5, 27.5
	pclower, pcupper = -20.0, 5.0
	
	ax4 = fig.add_subplot(224)
	#ax4inset = fig.add_axes([0.65, 0.25, relativesubplotsize, relativesubplotsize])
	#ax4inset = inloc.inset_axes(ax4, width="40%", height="40%", loc=1)
	
	ax4.plot(LHLQdata[:,0], -LHLQdata[:,4], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax4.plot(LHHQdata[:,0], -LHHQdata[:,4], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax4.plot(HHLQdata[:,0], -HHLQdata[:,4], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax4.plot(HHHQdata[:,0], -HHHQdata[:,4], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	#ax4inset.axhline(0.0, color='red', linewidth=2)
	#ax4inset.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,4],LHLQdata[:,4]), linestyle=':', color='blue', linewidth=2)
	#ax4inset.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,4],LHLQdata[:,4]), linestyle='-.', color='black', linewidth=2)
	#ax4inset.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,4],LHLQdata[:,4]), linestyle='--', color='green', linewidth=2)
	
	# update axes limits and axes labels
	ax4.axis([xlower, xupper, ylower, yupper])
	#ax4inset.axis([xlower, xupper, pclower, pcupper])
	#ax4inset.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize - 5})
	#ax4inset.set_ylabel(r'', {'fontsize': plotfontsize})
	#ax4inset.tick_params(labelsize=plotfontsize - 5)
	ax4.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax4.set_ylabel(r'$-\overline{R}^2_{ol}$ (fm$^2\!$)', {'fontsize': plotfontsize + 5, 'rotation': 90})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	ax4.text(0.85, 0.85,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	ax4.legend(loc='center right')
	# end of R2ol
	
	#plt.show()
	#plt.savefig('R2ijSSH_vs_TDEPVX_w_insets.pdf', format='pdf')
	plt.savefig('R2ijSSH_vs_TDEPVX.pdf', format='pdf')




if __name__ == "__main__":
	generate_all_plots()




# End of file
