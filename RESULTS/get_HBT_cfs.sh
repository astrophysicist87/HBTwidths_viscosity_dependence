#!/bin/bash

#output file contains (in this order):
# R^2_s, R^2_o, R^2_l, R^2_{ol}, <x_o t>, <x_l t>, <x_o x_l>, <x^2_o>, <x^2_l>, <t^2>

nevs=$1
ebs=$2

if [[ "$ebs" == "0.08" ]]
then
	for idx in 1 2 3 4
	do
		echo 'Starting TdepV =' $idx'...'
		direc="RESULTS_etaBYs_`echo $ebs`/NEW_TDEP_V`echo $idx`"
		subdirec="NEW_TDEP_V`echo $idx`_results"
		for ((i=1; i<=$nevs; i++))
		do
			echo '   --> TdepV =' $idx': event =' $i
			# generate *cfs_0 files
			infile1=$direc/`echo $subdirec`-`echo $i`/Sourcefunction_variances_cfs_COS.dat
			infile2=$direc/`echo $subdirec`-`echo $i`/HBTradii_cfs_ev`echo $i`.dat
			infile1p=`echo $infile1`'_cfs_0'
			infile2p=`echo $infile2`'_cfs_0'
			awk '$3==0' $infile1 >> $infile1p
			awk '$3==0' $infile2 >> $infile2p
			
			# generate EbE files
			for KTval in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0
			do
				outfile=$direc/NEW_TDEP_V`echo $idx`_EbE_HBT_and_SV_KT_`echo $KTval`_GeV_`echo $nevs`evs.dat
				res1=`awk -v kt=$KTval '$2==kt {print $5, $6, $9, $11, $12, $13}' $infile1p`
				res2=`awk -v kt=$KTval '$2==kt {print $4, $6, $10, $14}' $infile2p`
				echo $res2 $res1 >> $outfile
			done
		done
    echo 'Finished TdepV =' $idx
	done
else
    for ((i=1; i<=$nevs; i++))
    do
		# generate *cfs_0 files
		echo 'Event '$i': Generating cfs = 0 files...'
		infile1=RESULTS_etaBYs_`echo $ebs`/results-`echo $i`/Sourcefunction_variances_cfs_COS.dat
		infile2=RESULTS_etaBYs_`echo $ebs`/results-`echo $i`/HBTradii_cfs_ev`echo $i`.dat
		infile1p=`echo $infile1`'_cfs_0'
		infile2p=`echo $infile2`'_cfs_0'
		awk '$3==0' $infile1 >> $infile1p
		awk '$3==0' $infile2 >> $infile2p
		
		# generate EbE files
		echo 'Event '$i': Generating EbE files...'
		for KTval in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0
		do
			outfile=RESULTS_etaBYs_`echo $ebs`/EbE_HBT_and_SV_KT_`echo $KTval`_GeV_`echo $nevs`evs.dat
			res1=`awk -v kt=$KTval '$2==kt {print $5, $6, $9, $11, $12, $13}' $infile1p`
			res2=`awk -v kt=$KTval '$2==kt {print $4, $6, $10, $14}' $infile2p`
			echo $res2 $res1 >> $outfile
		done
    done
    echo 'Finished eta/s =' $ebs
fi
