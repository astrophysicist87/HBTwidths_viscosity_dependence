#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['pdf.fonttype'] = 42

def relf(a,b):
	return 100.*(a-b)/b

def generate_R2s_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.85,0.85])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -10.0, 85.0
	
	#R2s
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,1]]
	
	ax.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='blue', alpha='0.05')
	ax.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')
	ax.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='green', alpha='0.05')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'p.c. dev. from LH-LQ for $R^2_s$', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=2)
	
	#plt.show()
	#plt.savefig('R2sSSH_vs_DEA_TDEPVX.pdf', format='pdf')
	plt.savefig('R2sSSH_vs_DEA_TDEPVX_shaded.pdf', format='pdf')



def generate_R2o_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -45.0, 20.0
	
	#R2o
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,2]]
	
	ax.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='blue', alpha='0.05')
	ax.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')
	ax.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='green', alpha='0.05')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'p.c. dev. from LH-LQ for $R^2_o$', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=3)
	
	#plt.show()
	#plt.savefig('R2oSSH_vs_DEA_TDEPVX.pdf', format='pdf')
	plt.savefig('R2oSSH_vs_DEA_TDEPVX_shaded.pdf', format='pdf')



def generate_R2l_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -40.0, 10.0
	
	#R2l
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,3]]
	
	ax.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax.plot(LHHQdataDEA[:,0], relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax.plot(HHLQdataDEA[:,0], relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax.plot(HHHQdataDEA[:,0], relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	ax.fill_between(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='blue', alpha='0.05')
	ax.fill_between(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')
	ax.fill_between(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='green', alpha='0.05')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'p.c. dev. from LH-LQ for $R^2_l$', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=3)
	
	#plt.show()
	#plt.savefig('R2lSSH_vs_DEA_TDEPVX.pdf', format='pdf')
	plt.savefig('R2lSSH_vs_DEA_TDEPVX_shaded.pdf', format='pdf')



def generate_R2ol_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.1,0.825,0.8])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -30.0, 1.0
	
	#R2ol
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	LHLQdataDEA=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	LHHQdataDEA=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	HHLQdataDEA=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	HHHQdataDEA=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_complete_FOsurface_properties_etaBYs_0.08_1000evs.dat')[:,[0,4]]
	

	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	ax.axhline(0.0, color='red', linewidth=1, label='LH-LQ (SSH, DEA)')
	ax.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=1, label='LH-HQ (SSH)')
	ax.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=1, label='HH-LQ (SSH)')
	ax.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=1, label='HH-HQ (SSH)')
	
	ax.plot(LHHQdataDEA[:,0], onezero*relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle=':', color='blue', linewidth=3, label='LH-HQ (DEA)')
	ax.plot(HHLQdataDEA[:,0], onezero*relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='-.', color='black', linewidth=3, label='HH-LQ (DEA)')
	ax.plot(HHHQdataDEA[:,0], onezero*relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), linestyle='--', color='green', linewidth=3, label='HH-HQ (DEA)')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_{ol}/\left( R^2_{ol} \right) _{LH-LQ} - 1$ (%)', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=3)
	
	ax.fill_between(LHHQdata[:,0], onezero*relf(LHHQdata[:,1],LHLQdata[:,1]), onezero*relf(LHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='blue', alpha='0.05')
	ax.fill_between(HHLQdata[:,0], onezero*relf(HHLQdata[:,1],LHLQdata[:,1]), onezero*relf(HHLQdataDEA[:,1],LHLQdataDEA[:,1]), color='black', alpha='0.05')
	ax.fill_between(HHHQdata[:,0], onezero*relf(HHHQdata[:,1],LHLQdata[:,1]), onezero*relf(HHHQdataDEA[:,1],LHLQdataDEA[:,1]), color='green', alpha='0.05')
	
	#plt.show()
	#plt.savefig('R2olSSH_vs_DEA_TDEPVX.pdf', format='pdf')
	plt.savefig('R2olSSH_vs_DEA_TDEPVX_shaded.pdf', format='pdf')




if __name__ == "__main__":
	#generate_R2s_plots()
	#generate_R2o_plots()
	#generate_R2l_plots()
	generate_R2ol_plots()
