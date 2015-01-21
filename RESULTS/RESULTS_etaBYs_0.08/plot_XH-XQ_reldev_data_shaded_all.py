#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid.inset_locator as inloc
import matplotlib as mpl

mpl.rcParams['pdf.fonttype'] = 42

def relf(a,b):
	return 100.*(a-b)/b

def generate_all_plots():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	cols1 = [1,3,5,9,13]	# KT, R2s, R2o, R2l, R2ol (SSH)
	cols2 = [0,1,2,3,4]	# KT, R2s, R2o, R2l, R2ol (DEA)
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -10.0, 85.0
	
	ax1 = fig.add_subplot(221)
	
	ax1.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax1.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax1.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax1.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax1.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax1.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax1.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax1.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='blue', alpha='0.05')
	ax1.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')
	ax1.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$R^2_{s}/\left( R^2_{s} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize})
	ax1.text(0.05, 0.85,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	# end of R2s
	
	# R2o
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -32.0, 20.0
	
	ax2 = fig.add_subplot(222)
	
	ax2.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax2.plot(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdata[:,2]), linestyle=':', color='blue', linewidth=1)
	ax2.plot(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdata[:,2]), linestyle='-.', color='black', linewidth=1)
	ax2.plot(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdata[:,2]), linestyle='--', color='green', linewidth=1)
	
	ax2.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle=':', color='blue', linewidth=3)
	ax2.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle='-.', color='black', linewidth=3)
	ax2.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle='--', color='green', linewidth=3)
	
	ax2.fill_between(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdata[:,2]), relf(LHHQdataDEA[:,2],LHLQdataDEA[:,2]), color='blue', alpha='0.05')
	ax2.fill_between(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdata[:,2]), relf(HHLQdataDEA[:,2],LHLQdataDEA[:,2]), color='black', alpha='0.05')
	ax2.fill_between(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdata[:,2]), relf(HHHQdataDEA[:,2],LHLQdataDEA[:,2]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	ax2.set_xticklabels([])
	ax2.set_ylabel(r'$R^2_{o}/\left( R^2_{o} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize})
	ax2.yaxis.set_label_position('right')
	ax2.yaxis.tick_right()
	ax2.yaxis.set_ticks_position('both')
	ax2.text(0.05, 0.85,'(b)', transform=ax2.transAxes, fontsize=plotfontsize + 5)
	
	ax2.legend(loc='lower left')
	# end of R2o
	
	# R2l
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -55.0, 10.0
	
	ax3 = fig.add_subplot(223)
	
	ax3.axhline(0.0, color='red', linewidth=1)
	ax3.plot(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdata[:,3]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax3.plot(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdata[:,3]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax3.plot(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdata[:,3]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax3.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle=':', color='blue', linewidth=3)
	ax3.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle='-.', color='black', linewidth=3)
	ax3.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle='--', color='green', linewidth=3)
	
	ax3.fill_between(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdata[:,3]), relf(LHHQdataDEA[:,3],LHLQdataDEA[:,3]), color='blue', alpha='0.05')
	ax3.fill_between(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdata[:,3]), relf(HHLQdataDEA[:,3],LHLQdataDEA[:,3]), color='black', alpha='0.05')
	ax3.fill_between(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdata[:,3]), relf(HHHQdataDEA[:,3],LHLQdataDEA[:,3]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$R^2_{l}/\left( R^2_{l} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize})
	ax3.text(0.85, 0.1,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	ax3.legend(loc='lower left')
	
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -32.0, 1.0
	
	ax4 = fig.add_subplot(224)
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax4.axhline(0.0, color='red', linewidth=1)
	ax4.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,4],LHLQdata[:,4]), linestyle=':', color='blue', linewidth=1)
	ax4.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,4],LHLQdata[:,4]), linestyle='-.', color='black', linewidth=1)
	ax4.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,4],LHLQdata[:,4]), linestyle='--', color='green', linewidth=1)
	
	ax4.plot(LHHQdataDEA[:,0], onezero*relf(LHHQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax4.plot(HHLQdataDEA[:,0], onezero*relf(HHLQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax4.plot(HHHQdataDEA[:,0], onezero*relf(HHHQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax4.fill_between(LHHQdata[:,0], onezero*relf(LHHQdata[:,4],LHLQdata[:,4]), onezero*relf(LHHQdataDEA[:,4],LHLQdataDEA[:,4]), color='blue', alpha='0.05')
	ax4.fill_between(HHLQdata[:,0], onezero*relf(HHLQdata[:,4],LHLQdata[:,4]), onezero*relf(HHLQdataDEA[:,4],LHLQdataDEA[:,4]), color='black', alpha='0.05')
	ax4.fill_between(HHHQdata[:,0], onezero*relf(HHHQdata[:,4],LHLQdata[:,4]), onezero*relf(HHHQdataDEA[:,4],LHLQdataDEA[:,4]), color='green', alpha='0.05')

	# update axes limits and axes labels
	ax4.axis([xlower, xupper, ylower, yupper])
	ax4.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax4.set_ylabel(r'$R^2_{ol}/\left( R^2_{ol} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize, 'rotation': 90})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	ax4.text(0.85, 0.1,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	#ax4.legend(loc='lower left', prop={'size': plotfontsize})
	ax4.legend(loc='lower left')
	# end of R2ol
	
	#plt.show()
	plt.savefig('R2ij_reldev_SSHvsDEA_vs_TDEPVX.pdf', format='pdf')




if __name__ == "__main__":
	generate_all_plots()




# End of file
