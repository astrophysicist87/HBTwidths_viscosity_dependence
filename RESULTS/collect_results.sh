#!/bin/bash

# submit this script in the background

nevs=1000
ebs=0.00
collectresultsoutputname="RESULTS_etaBYs_`echo $ebs`/collect_results_run_record.dat"
collectresultsoutput=`get_filename $collectresultsoutputname`

# generate all nth order Fourier coefficients for HBT radii and source variances, collect all coefficients
bash get_HBT_cfs.sh $nevs $ebs &> $collectresultsoutput

# generate files for histograms and then zip them up for each folder
bash prep_hist_radii.sh $nevs $ebs &>> $collectresultsoutput

# then compute direct ensemble averages and variances
bash complete_FOsurface_properties.sh $nevs $ebs &>> $collectresultsoutput

# End of file
