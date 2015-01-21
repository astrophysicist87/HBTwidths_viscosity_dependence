#!/bin/bash

# submit this script in the background

nevs=1000
collectresultsoutput='RESULTS_etaBYs_0.08/collect_results_run_record.dat'

# generate all 0th order Fourier coefficients for HBT radii and source variances, collect all coefficients
bash get_HBT_cfs.sh &> $collectresultsoutput

for Tidx in 1 2 3 4
do
	# generate files for histograms and then zip them up for each folder
	bash prep_hist_radii.sh 0.08 $Tidx $nevs &>> $collectresultsoutput
	
	# then compute direct ensemble averages and variances
	bash complete_FOsurface_properties.sh $Tidx $nevs 0.08 &>> $collectresultsoutput
done
