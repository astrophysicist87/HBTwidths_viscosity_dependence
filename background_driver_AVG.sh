#! /usr/bin/env bash

# first argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-avg
hydrofolder=$basedirectory/$1/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

ICfile=$ICsfolder/sd_*_avg_1000evs_block.dat
#cp $ICsfolder`echo avg`/SCIENTIFIC_sd*_block.dat $hydrofolder/Initial/InitialSd.dat
cp $ICfile $hydrofolder/Initial/InitialSd.dat

outfilename="History/results-`echo avg`_hydro_processing.out"
outfile=`get_filename $outfilename`

#ebs = 0.20: fitfactor = 0.833
#ebs = 0.00: fitfactor = 1.155

for etaBYsval in 0.00
do
	echo 'Working on eta/s =' $etaBYsval'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s =' $etaBYsval 'and results-avg-1...' >> $outfile
	(cd $hydrofolder
	nice -n 0 ./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.155 IVisflagINPUT=0 >> $hydrofolder/results/RunRecord_results-avg_etaBYs_`echo $etaBYsval`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-avg-1.' >> $outfile
	cp $ICfile $hydrofolder/results/
	outputfolder=$basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-avg-1
	mv $hydrofolder/results $outputfolder
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	#cp $HBTfolder/process_event_w_df $outputfolder/process_event_w_df
	#$outputfolder/process_event_w_df &
	cp $HBTfolder/process_event_wo_df $outputfolder/process_event_wo_df
	$outputfolder/process_event_wo_df &
	echo 'Finished HBT calculations.' >> $outfile
done

\rm -rf $basedirectory/$1
