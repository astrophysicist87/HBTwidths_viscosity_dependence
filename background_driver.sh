#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/results-`echo $1`_hydro_processing.out"
outfile=`get_filename $outfilename`

for etaBYsval in 0.05 0.08 0.10 0.15 0.20
do
	echo 'Working on eta/s =' $etaBYsval'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s =' $etaBYsval 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.0 >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYs_`echo $etaBYsval`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-'$1'.' >> $outfile
	cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	mv $hydrofolder/results $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`
	echo 'Moved hydro results to' $basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1` >> $outfile
	echo '' >> $outfile
done

\rm -rf $basedirectory/$2
