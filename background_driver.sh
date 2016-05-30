#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

#for etaBYsval in 0.05 0.10 0.15 0.20
#factor for ebs=0.00 is 1.155
#factor for ebs=0.20 is 0.833
for etaBYsval in 0.00
do
	outfilename="History/EBS_`echo $etaBYsval`_results-`echo $1`_hydro_processing.out"
	outfile=`get_filename $outfilename`
	
	echo 'Working on eta/s =' $etaBYsval'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s =' $etaBYsval 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	nice -n 0 ./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.15 IVisflagINPUT=0 >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYs_`echo $etaBYsval`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-'$1'.' >> $outfile
	#cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	dir1=$basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`
	individualResultsDirectory=results
	outputfolder=$dir1/$individualResultsDirectory-`echo $1`
	mv $hydrofolder/results $outputfolder
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	cp $HBTfolder/process_event_wo_df $outputfolder/process_event_wo_df
	$outputfolder/process_event_wo_df
	cp $HBTfolder/process_event_w_df $outputfolder/process_event_w_df
	$outputfolder/process_event_w_df &
	echo 'Finished HBT calculations.' >> $outfile
done

echo 'Finished all.' >> $outfile
\rm -rf $basedirectory/$2
