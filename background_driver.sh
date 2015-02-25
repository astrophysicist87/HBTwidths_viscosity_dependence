#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

#outfilename="History/EBS_0.00_results-`echo $1`_hydro_processing.out"
#outfile=`get_filename $outfilename`

#for etaBYsval in 0.05 0.10 0.15 0.20
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
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.155 >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYs_`echo $etaBYsval`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-'$1'.' >> $outfile
	cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	#mv $hydrofolder/results $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`
	#echo 'Moved hydro results to' $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1` >> $outfile
	#echo '' >> $outfile
	#echo 'Starting HBT calculations...' >> $outfile
	#cp $HBTfolder/process_event_wo_df $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`/process_event_wo_df
	#$basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`/process_event_wo_df
	#echo 'Finished HBT calculations.' >> $outfile
done

echo 'Finished all.' >> $outfile
#\rm -rf $basedirectory/$2
