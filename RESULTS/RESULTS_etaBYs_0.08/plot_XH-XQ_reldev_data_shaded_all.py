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
	
	idealdata=loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	idealdataDEA=loadtxt('../RESULTS_etaBYs_0.00/complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')[:,cols2]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -25.0, 42.5
	
	ax1 = fig.add_subplot(221)
	
	ax1.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax1.plot(idealdata[:,0], relf(idealdata[:,1],LHLQdata[:,1]), linestyle='-', color='black', linewidth=1, label='ideal (SSH)')
	ax1.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax1.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax1.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax1.plot(idealdataDEA[:,0], relf(idealdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-', color='black', linewidth=3, label='ideal (DEA)')
	ax1.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax1.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax1.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')

	ax1.fill_between(idealdata[:,0], relf(idealdata[:,1],LHLQdata[:,1]), relf(idealdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')	
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
	ylower, yupper = -30.0, 15.0
	
	ax2 = fig.add_subplot(222)
	
	ax2.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax2.plot(idealdata[:,0], relf(idealdata[:,2],LHLQdata[:,2]), linestyle='-', color='black', linewidth=1, label='ideal (SSH)')
	ax2.plot(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdata[:,2]), linestyle=':', color='blue', linewidth=1)
	ax2.plot(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdata[:,2]), linestyle='-.', color='black', linewidth=1)
	ax2.plot(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdata[:,2]), linestyle='--', color='green', linewidth=1)
	
	ax2.plot(idealdataDEA[:,0], relf(idealdataDEA[:,2],LHLQdataDEA[:,2]), linestyle='-', color='black', linewidth=3, label='ideal (DEA)')
	ax2.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle=':', color='blue', linewidth=3)
	ax2.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle='-.', color='black', linewidth=3)
	ax2.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,2],LHLQdataDEA[:,2]), linestyle='--', color='green', linewidth=3)
	
	ax2.fill_between(idealdata[:,0], relf(idealdata[:,2],LHLQdata[:,2]), relf(idealdataDEA[:,2],LHLQdataDEA[:,2]), color='black', alpha='0.05')	
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
	
	#ax2.legend(loc='best')
	# end of R2o
	
	# R2l
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -35.0, 29.0
	
	ax3 = fig.add_subplot(223)
	
	ax3.axhline(0.0, color='red', linewidth=1)
	ax3.plot(idealdata[:,0], relf(idealdata[:,3],LHLQdata[:,3]), linestyle='-', color='black', linewidth=1, label='ideal (SSH)')
	ax3.plot(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdata[:,3]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax3.plot(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdata[:,3]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax3.plot(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdata[:,3]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax3.plot(idealdataDEA[:,0], relf(idealdataDEA[:,3],LHLQdataDEA[:,3]), linestyle='-', color='black', linewidth=3, label='ideal (DEA)')
	ax3.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle=':', color='blue', linewidth=3)
	ax3.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle='-.', color='black', linewidth=3)
	ax3.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,3],LHLQdataDEA[:,3]), linestyle='--', color='green', linewidth=3)
	
	ax3.fill_between(idealdata[:,0], relf(idealdata[:,3],LHLQdata[:,3]), relf(idealdataDEA[:,3],LHLQdataDEA[:,3]), color='black', alpha='0.05')	
	ax3.fill_between(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdata[:,3]), relf(LHHQdataDEA[:,3],LHLQdataDEA[:,3]), color='blue', alpha='0.05')
	ax3.fill_between(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdata[:,3]), relf(HHLQdataDEA[:,3],LHLQdataDEA[:,3]), color='black', alpha='0.05')
	ax3.fill_between(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdata[:,3]), relf(HHHQdataDEA[:,3],LHLQdataDEA[:,3]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$R^2_{l}/\left( R^2_{l} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize})
	ax3.text(0.85, 0.85,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	#ax3.legend(loc='upper left')
	
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -35.0, 29.0
	
	ax4 = fig.add_subplot(224)
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax4.axhline(0.0, color='red', linewidth=1)
	ax4.plot(idealdata[:,0], onezero*relf(idealdata[:,4],LHLQdata[:,4]), linestyle='-', color='black', linewidth=1, label='ideal (SSH)')
	ax4.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,4],LHLQdata[:,4]), linestyle=':', color='blue', linewidth=1)
	ax4.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,4],LHLQdata[:,4]), linestyle='-.', color='black', linewidth=1)
	ax4.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,4],LHLQdata[:,4]), linestyle='--', color='green', linewidth=1)
	
	ax4.plot(idealdataDEA[:,0], onezero*relf(idealdataDEA[:,4],LHLQdataDEA[:,4]), linestyle='-', color='black', linewidth=3, label='ideal (DEA)')
	ax4.plot(LHHQdataDEA[:,0], onezero*relf(LHHQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax4.plot(HHLQdataDEA[:,0], onezero*relf(HHLQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax4.plot(HHHQdataDEA[:,0], onezero*relf(HHHQdataDEA[:,4],LHLQdataDEA[:,4]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax4.fill_between(idealdata[:,0], onezero*relf(idealdata[:,4],LHLQdata[:,4]), onezero*relf(idealdataDEA[:,4],LHLQdataDEA[:,4]), color='black', alpha='0.05')	
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
	ax4.text(0.85, 0.85,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	#ax4.legend(loc='lower left', prop={'size': plotfontsize})
	#ax4.legend(loc='upper left')
	# end of R2ol
	
	plt.show()
	#plt.savefig('R2ij_reldev_SSHvsDEA_vs_TDEPVX.pdf', format='pdf')





def generate_all_self_plots():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	cols1 = [1,3,5,9,13]	# KT, R2s, R2o, R2l, R2ol (SSH)
	cols2 = [0,1,2,3,4]	# KT, R2s, R2o, R2l, R2ol (DEA)
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	idealdata=loadtxt('../RESULTS_etaBYs_0.00/results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,cols1]
	idealdataDEA=loadtxt('../RESULTS_etaBYs_0.00/complete_FOsurface_properties_etaBYs_0.00_1000evs.dat')[:,cols2]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	
	# R2s
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -12.5, 7.5
	
	ax1 = fig.add_subplot(221)
	
	ax1.axhline(0.0, color='black', linewidth=1)
	
	ax1.plot(LHLQdata[:,0], relf(LHLQdata[:,1],LHLQdataDEA[:,1]), linestyle='-', color='red', linewidth=3, label='LH-HQ')
	ax1.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHHQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ')
	ax1.plot(HHLQdata[:,0], relf(HHLQdata[:,1],HHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ')
	ax1.plot(HHHQdata[:,0], relf(HHHQdata[:,1],HHHQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ')
	ax1.plot(idealdata[:,0], relf(idealdata[:,1],idealdataDEA[:,1]), linestyle='-', color='black', linewidth=3, label='ideal')
	
	#ax1.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdataDEA[:,1]), 1.0, color='red', alpha='0.05')
	#ax1.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHHQdataDEA[:,1]), 1.0, color='blue', alpha='0.05')
	#ax1.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],HHLQdataDEA[:,1]), 1.0, color='black', alpha='0.05')
	#ax1.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],HHHQdataDEA[:,1]), 1.0, color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$\bar{R}^2_{s} \!/ \left< R^2_{s} \!\right> _{ev} - 1$ (%)', {'fontsize': plotfontsize+3})
	ax1.text(0.05, 0.85,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	# end of R2s
	
	# R2o
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -12.5, 7.5
	
	ax2 = fig.add_subplot(222)
	
	ax2.axhline(0.0, color='black', linewidth=1)
	
	ax2.plot(LHLQdata[:,0], relf(LHLQdata[:,2],LHLQdataDEA[:,2]), linestyle='-', color='red', linewidth=3)
	ax2.plot(LHHQdata[:,0], relf(LHHQdata[:,2],LHHQdataDEA[:,2]), linestyle=':', color='blue', linewidth=3)
	ax2.plot(HHLQdata[:,0], relf(HHLQdata[:,2],HHLQdataDEA[:,2]), linestyle='-.', color='black', linewidth=3)
	ax2.plot(HHHQdata[:,0], relf(HHHQdata[:,2],HHHQdataDEA[:,2]), linestyle='--', color='green', linewidth=3)
	ax2.plot(idealdata[:,0], relf(idealdata[:,2],idealdataDEA[:,2]), linestyle='-', color='black', linewidth=3, label='ideal')
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	ax2.set_xticklabels([])
	ax2.set_ylabel(r'$\bar{R}^2_{o} \!/ \left< R^2_{o} \!\right> _{ev} - 1$ (%)', {'fontsize': plotfontsize+3})
	ax2.yaxis.set_label_position('right')
	ax2.yaxis.tick_right()
	ax2.yaxis.set_ticks_position('both')
	ax2.text(0.05, 0.85,'(b)', transform=ax2.transAxes, fontsize=plotfontsize + 5)
	
	ax2.legend(loc='best')
	# end of R2o
	
	# R2l
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -12.5, 7.5
	
	ax3 = fig.add_subplot(223)
	
	ax3.axhline(0.0, color='black', linewidth=1)
	
	ax3.plot(LHLQdata[:,0], relf(LHLQdata[:,3],LHLQdataDEA[:,3]), linestyle='-', color='red', linewidth=3, label='LH-HQ')
	ax3.plot(LHHQdata[:,0], relf(LHHQdata[:,3],LHHQdataDEA[:,3]), linestyle=':', color='blue', linewidth=3, label='LH-HQ')
	ax3.plot(HHLQdata[:,0], relf(HHLQdata[:,3],HHLQdataDEA[:,3]), linestyle='-.', color='black', linewidth=3)
	ax3.plot(HHHQdata[:,0], relf(HHHQdata[:,3],HHHQdataDEA[:,3]), linestyle='--', color='green', linewidth=3)
	ax3.plot(idealdata[:,0], relf(idealdata[:,3],idealdataDEA[:,3]), linestyle='-', color='black', linewidth=3)
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$\bar{R}^2_{l} \!/ \left< R^2_{l} \!\right> _{ev} - 1$ (%)', {'fontsize': plotfontsize+3})
	#ax3.text(0.85, 0.1,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	ax3.text(0.05, 0.1,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	#ax3.legend(loc='lower left')
	ax3.legend(loc='best')
	
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -12.5, 7.5
	
	ax4 = fig.add_subplot(224)
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax4.axhline(0.0, color='black', linewidth=1)
	
	ax4.plot(LHLQdata[:,0], onezero*relf(LHLQdata[:,4],LHLQdataDEA[:,4]), linestyle='-', color='red', linewidth=3)
	ax4.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,4],LHHQdataDEA[:,4]), linestyle=':', color='blue', linewidth=3)
	ax4.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,4],HHLQdataDEA[:,4]), linestyle='-.', color='black', linewidth=3, label='HH-LQ')
	ax4.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,4],HHHQdataDEA[:,4]), linestyle='--', color='green', linewidth=3, label='HH-HQ')
	ax4.plot(idealdata[:,0], onezero*relf(idealdata[:,4],idealdataDEA[:,4]), linestyle='-', color='black', linewidth=3)

	# update axes limits and axes labels
	ax4.axis([xlower, xupper, ylower, yupper])
	ax4.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax4.set_ylabel(r'$\bar{R}^2_{ol} \!/ \left< R^2_{ol} \!\right> _{ev} - 1$ (%)', {'fontsize': plotfontsize+3})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	#ax4.text(0.85, 0.1,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	ax4.text(0.05, 0.1,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	#ax4.legend(loc='lower left', prop={'size': plotfontsize})
	#ax4.legend(loc='lower left')
	ax4.legend(loc='best')
	# end of R2ol
	
	#plt.show()
	plt.savefig('R2ij_reldevabs_SSHvsDEA_vs_TDEPVX.pdf', format='pdf')







def generate_SV_self_plots():
	# set-up
	plotfontsize = 12
	relativesubplotsize = 0.125
	cols1 = [1,10,4,12,8]	# KT, x2o, xot, t2, xoxl (SSH)
	cols2 = [0,8,5,10,7]	# KT, x2o, xot, t2, xoxl (DEA)
	fig = plt.figure()
	fig.subplots_adjust(wspace=0.0, hspace=0.0)
	
	LHLQdataradii=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[5,13]]
	LHHQdataradii=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[5,13]]
	HHLQdataradii=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[5,13]]
	HHHQdataradii=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[5,13]]
	LHLQdataDEAradii=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[2,4]]
	LHHQdataDEAradii=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[2,4]]
	HHLQdataDEAradii=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[2,4]]
	HHHQdataDEAradii=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[2,4]]
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/Sourcefunction_variances_cfs_COS.dat_cfs_0')[:,cols1]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/Sourcefunction_variances_cfs_COS.dat_cfs_0')[:,cols1]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/Sourcefunction_variances_cfs_COS.dat_cfs_0')[:,cols1]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/Sourcefunction_variances_cfs_COS.dat_cfs_0')[:,cols1]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,cols2]
	
	# R2s
	xlower, xupper = 1.0, 2.0
	ylower, yupper = -95.0, -80.0
	
	ax1 = fig.add_subplot(221)
	
	ax1.plot(LHLQdata[:,0], relf(LHLQdata[:,1],LHLQdataradii[:,0]), linestyle='solid', color='red', linewidth=1, label='LH-LQ (SSH)')
	ax1.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdataradii[:,0]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax1.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdataradii[:,0]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax1.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdataradii[:,0]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax1.plot(LHLQdataDEA[:,0], relf(LHLQdataDEA[:,1],LHLQdataDEAradii[:,0]), linestyle='solid', color='red', linewidth=3, label='LH-LQ (DEA)')
	ax1.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEAradii[:,0]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax1.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEAradii[:,0]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax1.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEAradii[:,0]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax1.fill_between(LHLQdata[:,0], relf(LHLQdata[:,1],LHLQdataradii[:,0]), relf(LHLQdataDEA[:,1],LHLQdataDEAradii[:,0]), color='red', alpha='0.05')
	ax1.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdataradii[:,0]), relf(LHHQdataDEA[:,1],LHLQdataDEAradii[:,0]), color='blue', alpha='0.05')
	ax1.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdataradii[:,0]), relf(HHLQdataDEA[:,1],LHLQdataDEAradii[:,0]), color='black', alpha='0.05')
	ax1.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdataradii[:,0]), relf(HHHQdataDEA[:,1],LHLQdataDEAradii[:,0]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax1.axis([xlower, xupper, ylower, yupper])
	ax1.set_xticklabels([])
	ax1.set_ylabel(r'$\left( x^2_{o} \!\right) /\left( x^2_{o} \!\right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize})
	#ax1.text(0.05, 0.85,'(a)', transform=ax1.transAxes, fontsize=plotfontsize + 5)
	
	# end of R2s
	
	# R2o
	xlower, xupper = 1.0, 2.0
	ylower, yupper = -120.0, -95.0
	
	ax2 = fig.add_subplot(222)
	
	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax2.plot(LHLQdata[:,0], relf(LHLQdata[:,2],LHLQdataradii[:,0]), linestyle='solid', color='red', linewidth=1, label='LH-LQ (SSH)')
	ax2.plot(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdataradii[:,0]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax2.plot(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdataradii[:,0]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax2.plot(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdataradii[:,0]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax2.plot(LHLQdataDEA[:,0], relf(LHLQdataDEA[:,2],LHLQdataDEAradii[:,0]), linestyle='solid', color='red', linewidth=3, label='LH-LQ (DEA)')
	ax2.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,2],LHLQdataDEAradii[:,0]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax2.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,2],LHLQdataDEAradii[:,0]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax2.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,2],LHLQdataDEAradii[:,0]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax2.fill_between(LHLQdata[:,0], relf(LHLQdata[:,2],LHLQdataradii[:,0]), relf(LHLQdataDEA[:,2],LHLQdataDEAradii[:,0]), color='red', alpha='0.05')
	ax2.fill_between(LHHQdata[:,0], relf(LHHQdata[:,2],LHLQdataradii[:,0]), relf(LHHQdataDEA[:,2],LHLQdataDEAradii[:,0]), color='blue', alpha='0.05')
	ax2.fill_between(HHLQdata[:,0], relf(HHLQdata[:,2],LHLQdataradii[:,0]), relf(HHLQdataDEA[:,2],LHLQdataDEAradii[:,0]), color='black', alpha='0.05')
	ax2.fill_between(HHHQdata[:,0], relf(HHHQdata[:,2],LHLQdataradii[:,0]), relf(HHHQdataDEA[:,2],LHLQdataDEAradii[:,0]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax2.axis([xlower, xupper, ylower, yupper])
	ax2.set_xticklabels([])
	ax2.set_ylabel(r'$\left( x_{o}t \!\right) _{SSH}/\left( x_{o}t \!\right) _{DEA} - 1$ (%)', {'fontsize': plotfontsize})
	ax2.yaxis.set_label_position('right')
	ax2.yaxis.tick_right()
	ax2.yaxis.set_ticks_position('both')
	#ax2.text(0.05, 0.85,'(b)', transform=ax2.transAxes, fontsize=plotfontsize + 5)
	
	#ax2.legend(loc='best')
	# end of R2o
	
	# R2l
	xlower, xupper = 1.0, 2.0
	ylower, yupper = -60.0, -25.0
	
	ax3 = fig.add_subplot(223)
	
	ax3.plot(LHLQdata[:,0], relf(LHLQdata[:,3],LHLQdataradii[:,0]), linestyle='solid', color='red', linewidth=1, label='LH-LQ (SSH)')
	ax3.plot(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdataradii[:,0]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax3.plot(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdataradii[:,0]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax3.plot(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdataradii[:,0]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax3.plot(LHLQdataDEA[:,0], relf(LHLQdataDEA[:,3],LHLQdataDEAradii[:,0]), linestyle='solid', color='red', linewidth=3, label='LH-LQ (DEA)')
	ax3.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,3],LHLQdataDEAradii[:,0]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax3.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,3],LHLQdataDEAradii[:,0]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax3.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,3],LHLQdataDEAradii[:,0]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax3.fill_between(LHLQdata[:,0], relf(LHLQdata[:,3],LHLQdataradii[:,0]), relf(LHLQdataDEA[:,3],LHLQdataDEAradii[:,0]), color='red', alpha='0.05')
	ax3.fill_between(LHHQdata[:,0], relf(LHHQdata[:,3],LHLQdataradii[:,0]), relf(LHHQdataDEA[:,3],LHLQdataDEAradii[:,0]), color='blue', alpha='0.05')
	ax3.fill_between(HHLQdata[:,0], relf(HHLQdata[:,3],LHLQdataradii[:,0]), relf(HHLQdataDEA[:,3],LHLQdataDEAradii[:,0]), color='black', alpha='0.05')
	ax3.fill_between(HHHQdata[:,0], relf(HHHQdata[:,3],LHLQdataradii[:,0]), relf(HHHQdataDEA[:,3],LHLQdataDEAradii[:,0]), color='green', alpha='0.05')
	
	# update axes limits and axes labels
	ax3.axis([xlower, xupper, ylower, yupper])
	ax3.set_xticklabels(['0.0', '0.5', '1.0', '1.5'])
	ax3.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax3.set_ylabel(r'$\left( t^2 \!\right) _{SSH}/\left( t^2 \!\right) _{DEA} - 1$ (%)', {'fontsize': plotfontsize})
	#ax3.text(0.85, 0.1,'(c)', transform=ax3.transAxes, fontsize=plotfontsize + 5)
	#ax3.legend(loc='lower left')
	
	# end of R2l
	
	# R2ol
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -75.0, 15.0
	
	ax4 = fig.add_subplot(224)
	
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
	ax4.set_ylabel(r'$\left( x_o x_l \!\right) _{SSH}/\left( x_o x_l \!\right) _{DEA} - 1$ (%)', {'fontsize': plotfontsize})
	ax4.yaxis.set_label_position('right')
	ax4.yaxis.tick_right()
	ax4.yaxis.set_ticks_position('both')
	#ax4.text(0.85, 0.1,'(d)', transform=ax4.transAxes, fontsize=plotfontsize + 5)
	
	#ax4.legend(loc='lower left', prop={'size': plotfontsize})
	#ax4.legend(loc='lower left')
	# end of R2ol
	
	plt.show()
	#plt.savefig('R2ij_reldev_SSHvsDEA_vs_TDEPVX.pdf', format='pdf')








if __name__ == "__main__":
	#generate_all_plots()
	generate_all_self_plots()
	#generate_SV_self_plots()




# End of file
