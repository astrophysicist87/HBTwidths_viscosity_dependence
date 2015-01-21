#! /usr/bin/env bash

# first argument: index of results folder

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/EBE-Node/VISHNew

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfile=results-`echo $1`_hydro_processing.out

for etaBYsval in 0.00 0.05 0.10 0.15 0.20
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
	mv $hydrofolder/results $basedirectory/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`
	echo 'Moved hydro results to' $basedirectory/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1` >> $outfile
	echo '' >> $outfile
done
