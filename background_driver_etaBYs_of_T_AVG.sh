#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-avg-10000
hydrofolder=$basedirectory/$1/VISHNew

cp $ICsfolder/sd_elliptical_gaussian_block.dat $hydrofolder/Initial/InitialSd.dat

outfilename="History/NEWresults-avg_hydro_processing.out"
outfile=`get_filename $outfilename`

for CPvisflag in 1 2
do
	echo 'Working on eta/s(T), parametrization #' $CPvisflag'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	echo 'Running hydro for eta/s(T), parametrization #' $CPvisflag 'and results-smooth...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=0.08 IINIT=2 iEin=1 iLS=130 factor=1.0 IVisflagINPUT=`echo $CPvisflag` >> $hydrofolder/results/RunRecord_results-avg_etaBYsTparm_`echo $CPvisflag`.txt
	cd $basedirectory)
	echo 'Finished hydro for eta/s(T), parametrization #' $CPvisflag 'and results-smooth.' >> $outfile
	cp $ICsfolder/sd_elliptical_gaussian_block.dat $hydrofolder/results/
	#mv $hydrofolder/results $basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`_results-avg
	mv $hydrofolder/results $hydrofolder/TV`echo $CPvisflag`_results-smooth
	#echo 'Moved hydro results to' $basedirectory/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $CPvisflag`_results-avg >> $outfile
	echo '' >> $outfile
done

#\rm -rf $basedirectory/$1
