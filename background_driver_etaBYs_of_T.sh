#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src
HBTexecutable=process_event

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/TDEPebs_results-`echo $1`_hydro_and_HBT_processing.out"
outfile=`get_filename $outfilename`

for CPvisflag in 1 2 3 4
do
	if [[ "$CPvisflag" == "1" ]]
	then
		fitfactor=1.027
	elif [[ "$CPvisflag" == "2" ]]
	then
		fitfactor=0.688
	elif [[ "$CPvisflag" == "3" ]]
	then
		fitfactor=1.014
	else
		fitfactor=0.68
	fi
	echo 'Working on eta/s(T), parametrization #' $CPvisflag'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization #' $CPvisflag 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=`echo $CPvisflag` >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYsTparm_`echo $CPvisflag`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization #' $CPvisflag 'and results-'$1'.' >> $outfile
	cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	dir1=$basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`
	individualResultsDirectory=NEW_TDEP_V`echo $CPvisflag`_results
	outputfolder=$dir1/$individualResultsDirectory-`echo $1`
	# move output from hydro
	mv $hydrofolder/results $outputfolder
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	# do HBT and related calculations on hydro output
	#echo 'Starting HBT calculations...' >> $outfile
	#cp $HBTfolder/$HBTexecutable $outputfolder/$HBTexecutable
	#$outputfolder/$HBTexecutable $dir1 $individualResultsDirectory $idx &
done

\rm -rf $basedirectory/$2
