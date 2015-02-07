#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-avg
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

cp $ICsfolder/sd*block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/TDEPebs_results-avg_hydro_and_HBT_processing.out"
outfile=`get_filename $outfilename`

CPvisflag=$3

#for CPvisflag in 1 2 3 4
#do
	# chosen to get thermal pi^+ multiplicity of (approximately) 137.225
	if [[ "$CPvisflag" == "0" ]]
	then
		fitfactor=1.027
	elif [[ "$CPvisflag" == "1" ]]
	then
		fitfactor=1.027
		#fitfactor=1.24
	elif [[ "$CPvisflag" == "2" ]]
	then
		fitfactor=0.688
		#fitfactor=0.85
	elif [[ "$CPvisflag" == "3" ]]
	then
		fitfactor=1.014
		#fitfactor=1.19
	else
		fitfactor=0.68
		#fitfactor=0.82
	fi
	#fitfactor=1.027
	echo 'Working on eta/s(T), parametrization #' $CPvisflag'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization #' $CPvisflag 'and results-avg-1...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=`echo $CPvisflag` >> $hydrofolder/results/RunRecord_results-avg_etaBYsTparm_`echo $CPvisflag`.txt
	#./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` >> $hydrofolder/results/RunRecord_results-avg_etaBYsTparm_`echo $CPvisflag`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization #' $CPvisflag 'and results-avg-1.' >> $outfile
	cp $ICsfolder/sd*block.dat $hydrofolder/results/
	outputfolder=$basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`/NEW_TDEP_V`echo $CPvisflag`_results-avg-1
	#mv $hydrofolder/results $outputfolder
	mv $hydrofolder/results $hydrofolder/TV`echo $CPvisflag`_results-avg-1
	####################################################################################
	#cp ~/HBTPlumberg/get_anisotropic_flows_src/get_anisotropic_flows $hydrofolder/TV`echo $CPvisflag`_results-avg-1/get_anisotropic_flows
	#$hydrofolder/TV`echo $CPvisflag`_results-avg-1/get_anisotropic_flows &
	####################################################################################
	#cp $HBTfolder/process_event $hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event
	#$hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event &
	####################################################################################
	#echo 'Moved hydro results to' $outputfolder >> $outfile
	#echo '' >> $outfile
	#echo 'Starting HBT calculations...' >> $outfile
	#cp $HBTfolder/process_event $outputfolder/process_event
	#$outputfolder/process_event $1 &
	#echo 'Finished HBT calculations.' >> $outfile
#done

#\rm -rf $basedirectory/$2

echo 'Finished all calculations.' >> $outfile
