#!/bin/bash

ebs=$1
TdepVidx=$2
nevs=$3

#for ebs in 0.00 0.05 0.08 0.10 0.15 0.20
#do
    direc="RESULTS_etaBYs_`echo $ebs`/NEW_TDEP_V`echo $TdepVidx`"
    subdirec="NEW_TDEP_V`echo $TdepVidx`_results"
    echo 'Entering' $direc'...'
    
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Collecting unnormalized radii...'
    
    fsKT0="$direc/R2s0_kt_0.0_`echo $nevs`evs.input"
    fsKT02="$direc/R2s0_kt_0.2_`echo $nevs`evs.input"
    fsKT04="$direc/R2s0_kt_0.4_`echo $nevs`evs.input"
    fsKT06="$direc/R2s0_kt_0.6_`echo $nevs`evs.input"
    fsKT08="$direc/R2s0_kt_0.8_`echo $nevs`evs.input"
    fsKT10="$direc/R2s0_kt_1.0_`echo $nevs`evs.input"
    
    foKT0="$direc/R2o0_kt_0.0_`echo $nevs`evs.input"
    foKT02="$direc/R2o0_kt_0.2_`echo $nevs`evs.input"
    foKT04="$direc/R2o0_kt_0.4_`echo $nevs`evs.input"
    foKT06="$direc/R2o0_kt_0.6_`echo $nevs`evs.input"
    foKT08="$direc/R2o0_kt_0.8_`echo $nevs`evs.input"
    foKT10="$direc/R2o0_kt_1.0_`echo $nevs`evs.input"
    
    flKT0="$direc/R2l0_kt_0.0_`echo $nevs`evs.input"
    flKT02="$direc/R2l0_kt_0.2_`echo $nevs`evs.input"
    flKT04="$direc/R2l0_kt_0.4_`echo $nevs`evs.input"
    flKT06="$direc/R2l0_kt_0.6_`echo $nevs`evs.input"
    flKT08="$direc/R2l0_kt_0.8_`echo $nevs`evs.input"
    flKT10="$direc/R2l0_kt_1.0_`echo $nevs`evs.input"
    
    folKT0="$direc/R2ol0_kt_0.0_`echo $nevs`evs.input"
    folKT02="$direc/R2ol0_kt_0.2_`echo $nevs`evs.input"
    folKT04="$direc/R2ol0_kt_0.4_`echo $nevs`evs.input"
    folKT06="$direc/R2ol0_kt_0.6_`echo $nevs`evs.input"
    folKT08="$direc/R2ol0_kt_0.8_`echo $nevs`evs.input"
    folKT10="$direc/R2ol0_kt_1.0_`echo $nevs`evs.input"
    
    for((ev=1; ev<=$nevs; ev++));
    do
	awk '$2==0 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT0
	awk '$2==0 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT0
	awk '$2==0 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT0
	awk '$2==0 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT0

	awk '$2==0.2 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT02
	awk '$2==0.2 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT02
	awk '$2==0.2 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT02
	awk '$2==0.2 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT02

	awk '$2==0.4 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT04
	awk '$2==0.4 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT04
	awk '$2==0.4 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT04
	awk '$2==0.4 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT04

	awk '$2==0.6 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT06
	awk '$2==0.6 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT06
	awk '$2==0.6 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT06
	awk '$2==0.6 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT06

	awk '$2==0.8 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT08
	awk '$2==0.8 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT08
	awk '$2==0.8 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT08
	awk '$2==0.8 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT08

	awk '$2==1.0 && $3==0 {print $4}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $fsKT10
	awk '$2==1.0 && $3==0 {print $6}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $foKT10
	awk '$2==1.0 && $3==0 {print $10}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $flKT10
	awk '$2==1.0 && $3==0 {print $14}' $direc/`echo $subdirec`-`echo $ev`/HBTradii_cfs_ev`echo $ev`.dat >> $folKT10

	echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished getting radii from event' $ev
    done
    
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished collecting unnormalized radii'
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Time to average now...'
    
    meanR2s0KT0=`mean $fsKT0`
    meanR2o0KT0=`mean $foKT0`
    meanR2l0KT0=`mean $flKT0`
    meanR2ol0KT0=`mean $folKT0`
    
    meanR2s0KT02=`mean $fsKT02`
    meanR2o0KT02=`mean $foKT02`
    meanR2l0KT02=`mean $flKT02`
    meanR2ol0KT02=`mean $folKT02`
    
    meanR2s0KT04=`mean $fsKT04`
    meanR2o0KT04=`mean $foKT04`
    meanR2l0KT04=`mean $flKT04`
    meanR2ol0KT04=`mean $folKT04`
    
    meanR2s0KT06=`mean $fsKT06`
    meanR2o0KT06=`mean $foKT06`
    meanR2l0KT06=`mean $flKT06`
    meanR2ol0KT06=`mean $folKT06`
    
    meanR2s0KT08=`mean $fsKT08`
    meanR2o0KT08=`mean $foKT08`
    meanR2l0KT08=`mean $flKT08`
    meanR2ol0KT08=`mean $folKT08`
    
    meanR2s0KT10=`mean $fsKT10`
    meanR2o0KT10=`mean $foKT10`
    meanR2l0KT10=`mean $flKT10`
    meanR2ol0KT10=`mean $folKT10`
    
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Made it through averages!'
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Normalizing radii...'
    
    awk -v avg=$meanR2s0KT0 '{print $1/avg}' $fsKT0 >> `echo $fsKT0`.normed
    awk -v avg=$meanR2o0KT0 '{print $1/avg}' $foKT0 >> `echo $foKT0`.normed
    awk -v avg=$meanR2l0KT0 '{print $1/avg}' $flKT0 >> `echo $flKT0`.normed
    awk -v avg=$meanR2ol0KT0 '{print $1/avg}' $folKT0 >> `echo $folKT0`.normed
    
    awk -v avg=$meanR2s0KT02 '{print $1/avg}' $fsKT02 >> `echo $fsKT02`.normed
    awk -v avg=$meanR2o0KT02 '{print $1/avg}' $foKT02 >> `echo $foKT02`.normed
    awk -v avg=$meanR2l0KT02 '{print $1/avg}' $flKT02 >> `echo $flKT02`.normed
    awk -v avg=$meanR2ol0KT02 '{print $1/avg}' $folKT02 >> `echo $folKT02`.normed
    
    awk -v avg=$meanR2s0KT04 '{print $1/avg}' $fsKT04 >> `echo $fsKT04`.normed
    awk -v avg=$meanR2o0KT04 '{print $1/avg}' $foKT04 >> `echo $foKT04`.normed
    awk -v avg=$meanR2l0KT04 '{print $1/avg}' $flKT04 >> `echo $flKT04`.normed
    awk -v avg=$meanR2ol0KT04 '{print $1/avg}' $folKT04 >> `echo $folKT04`.normed
    
    awk -v avg=$meanR2s0KT06 '{print $1/avg}' $fsKT06 >> `echo $fsKT06`.normed
    awk -v avg=$meanR2o0KT06 '{print $1/avg}' $foKT06 >> `echo $foKT06`.normed
    awk -v avg=$meanR2l0KT06 '{print $1/avg}' $flKT06 >> `echo $flKT06`.normed
    awk -v avg=$meanR2ol0KT06 '{print $1/avg}' $folKT06 >> `echo $folKT06`.normed
    
    awk -v avg=$meanR2s0KT08 '{print $1/avg}' $fsKT08 >> `echo $fsKT08`.normed
    awk -v avg=$meanR2o0KT08 '{print $1/avg}' $foKT08 >> `echo $foKT08`.normed
    awk -v avg=$meanR2l0KT08 '{print $1/avg}' $flKT08 >> `echo $flKT08`.normed
    awk -v avg=$meanR2ol0KT08 '{print $1/avg}' $folKT08 >> `echo $folKT08`.normed
    
    awk -v avg=$meanR2s0KT10 '{print $1/avg}' $fsKT10 >> `echo $fsKT10`.normed
    awk -v avg=$meanR2o0KT10 '{print $1/avg}' $foKT10 >> `echo $foKT10`.normed
    awk -v avg=$meanR2l0KT10 '{print $1/avg}' $flKT10 >> `echo $flKT10`.normed
    awk -v avg=$meanR2ol0KT10 '{print $1/avg}' $folKT10 >> `echo $folKT10`.normed
    
    echo '   eta/s =' $ebs', TV =' $TdepVidx': Finished normalizing radii'
    echo
#done
echo '   eta/s =' $ebs', TV =' $TdepVidx': Zipping output'
zip -r $direc/R2ij0_histfiles_`echo $nevs`evs.zip $direc/R2*0_kt_*_`echo $nevs`evs.input*
rm $direc/R2*0_kt_*_`echo $nevs`evs.input*

echo 'Finished all.'
