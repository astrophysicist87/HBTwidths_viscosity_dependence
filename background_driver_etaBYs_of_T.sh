#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/TDEPebs_results-`echo $1`_hydro_and_HBT_processing.out"
outfile=`get_filename $outfilename`

#CPvisflag=$3

for CPvisflag in 2 3 4
do
	if [[ "$CPvisflag" == "1" ]]
	then
		fitfactor=1.027
		TVstring="LHLQ"
	elif [[ "$CPvisflag" == "2" ]]
	then
		fitfactor=0.688
		TVstring="LHHQ"
	elif [[ "$CPvisflag" == "3" ]]
	then
		fitfactor=1.014
		TVstring="HHLQ"
	else
		fitfactor=0.68
		TVstring="HHHQ"
	fi
	echo 'Working on eta/s(T), parametrization ' $TVstring'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization ' $TVstring 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	nice -n 0 ./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=`echo $CPvisflag` >> $hydrofolder/results/RunRecord_results-`echo $1`_etaBYsTparm_`echo $TVstring`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization ' $TVstring 'and results-'$1'.' >> $outfile
	#cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/results/
	dir1=$basedirectory/RESULTS/RESULTS_etaBYs_`echo $TVstring`
	individualResultsDirectory=results
	outputfolder=$dir1/$individualResultsDirectory-`echo $1`
	# move output from hydro
	mv $hydrofolder/results $outputfolder
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	cp $HBTfolder/process_event_w_df $outputfolder/process_event_w_df
	$outputfolder/process_event_w_df
	cp $HBTfolder/process_event_wo_df $outputfolder/process_event_wo_df
	$outputfolder/process_event_wo_df
	echo 'Finished HBT calculations.' >> $outfile
done

\rm -rf $basedirectory/$2
