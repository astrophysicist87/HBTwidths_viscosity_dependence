#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/HBT_process_event

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/TDEPebs_results-`echo $1`_hydro_and_HBT_processing.out"
outfile=`get_filename $outfilename`

for CPvisflag in 1 2 3 4
do
	echo 'Working on eta/s(T), parametrization #' $CPvisflag'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization #' $CPvisflag 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=1.0 IVisflagINPUT=`echo $CPvisflag` >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYsTparm_`echo $CPvisflag`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization #' $CPvisflag 'and results-'$1'.' >> $outfile
	cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	outputfolder=$basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`/NEW_TDEP_V`echo $CPvisflag`_results-`echo $1`
	mv $hydrofolder/results $outputfolder
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	cp $HBTfolder/process_event_ebs_0.08_TV`echo $CPvisflag` $outputfolder/process_event
	$outputfolder/process_event $1
done

\rm -rf $basedirectory/$2
