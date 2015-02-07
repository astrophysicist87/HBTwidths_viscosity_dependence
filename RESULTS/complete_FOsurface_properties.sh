#!/bin/bash

#script to generate means and variances for {X_i}, i=1..10, where
#{X_i} = {R^2_s, R^2_o, R^2_l, R^2_{ol}, <x_o t>, <x_l t>, <x_o x_l>, <x^2_o>, <x^2_l>, <t^2>}

nevs=$1
ebs=$2

if [[ "$ebs" == "0.08" ]]
then
	for TdepVidx in 1 2 3 4
	do
		direc="RESULTS_etaBYs_`echo $ebs`/NEW_TDEP_V`echo $TdepVidx`"
		subdirec="NEW_TDEP_V`echo $TdepVidx`_results"
		
		outfile=$direc/NEW_TDEP_V`echo $TdepVidx`_complete_FOsurface_properties_etaBYs_`echo $ebs`_`echo $nevs`evs.dat
		
		for KTval in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0
		do
			infile="$direc/NEW_TDEP_V`echo $TdepVidx`_EbE_HBT_and_SV_KT_`echo $KTval`_GeV_`echo $nevs`evs.dat"
	
			echo 'Processing file' $infile
	
			m1=`mean $infile 1`
			m2=`mean $infile 2`
			m3=`mean $infile 3`
			m4=`mean $infile 4`
			m5=`mean $infile 5`
			m6=`mean $infile 6`
			m7=`mean $infile 7`
			m8=`mean $infile 8`
			m9=`mean $infile 9`
			m10=`mean $infile 10`
	
			v1=`variance $infile 1`
			v2=`variance $infile 2`
			v3=`variance $infile 3`
			v4=`variance $infile 4`
			v5=`variance $infile 5`
			v6=`variance $infile 6`
			v7=`variance $infile 7`
			v8=`variance $infile 8`
			v9=`variance $infile 9`
			v10=`variance $infile 10`
	
			echo $KTval $m1 $m2 $m3 $m4 $m5 $m6 $m7 $m8 $m9 $m10 $v1 $v2 $v3 $v4 $v5 $v6 $v7 $v8 $v9 $v10 >> $outfile

		echo '  '$infile': Finished calculation for K_T =' $KTval
		done	# end of KTval loop
	done	# end of TdepVidx loop
else
	direc="RESULTS_etaBYs_`echo $ebs`"
	subdirec="results"

	outfile=$direc/complete_FOsurface_properties_etaBYs_`echo $ebs`_`echo $nevs`evs.dat

	for KTval in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0
	do
		infile=$direc/EbE_HBT_and_SV_KT_`echo $KTval`_GeV_`echo $nevs`evs.dat

		echo 'Processing file' $infile

		m1=`mean $infile 1`
		m2=`mean $infile 2`
		m3=`mean $infile 3`
		m4=`mean $infile 4`
		m5=`mean $infile 5`
		m6=`mean $infile 6`
		m7=`mean $infile 7`
		m8=`mean $infile 8`
		m9=`mean $infile 9`
		m10=`mean $infile 10`

		v1=`variance $infile 1`
		v2=`variance $infile 2`
		v3=`variance $infile 3`
		v4=`variance $infile 4`
		v5=`variance $infile 5`
		v6=`variance $infile 6`
		v7=`variance $infile 7`
		v8=`variance $infile 8`
		v9=`variance $infile 9`
		v10=`variance $infile 10`

		echo $KTval $m1 $m2 $m3 $m4 $m5 $m6 $m7 $m8 $m9 $m10 $v1 $v2 $v3 $v4 $v5 $v6 $v7 $v8 $v9 $v10 >> $outfile

		echo '  '$infile': Finished calculation for K_T =' $KTval
	done	# end of KTval loop
fi

# End of file
