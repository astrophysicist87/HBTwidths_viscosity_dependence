#!/usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

ebsvals = ['0.08']
TVs = ['1']

dfstem=''
#dfstem='_no_df'

def plot_EbE_R2o(ebs):
	numplots = 6
	plotfontsize = 18
	ax=plt.axes([0.1,0.15,0.85,0.8])
	plt.axhline(0.0, color='black', linewidth=1.5)
	
	#direc = 'RESULTS_etaBYs_%(ebsstring)s/' % {"ebsstring": ebs}
	direc = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)s/' % {"ebsstring": ebs, "TV": TVs[0]}
	
	R2oKT00n = loadtxt(direc + 'R2o0_kt_0.0_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2oKT02n = loadtxt(direc + 'R2o0_kt_0.2_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2oKT04n = loadtxt(direc + 'R2o0_kt_0.4_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2oKT06n = loadtxt(direc + 'R2o0_kt_0.6_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2oKT08n = loadtxt(direc + 'R2o0_kt_0.8_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2oKT10n = loadtxt(direc + 'R2o0_kt_1.0_1000evs%(df)s.input.normed' % {"df": dfstem})

	minKT00n, maxKT00n = min(R2oKT00n), max(R2oKT00n)
	minKT02n, maxKT02n = min(R2oKT02n), max(R2oKT02n)
	minKT04n, maxKT04n = min(R2oKT04n), max(R2oKT04n)
	minKT06n, maxKT06n = min(R2oKT06n), max(R2oKT06n)
	minKT08n, maxKT08n = min(R2oKT08n), max(R2oKT08n)
	minKT10n, maxKT10n = min(R2oKT10n), max(R2oKT10n)

	plotmin, plotmax = min(array([minKT00n, minKT02n, minKT04n, minKT06n, minKT08n, minKT10n])), max(array([maxKT00n, maxKT02n, maxKT04n, maxKT06n, maxKT08n, maxKT10n]))

	#print plotmin, plotmax

	nbins = 20
	dKT = (plotmax - plotmin)/nbins

	plotbins = linspace(plotmin, plotmax, num=nbins)

	#bin_centers = 0.5*(bin_edge[1:] + bin_edges[:-1])
	colormap = plt.cm.gist_ncar
	plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, numplots)])

	# the histogram of the data
	nKT00n, binsKT00n, patchesKT00n = plt.hist(R2oKT00n, plotbins, histtype='step', normed=1)
	nKT02n, binsKT02n, patchesKT02n = plt.hist(R2oKT02n, plotbins, histtype='step', normed=1)
	nKT04n, binsKT04n, patchesKT04n = plt.hist(R2oKT04n, plotbins, histtype='step', normed=1)
	nKT06n, binsKT06n, patchesKT06n = plt.hist(R2oKT06n, plotbins, histtype='step', normed=1)
	nKT08n, binsKT08n, patchesKT08n = plt.hist(R2oKT08n, plotbins, histtype='step', normed=1)
	nKT10n, binsKT10n, patchesKT10n = plt.hist(R2oKT10n, plotbins, histtype='step', normed=1)

	plt.plot(delete(binsKT00n,-1) + 0.5*dKT, nKT00n, '-o', label='$K_T = 0.0$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT02n,-1) + 0.5*dKT, nKT02n, '-o', label='$K_T = 0.2$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT04n,-1) + 0.5*dKT, nKT04n, '-o', label='$K_T = 0.4$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT06n,-1) + 0.5*dKT, nKT06n, '-o', label='$K_T = 0.6$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT08n,-1) + 0.5*dKT, nKT08n, '-o', label='$K_T = 0.8$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT10n,-1) + 0.5*dKT, nKT10n, '-o', label='$K_T = 1.0$ GeV' % {"df": dfstem})

	#adds some nice bars in the background of the histogram to give plot some structure
	dummy1, dummy2, dummy3 = plt.hist(R2oKT00n, plotbins, histtype='bar', normed=1, edgecolor='black', color='white', alpha=0.5)

	plt.xlabel(r'$R^2_{o}/\left<R^2_{o}\right>_{ev}$', {'fontsize': plotfontsize + 5})
	plt.ylabel(r'P($R^2_{o}/\left<R^2_{o}\right>_{ev}$)', {'fontsize': plotfontsize + 5})
	plt.xticks(color='k', size=plotfontsize)
	plt.yticks(color='k', size=plotfontsize)
	minorLocator=MultipleLocator(0.05)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.xaxis.set_tick_params(length=7.5, width=1.5)
	ax.xaxis.set_tick_params(which='minor',length=5.0, width=1.0)
	plt.xlim([plotmin, plotmax])
	plt.ylim([-0.25, 5.25])
	plt.text(0.65, 4.5, 'Normalized event-by-event\n\t\tdistribution for $R^2_{o}$', fontsize=plotfontsize)
	#hl = plt.legend(loc=2, fontsize=plotfontsize)
	#hl.draw_frame(False)

	plt.legend()

	plt.show()

	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2o_vs_KT_1000evs%(df)s.pdf', format='pdf')
	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2o_vs_KT_1000evs%(df)s.eps', format='eps')

	plt.close()


def plot_EbE_R2s(ebs):
	numplots = 6
	plotfontsize = 18
	ax=plt.axes([0.1,0.15,0.85,0.8])
	plt.axhline(0.0, color='black', linewidth=1.5)
	
	#direc = 'RESULTS_etaBYs_%(ebsstring)s/' % {"ebsstring": ebs}
	direc = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)s/' % {"ebsstring": ebs, "TV": TVs[0]}

	R2sKT00n = loadtxt(direc + 'R2s0_kt_0.0_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2sKT02n = loadtxt(direc + 'R2s0_kt_0.2_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2sKT04n = loadtxt(direc + 'R2s0_kt_0.4_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2sKT06n = loadtxt(direc + 'R2s0_kt_0.6_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2sKT08n = loadtxt(direc + 'R2s0_kt_0.8_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2sKT10n = loadtxt(direc + 'R2s0_kt_1.0_1000evs%(df)s.input.normed' % {"df": dfstem})

	minKT00n, maxKT00n = min(R2sKT00n), max(R2sKT00n)
	minKT02n, maxKT02n = min(R2sKT02n), max(R2sKT02n)
	minKT04n, maxKT04n = min(R2sKT04n), max(R2sKT04n)
	minKT06n, maxKT06n = min(R2sKT06n), max(R2sKT06n)
	minKT08n, maxKT08n = min(R2sKT08n), max(R2sKT08n)
	minKT10n, maxKT10n = min(R2sKT10n), max(R2sKT10n)

	plotmin, plotmax = min(array([minKT00n, minKT02n, minKT04n, minKT06n, minKT08n, minKT10n])), max(array([maxKT00n, maxKT02n, maxKT04n, maxKT06n, maxKT08n, maxKT10n]))

	nbins = 20
	dKT = (plotmax - plotmin)/nbins

	plotbins = linspace(plotmin, plotmax, num=nbins)

	#bin_centers = 0.5*(bin_edge[1:] + bin_edges[:-1])
	colormap = plt.cm.gist_ncar
	plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, numplots)])

	# the histogram of the data
	nKT00n, binsKT00n, patchesKT00n = plt.hist(R2sKT00n, plotbins, histtype='step', normed=1)
	nKT02n, binsKT02n, patchesKT02n = plt.hist(R2sKT02n, plotbins, histtype='step', normed=1)
	nKT04n, binsKT04n, patchesKT04n = plt.hist(R2sKT04n, plotbins, histtype='step', normed=1)
	nKT06n, binsKT06n, patchesKT06n = plt.hist(R2sKT06n, plotbins, histtype='step', normed=1)
	nKT08n, binsKT08n, patchesKT08n = plt.hist(R2sKT08n, plotbins, histtype='step', normed=1)
	nKT10n, binsKT10n, patchesKT10n = plt.hist(R2sKT10n, plotbins, histtype='step', normed=1)

	plt.plot(delete(binsKT00n,-1) + 0.5*dKT, nKT00n, '-o', label='$K_T = 0.0$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT02n,-1) + 0.5*dKT, nKT02n, '-o', label='$K_T = 0.2$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT04n,-1) + 0.5*dKT, nKT04n, '-o', label='$K_T = 0.4$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT06n,-1) + 0.5*dKT, nKT06n, '-o', label='$K_T = 0.6$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT08n,-1) + 0.5*dKT, nKT08n, '-o', label='$K_T = 0.8$ GeV' % {"df": dfstem})
	plt.plot(delete(binsKT10n,-1) + 0.5*dKT, nKT10n, '-o', label='$K_T = 1.0$ GeV' % {"df": dfstem})

	#adds some nice bars in the background of the histogram to give plot some structure
	dummy1, dummy2, dummy3 = plt.hist(R2sKT00n, plotbins, histtype='bar', normed=1, edgecolor='black', color='white', alpha=0.5)

	plt.xlabel(r'$R^2_{s}/\left<R^2_{s}\right>_{ev}$', {'fontsize': plotfontsize + 5})
	plt.ylabel(r'P($R^2_{s}/\left<R^2_{s}\right>_{ev}$)', {'fontsize': plotfontsize + 5})
	plt.xticks(color='k', size=plotfontsize)
	plt.yticks(color='k', size=plotfontsize)
	minorLocator=MultipleLocator(0.05)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.xaxis.set_tick_params(length=7.5, width=1.5)
	ax.xaxis.set_tick_params(which='minor',length=5.0, width=1.0)
	#plt.xlim([plotmin, plotmax])
	plt.xlim([0.75, 1.35])
	plt.ylim([-0.25, 6.5])
	plt.text(0.79, 5.35, 'Normalized event-by-event\n\t\tdistribution for $R^2_{s}$', fontsize=plotfontsize)
	#hl = plt.legend(loc=2, fontsize=plotfontsize)
	#hl.draw_frame(False)

	plt.legend()

	plt.show()

	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2s_vs_KT_1000evs%(df)s.pdf', format='pdf')
	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2s_vs_KT_1000evs%(df)s.eps', format='eps')

	plt.close()




def plot_EbE_R2l(ebs):
	numplots = 6
	plotfontsize = 18
	ax=plt.axes([0.1,0.15,0.85,0.8])
	plt.axhline(0.0, color='black', linewidth=1.5)
	
	#direc = 'RESULTS_etaBYs_%(ebsstring)s/' % {"ebsstring": ebs}
	direc = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)s/' % {"ebsstring": ebs, "TV": TVs[0]}

	R2lKT00n = loadtxt(direc + 'R2l0_kt_0.0_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2lKT02n = loadtxt(direc + 'R2l0_kt_0.2_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2lKT04n = loadtxt(direc + 'R2l0_kt_0.4_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2lKT06n = loadtxt(direc + 'R2l0_kt_0.6_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2lKT08n = loadtxt(direc + 'R2l0_kt_0.8_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2lKT10n = loadtxt(direc + 'R2l0_kt_1.0_1000evs%(df)s.input.normed' % {"df": dfstem})

	minKT00n, maxKT00n = min(R2lKT00n), max(R2lKT00n)
	minKT02n, maxKT02n = min(R2lKT02n), max(R2lKT02n)
	minKT04n, maxKT04n = min(R2lKT04n), max(R2lKT04n)
	minKT06n, maxKT06n = min(R2lKT06n), max(R2lKT06n)
	minKT08n, maxKT08n = min(R2lKT08n), max(R2lKT08n)
	minKT10n, maxKT10n = min(R2lKT10n), max(R2lKT10n)

	plotmin, plotmax = min(array([minKT00n, minKT02n, minKT04n, minKT06n, minKT08n, minKT10n])), max(array([maxKT00n, maxKT02n, maxKT04n, maxKT06n, maxKT08n, maxKT10n]))

	#print plotmin, plotmax

	nbins = 20
	dKT = (plotmax - plotmin)/nbins

	plotbins = linspace(plotmin, plotmax, num=nbins)

	#bin_centers = 0.5*(bin_edge[1:] + bin_edges[:-1])
	colormap = plt.cm.gist_ncar
	plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, numplots)])

	# the histogram of the data
	nKT00n, binsKT00n, patchesKT00n = plt.hist(R2lKT00n, plotbins, histtype='step', normed=1)
	nKT02n, binsKT02n, patchesKT02n = plt.hist(R2lKT02n, plotbins, histtype='step', normed=1)
	nKT04n, binsKT04n, patchesKT04n = plt.hist(R2lKT04n, plotbins, histtype='step', normed=1)
	nKT06n, binsKT06n, patchesKT06n = plt.hist(R2lKT06n, plotbins, histtype='step', normed=1)
	nKT08n, binsKT08n, patchesKT08n = plt.hist(R2lKT08n, plotbins, histtype='step', normed=1)
	nKT10n, binsKT10n, patchesKT10n = plt.hist(R2lKT10n, plotbins, histtype='step', normed=1)

	plt.plot(delete(binsKT00n,-1) + 0.5*dKT, nKT00n, '-o', label='$K_T = 0.0$ GeV')
	plt.plot(delete(binsKT02n,-1) + 0.5*dKT, nKT02n, '-o', label='$K_T = 0.2$ GeV')
	plt.plot(delete(binsKT04n,-1) + 0.5*dKT, nKT04n, '-o', label='$K_T = 0.4$ GeV')
	plt.plot(delete(binsKT06n,-1) + 0.5*dKT, nKT06n, '-o', label='$K_T = 0.6$ GeV')
	plt.plot(delete(binsKT08n,-1) + 0.5*dKT, nKT08n, '-o', label='$K_T = 0.8$ GeV')
	plt.plot(delete(binsKT10n,-1) + 0.5*dKT, nKT10n, '-o', label='$K_T = 1.0$ GeV')

	#adds some nice bars in the background of the histogram to give plot some structure
	dummy1, dummy2, dummy3 = plt.hist(R2lKT04n, plotbins, histtype='bar', normed=1, edgecolor='black', color='white', alpha=0.5)

	plt.xlabel(r'$R^2_{l}/\left<R^2_{l}\right>_{ev}$', {'fontsize': plotfontsize + 5})
	plt.ylabel(r'P($R^2_{l}/\left<R^2_{l}\right>_{ev}$)', {'fontsize': plotfontsize + 5})
	plt.xticks(color='k', size=plotfontsize)
	plt.yticks(color='k', size=plotfontsize)
	minorLocator=MultipleLocator(0.05)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.xaxis.set_tick_params(length=7.5, width=1.5)
	ax.xaxis.set_tick_params(which='minor',length=5.0, width=1.0)
	plt.xlim([plotmin, plotmax])
	plt.ylim([-0.25, 5.75])
	plt.text(0.85, 4.75, 'Normalized event-by-event\n\t\tdistribution for $R^2_{l}$', fontsize=plotfontsize)
	#hl = plt.legend(loc=2, fontsize=plotfontsize)
	#hl.draw_frame(False)

	plt.legend()

	plt.show()

	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2l_vs_KT_1000evs%(df)s.pdf', format='pdf')
	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2l_vs_KT_1000evs%(df)s.eps', format='eps')

	plt.close()


def plot_EbE_R2ol(ebs):
	numplots = 6
	plotfontsize = 18
	ax=plt.axes([0.1,0.15,0.85,0.8])
	plt.axhline(0.0, color='black', linewidth=1.5)
	
	#direc = 'RESULTS_etaBYs_%(ebsstring)s/' % {"ebsstring": ebs}
	direc = 'RESULTS_etaBYs_%(ebsstring)s/NEW_TDEP_V%(TV)s/' % {"ebsstring": ebs, "TV": TVs[0]}

	#R2olKT00n = loadtxt(direc + 'R2ol0_kt_0.0_1000evs.input.normed')
	R2olKT02n = loadtxt(direc + 'R2ol0_kt_0.2_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2olKT04n = loadtxt(direc + 'R2ol0_kt_0.4_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2olKT06n = loadtxt(direc + 'R2ol0_kt_0.6_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2olKT08n = loadtxt(direc + 'R2ol0_kt_0.8_1000evs%(df)s.input.normed' % {"df": dfstem})
	R2olKT10n = loadtxt(direc + 'R2ol0_kt_1.0_1000evs%(df)s.input.normed' % {"df": dfstem})

	#minKT00n, maxKT00n = min(R2olKT00n), max(R2olKT00n)
	minKT02n, maxKT02n = min(R2olKT02n), max(R2olKT02n)
	minKT04n, maxKT04n = min(R2olKT04n), max(R2olKT04n)
	minKT06n, maxKT06n = min(R2olKT06n), max(R2olKT06n)
	minKT08n, maxKT08n = min(R2olKT08n), max(R2olKT08n)
	minKT10n, maxKT10n = min(R2olKT10n), max(R2olKT10n)

	#plotmin, plotmax = min(array([minKT00n, minKT02n, minKT04n, minKT06n, minKT08n, minKT10n])), max(array([maxKT00n, maxKT02n, maxKT04n, maxKT06n, maxKT08n, maxKT10n]))
	plotmin, plotmax = min(array([minKT02n, minKT04n, minKT06n, minKT08n, minKT10n])), max(array([maxKT02n, maxKT04n, maxKT06n, maxKT08n, maxKT10n]))

	nbins = 20
	dKT = (plotmax - plotmin)/nbins

	plotbins = linspace(plotmin, plotmax, num=nbins)

	#bin_centers = 0.5*(bin_edge[1:] + bin_edges[:-1])
	colormap = plt.cm.gist_ncar
	plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, numplots)])

	# the histogram of the data
	#nKT00n, binsKT00n, patchesKT00n = plt.hist(R2olKT00n, plotbins, histtype='step', normed=1)
	nKT02n, binsKT02n, patchesKT02n = plt.hist(R2olKT02n, plotbins, histtype='step', normed=1)
	nKT04n, binsKT04n, patchesKT04n = plt.hist(R2olKT04n, plotbins, histtype='step', normed=1)
	nKT06n, binsKT06n, patchesKT06n = plt.hist(R2olKT06n, plotbins, histtype='step', normed=1)
	nKT08n, binsKT08n, patchesKT08n = plt.hist(R2olKT08n, plotbins, histtype='step', normed=1)
	nKT10n, binsKT10n, patchesKT10n = plt.hist(R2olKT10n, plotbins, histtype='step', normed=1)

	#plt.plot(delete(binsKT00n,-1) + 0.5*dKT, nKT00n, '-o', label='$K_T = 0.0$ GeV')
	plt.plot(delete(binsKT02n,-1) + 0.5*dKT, nKT02n, '-o', label='$K_T = 0.2$ GeV')
	plt.plot(delete(binsKT04n,-1) + 0.5*dKT, nKT04n, '-o', label='$K_T = 0.4$ GeV')
	plt.plot(delete(binsKT06n,-1) + 0.5*dKT, nKT06n, '-o', label='$K_T = 0.6$ GeV')
	plt.plot(delete(binsKT08n,-1) + 0.5*dKT, nKT08n, '-o', label='$K_T = 0.8$ GeV')
	plt.plot(delete(binsKT10n,-1) + 0.5*dKT, nKT10n, '-o', label='$K_T = 1.0$ GeV')

	#adds some nice bars in the background of the histogram to give plot some structure
	dummy1, dummy2, dummy3 = plt.hist(R2olKT02n, plotbins, histtype='bar', normed=1, edgecolor='black', color='white', alpha=0.5)

	plt.xlabel(r'$R^2_{ol}/\left<R^2_{ol}\right>_{ev}$', {'fontsize': plotfontsize + 5})
	plt.ylabel(r'P($R^2_{ol}/\left<R^2_{ol}\right>_{ev}$)', {'fontsize': plotfontsize + 5})
	plt.xticks(color='k', size=plotfontsize)
	plt.yticks(color='k', size=plotfontsize)
	minorLocator=MultipleLocator(0.05)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.xaxis.set_tick_params(length=7.5, width=1.5)
	ax.xaxis.set_tick_params(which='minor',length=5.0, width=1.0)
	#plt.xlim([plotmin, plotmax])
	plt.xlim([0.75, 1.35])
	plt.ylim([-0.25, 5.5])
	plt.text(0.79, 4.55, 'Normalized event-by-event\n\t\tdistribution for $R^2_{ol}$', fontsize=plotfontsize)
	#hl = plt.legend(loc=2, fontsize=plotfontsize)
	#hl.draw_frame(False)

	plt.legend()

	plt.show()

	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2ol_vs_KT_1000evs%(df)s.pdf', format='pdf')
	#plt.savefig('/home/plumberg.1/EBE-results/database/EbE_R2ol_vs_KT_1000evs%(df)s.eps', format='eps')

	plt.close()



if __name__ == "__main__":
	for etaBYs in ebsvals:
		plot_EbE_R2s(etaBYs)
		plot_EbE_R2o(etaBYs)
		plot_EbE_R2l(etaBYs)
		plot_EbE_R2ol(etaBYs)


# End of file
