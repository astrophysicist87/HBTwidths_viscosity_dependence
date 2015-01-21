#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt

def relf(a,b):
	return 100.*(a-b)/b

def generate_R2s_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.85,0.85])
	axinset = fig.add_axes([0.15, 0.15, 0.4, 0.3])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 12.0
	pclower, pcupper = -10.0, 100.0
	
	#R2o
	LHLQdata=loadtxt('results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,3]]
	
	ax.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_s$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=1)
	
	#plt.show()
	plt.savefig('R2sSSH_vs_TDEPVX_w_inset.pdf', format='pdf')



def generate_R2o_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.4, 0.5, 0.45, 0.35])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 5.0, 35.0
	pclower, pcupper = -25.0, 25.0
	
	#R2o
	LHLQdata=loadtxt('results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,5]]
	
	ax.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_o$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=3)
	
	#plt.show()
	plt.savefig('R2oSSH_vs_TDEPVX_w_inset.pdf', format='pdf')



def generate_R2l_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.3, 0.3, 0.45, 0.35])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = 0.0, 80.0
	pclower, pcupper = -40.0, 10.0
	
	#R2o
	LHLQdata=loadtxt('results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,9]]
	
	ax.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(LHHQdata[:,0], relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(HHLQdata[:,0], relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(HHHQdata[:,0], relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$R^2_l$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	
	ax.legend()
	
	#plt.show()
	plt.savefig('R2lSSH_vs_TDEPVX_w_inset.pdf', format='pdf')



def generate_R2ol_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	axinset = fig.add_axes([0.4, 0.5, 0.4, 0.3])
	
	#set axes limits
	xlower, xupper = 0.0, 2.0
	ylower, yupper = -5.0, 30.0
	pclower, pcupper = -20.0, 5.0
	
	#R2o
	LHLQdata=loadtxt('results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/HBTradii_cfs_ev1.dat_cfs_0')[:,[1,13]]
	
	ax.plot(LHLQdata[:,0], -LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], -LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], -HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], -HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')

	onezero=zeros(len(LHLQdata[:,0]))+1
	onezero[0]=0.
	
	axinset.axhline(0.0, color='red', linewidth=2)
	axinset.plot(LHHQdata[:,0], onezero*relf(LHHQdata[:,1],LHLQdata[:,1]), linestyle=':', color='blue', linewidth=2)
	axinset.plot(HHLQdata[:,0], onezero*relf(HHLQdata[:,1],LHLQdata[:,1]), linestyle='-.', color='black', linewidth=2)
	axinset.plot(HHHQdata[:,0], onezero*relf(HHHQdata[:,1],LHLQdata[:,1]), linestyle='--', color='green', linewidth=2)
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	axinset.axis([xlower, xupper, pclower, pcupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$-R^2_{ol}$ (fm$^2$)', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=3)
	
	#plt.show()
	plt.savefig('R2olSSH_vs_TDEPVX_w_inset.pdf', format='pdf')



def generate_v2_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 3.0
	ylower, yupper = 0.0, 0.08
	
	#R2o
	LHLQdata=loadtxt('NEW_TDEP_V1/NEW_TDEP_V1_results-avg-1/v2_pTdiff_ev1.dat')[:,[1,2]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/v2_pTdiff_ev1.dat')[:,[1,2]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/v2_pTdiff_ev1.dat')[:,[1,2]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/v2_pTdiff_ev1.dat')[:,[1,2]]
	
	ax.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$v_2$ (SSH)', {'fontsize': plotfontsize + 5})
	
	ax.legend(loc=2)
	
	#plt.show()
	plt.savefig('v2SSH_vs_TDEPVX_w_corrections.pdf', format='pdf')



def generate_v4_plots():
	#set-up
	plotfontsize = 18
	fig = plt.figure()
	ax = fig.add_axes([0.125,0.125,0.825,0.825])
	
	#set axes limits
	xlower, xupper = 0.0, 3.0
	ylower, yupper = 0.00001, 0.04
	
	#R2o
	LHLQdata=loadtxt('results-avg-1/anisotropic_flows_v4_pTdiff_ev1.dat')[:,[1,2]]
	LHHQdata=loadtxt('NEW_TDEP_V2/NEW_TDEP_V2_results-avg-1/anisotropic_flows_v4_pTdiff_ev1.dat')[:,[1,2]]
	HHLQdata=loadtxt('NEW_TDEP_V3/NEW_TDEP_V3_results-avg-1/anisotropic_flows_v4_pTdiff_ev1.dat')[:,[1,2]]
	HHHQdata=loadtxt('NEW_TDEP_V4/NEW_TDEP_V4_results-avg-1/anisotropic_flows_v4_pTdiff_ev1.dat')[:,[1,2]]
	
	ax.plot(LHLQdata[:,0], LHLQdata[:,1], linestyle='solid', color='red', linewidth=2, label='LH-LQ')
	ax.plot(LHHQdata[:,0], LHHQdata[:,1], linestyle=':', color='blue', linewidth=2, label='LH-HQ')
	ax.plot(HHLQdata[:,0], HHLQdata[:,1], linestyle='-.', color='black', linewidth=2, label='HH-LQ')
	ax.plot(HHHQdata[:,0], HHHQdata[:,1], linestyle='--', color='green', linewidth=2, label='HH-HQ')
	
	#update axes limits and axes labels
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_xlabel(r'$K_T$ (GeV)', {'fontsize': plotfontsize + 5})
	ax.set_ylabel(r'$v_2$ (SSH)', {'fontsize': plotfontsize + 5})

	#ax.set_yscale('log')
	
	ax.legend(loc=2)
	
	plt.show()
	#plt.savefig('R2olSSH_vs_TDEPVX_w_inset.pdf', format='pdf')



if __name__ == "__main__":
	#generate_R2s_plots()
	#generate_R2o_plots()
	#generate_R2l_plots()
	#generate_R2ol_plots()
	generate_v2_plots()
	#generate_v4_plots()




# End of file
