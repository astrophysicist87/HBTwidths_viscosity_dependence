#!/bin/bash

nevs=$1
ebs=$2

#for ebs in 0.00 0.05 0.08 0.10 0.15 0.20
#do
if [[ "$ebs" == "0.08" ]]
then
	for TdepVidx in 1 2 3 4
	do
		direc="RESULTS_etaBYs_`echo $ebs`/NEW_TDEP_V`echo $TdepVidx`"
		subdirec="NEW_TDEP_V`echo $TdepVidx`_results"
		echo 'Entering' $direc'...'
		
		echo '   eta/s =' $ebs', TV =' $TdepVidx': Collecting unnormalized radii...'
		for KT in 0.0 0.2 0.4 0.6 0.8 1.0
		do
			fnR2s0KTval="$direc/R2s0_kt_`echo $KT`_`echo $nevs`evs.input"
			fnR2o0KTval="$direc/R2o0_kt_`echo $KT`_`echo $nevs`evs.input"
			fnR2l0KTval="$direc/R2l0_kt_`echo $KT`_`echo $nevs`evs.input"
			fnR2ol0KTval="$direc/R2ol0_kt_`echo $KT`_`echo $nevs`evs.input"
			for((ev=1; ev<=$nevs; ev++))
    			do
				awk -v akt=$KT '$2==akt && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2s0KTval
				awk -v akt=$KT '$2==akt && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2o0KTval
				awk -v akt=$KT '$2==akt && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2l0KTval
				awk -v akt=$KT '$2==akt && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2ol0KTval
				echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished getting radii from event' $ev
			done	# end of ev loop

			echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished collecting unnormalized radii'
			echo '   eta/s =' $ebs', TV =' $TdepVidx': Time to average now...'

			meanR2s0KTval=`mean $fnR2s0KTval`
        		meanR2o0KTval=`mean $fnR2o0KTval`
        		meanR2l0KTval=`mean $fnR2l0KTval`
        		meanR2ol0KTval=`mean $fnR2ol0KTval`

			echo '   eta/s =' $ebs', TV =' $TdepVidx': Made it through averages!'
			echo '   eta/s =' $ebs', TV =' $TdepVidx': Normalizing radii...'

			awk -v avg=$meanR2s0KTval '{print $1/avg}' $fnR2s0KTval >> `echo $fnR2s0KTval`.normed
			awk -v avg=$meanR2o0KTval '{print $1/avg}' $fnR2o0KTval >> `echo $fnR2o0KTval`.normed
			awk -v avg=$meanR2l0KTval '{print $1/avg}' $fnR2l0KTval >> `echo $fnR2l0KTval`.normed
			awk -v avg=$meanR2ol0KTval '{print $1/avg}' $fnR2ol0KTval >> `echo $fnR2ol0KTval`.normed

			echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished normalizing radii'
			echo
		done	# end of KT loop
	echo '   eta/s =' $ebs', TV =' $TdepVidx': Zipping output'
	zip -r $direc/R2ij0_histfiles_`echo $nevs`evs.zip $direc/R2*0_kt_*_`echo $nevs`evs.input*
	rm $direc/R2*0_kt_*_`echo $nevs`evs.input*
	done	# end of TdepVidx loop
else
	direc="RESULTS_etaBYs_`echo $ebs`"
	subdirec="results"
	echo 'Entering' $direc'...'
	
	echo '   eta/s =' $ebs': Collecting unnormalized radii...'
	for KT in 0.0 0.2 0.4 0.6 0.8 1.0
	do
		fnR2s0KTval="$direc/R2s0_kt_`echo $KT`_`echo $nevs`evs.input"
		fnR2o0KTval="$direc/R2o0_kt_`echo $KT`_`echo $nevs`evs.input"
		fnR2l0KTval="$direc/R2l0_kt_`echo $KT`_`echo $nevs`evs.input"
		fnR2ol0KTval="$direc/R2ol0_kt_`echo $KT`_`echo $nevs`evs.input"
		for((ev=1; ev<=$nevs; ev++))
    	do
			awk -v akt=$KT '$2==akt && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2s0KTval
			awk -v akt=$KT '$2==akt && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2o0KTval
			awk -v akt=$KT '$2==akt && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2l0KTval
			awk -v akt=$KT '$2==akt && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fnR2ol0KTval
			#echo '   eta/s =' $ebs': Finished getting radii from event' $ev
		done	# end of ev loop

		echo '   eta/s =' $ebs': Finished collecting unnormalized radii from all events'
		echo '   eta/s =' $ebs': Time to average now...'

		meanR2s0KTval=`mean $fnR2s0KTval`
        meanR2o0KTval=`mean $fnR2o0KTval`
        meanR2l0KTval=`mean $fnR2l0KTval`
        meanR2ol0KTval=`mean $fnR2ol0KTval`

		echo '   eta/s =' $ebs': Made it through averages!'
		echo '   eta/s =' $ebs': Normalizing radii...'

		awk -v avg=$meanR2s0KTval '{print $1/avg}' $fnR2s0KTval >> `echo $fnR2s0KTval`.normed
		awk -v avg=$meanR2o0KTval '{print $1/avg}' $fnR2o0KTval >> `echo $fnR2o0KTval`.normed
		awk -v avg=$meanR2l0KTval '{print $1/avg}' $fnR2l0KTval >> `echo $fnR2l0KTval`.normed
		awk -v avg=$meanR2ol0KTval '{print $1/avg}' $fnR2ol0KTval >> `echo $fnR2ol0KTval`.normed

		echo '   eta/s =' $ebs': Finished normalizing radii'
		echo
	done	# end of KT loop
	echo '   eta/s =' $ebs': Zipping output'
	zip -r $direc/R2ij0_histfiles_`echo $nevs`evs.zip $direc/R2*0_kt_*_`echo $nevs`evs.input*
	rm $direc/R2*0_kt_*_`echo $nevs`evs.input*
fi

echo 'Finished all.'
