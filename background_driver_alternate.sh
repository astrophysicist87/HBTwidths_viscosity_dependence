#! /usr/bin/env bash

# first argument: index of results folder
# second argument: local copy of EBE-Node

basedirectory=~/HBTwidths_viscosity_dependence
ICsfolder=$basedirectory/ICs/results-
hydrofolder=$basedirectory/$2/VISHNew

cp $ICsfolder`echo $1`/sd_event_*_block.dat $hydrofolder/Initial/InitialSd.dat

outfile=results-`echo $1`-OSCAR_hydro_processing.out
echo 'Started running at' `date` >> $outfile

for etaBYsval in 0.00 0.05 0.10 0.15 0.20
do
	echo 'Working on eta/s =' $etaBYsval'...' >> $outfile
	#run hydro
	\rm -fr $hydrofolder/results
	mkdir $hydrofolder/results
	runrecordfilename="RunRecord_results-`echo $1`_etaBYs_`echo $etaBYsval`.txt"
	echo 'Running hydro for eta/s =' $etaBYsval 'and results-'$1'...' >> $outfile
	(cd $hydrofolder
	./VISHNew.e IEOS=7 Edec=0.18 T0=0.6 vis=`echo $etaBYsval` IINIT=2 iEin=1 iLS=130 factor=1.0 NDX=1 NDY=1 NDT=1 >> $hydrofolder/results/$runrecordfilename
	cd $basedirectory)
	echo 'Finished hydro for eta/s =' $etaBYsval 'and results-'$1'.' >> $outfile
	lim=`grep ' time= ' $hydrofolder/results/$runrecordfilename | tail -1 | awk '{print $1}'`
	#awk -v v1=$lim '$1<=v1' $hydrofolder/results/OSCAR2008H.dat >> $hydrofolder/results/OSCAR2008H_trunc.dat
	#\rm $hydrofolder/results/OSCAR2008H.dat
	#bash process_OSCAR.sh $hydrofolder/results/OSCAR2008H_trunc.dat
	#zip $hydrofolder/results/OSCAR2008H_trunc.dat.zip $hydrofolder/results/OSCAR2008H_trunc.dat* &> $outfile

	#move OSCAR output to final results directory
	finalresultsdir="$basedirectory/RESULTS/RESULTS_etaBYs_`echo $etaBYsval`/results-`echo $1`-DENSE"
	#echo 'Zipped OSCAR output'
	mv $hydrofolder/results $finalresultsdir
	#\rm $hydrofolder/results/OSCAR2008H_trunc.dat*
	echo 'Moved hydro results to' $finalresultsdir >> $outfile
	echo '' >> $outfile
done

echo 'Finished running at' `date` >> $outfile

\rm -rf $basedirectory/$2
