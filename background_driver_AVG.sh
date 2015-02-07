#! /usr/bin/env bash

# first argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$1/VISHNew

cp $ICsfolder`echo avg`/sd*_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/results-`echo avg`_hydro_processing.out"
outfile=`get_filename $outfilename`

for etaBYsval in 0.00
do
	echo 'Working on eta/s =' $etaBYsval'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s =' $etaBYsval 'and results-avg-1...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.051 >> $hydrofolder/results/RunRecord_results-avg_etaBYs_`echo $etaBYsval`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-avg-1.' >> $outfile
	cp $ICsfolder`echo avg`/sd*_block.dat $hydrofolder/results/
	mv $hydrofolder/results $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-avg-1
	echo 'Moved hydro results to' $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-avg-1 >> $outfile
	#mv $hydrofolder/results $hydrofolder/results-avg-renormed
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	cp $HBTfolder/process_event $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-avg-1/process_event
	$basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-avg-1/process_event
	echo 'Finished HBT calculations.' >> $outfile
done

\rm -rf $basedirectory/$1
