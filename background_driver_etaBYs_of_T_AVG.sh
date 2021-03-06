#! /usr/bin/env bash

# first argument: CPvisflag value
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-avg
hydrofolder=$basedirectory/$2/VISHNew
HBTfolder=~/HBTPlumberg/process_event_src

ICfile=$ICsfolder/sd_shifted_and_rotated*_avg_1000evs_block.dat
cp $ICfile $hydrofolder/Initial/InitialSd.dat

outfilename="History/TDEPebs_results-avg_hydro_and_HBT_processing.out"
outfile=`get_filename $outfilename`

CPvisflag=$1

#for CPvisflag in 1 2 3 4
#do
	# chosen to get thermal pi^+ multiplicity of (approximately) 137.225
	if [[ "$CPvisflag" == "0" ]]
	then
		#fitfactor=1.051
		myvis=0.00
		fitfactor=1.155
	elif [[ "$CPvisflag" == "1" ]]
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
	#fitfactor=1.0
	echo 'Working on eta/s(T), parametrization #' $CPvisflag'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization #' $CPvisflag 'and results-avg-1...' >> $outfile
	hydrooutput=$hydrofolder/results/RunRecord_results-avg_etaBYsTparm_`echo $CPvisflag`.txt
	echo "Running ./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $myvis` IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=`echo $CPvisflag`" >> $hydrooutput
	echo '-------------------------------------------------------------' >> $hydrooutput
	echo '-------------------------------------------------------------' >> $hydrooutput
	echo 'Beginning:' >> $hydrooutput
	(cd $hydrofolder
	nice -n 0 ./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=`echo $CPvisflag` >> $hydrooutput
	#./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $myvis` IINIT=2 iEin=1 iLS=130 factor=`echo $fitfactor` IVisflagINPUT=0 >> $hydrofolder/results/RunRecord_results-avg_etaBYsTparm_`echo $CPvisflag`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization #' $CPvisflag 'and results-avg-1.' >> $outfile
	cp $ICfile $hydrofolder/results/
	#outputfolder=$basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`/NEW_TDEP_V`echo $CPvisflag`_results-avg-1
	#outputfolder=$hydrofolder/NEW_TDEP_V`echo $CPvisflag`_results
	dir1=$basedirectory/RESULTS/RESULTS_etaBYs_`echo $TVstring`
	individualResultsDirectory=results-avg-1
	outputfolder=$dir1/$individualResultsDirectory
	mv $hydrofolder/results $outputfolder
	#mv $hydrofolder/results $hydrofolder/TV`echo $CPvisflag`_results-avg-1
	echo 'Finished running hydro for (eta/s)(T) =' $TVstring
	####################################################################################
	#cp ~/HBTPlumberg/get_anisotropic_flows_src/get_anisotropic_flows $hydrofolder/TV`echo $CPvisflag`_results-avg-1/get_anisotropic_flows
	#$hydrofolder/TV`echo $CPvisflag`_results-avg-1/get_anisotropic_flows &
	####################################################################################
	#cp $HBTfolder/process_event_w_df $hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event_w_df
	#cp $HBTfolder/process_event_wo_df $hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event_wo_df
	#$hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event_w_df &
	#$hydrofolder/TV`echo $CPvisflag`_results-avg-1/process_event_wo_df &
	####################################################################################
	echo 'Moved hydro results to' $outputfolder >> $outfile
	echo '' >> $outfile
	echo 'Starting HBT calculations...' >> $outfile
	cp $HBTfolder/process_event_w_df $outputfolder/process_event_w_df
	$outputfolder/process_event_w_df &
	cp $HBTfolder/process_event_wo_df $outputfolder/process_event_wo_df
	$outputfolder/process_event_wo_df &
	#cp $HBTfolder/process_event_wo_df_SHORT $outputfolder/process_event_wo_df_SHORT
	#$outputfolder/process_event_wo_df_SHORT &
	echo 'Finished HBT calculations.' >> $outfile
#done

\rm -rf $basedirectory/$2

echo 'Finished all calculations.' >> $outfile
