#! /usr/bin/env bash

# at present only care about using SurfaceX.dat files

#nevs = 1000
#TdepV = 1
nevs=$1
TdepV=$2

outfilename="/home/plumberg.1/HBTwidths_viscosity_dependence/History/generate_transverse_flow_profile_data_record_`date +%F`.out"
outfile=`get_filename $outfilename`		# get_filename checks to see if outfilename already exists
						# and attaches an appropriate index to the end to ensure that it is a new file

echo 'ebs = 0.08' &>> $outfile
echo 'nevs =' $nevs &>> $outfile
echo '(eta/s)(T) version =' $TdepV &>> $outfile

workingDirectoryStem=NEW_TDEP_V`echo $TdepV`/NEW_TDEP_V`echo $TdepV`_results-

for ((i=1; i<=$nevs; i++))
do
	# generate Surface_posX.dat files
	surfaceFile=$workingDirectoryStem`echo $i`/SurfaceX.dat
	newSurfaceFile=$workingDirectoryStem`echo $i`/Surface_posX.dat
	awk '$4 >= 0' $surfaceFile > $newSurfaceFile
	echo 'Generated all */Surface_posX.dat files' &>> $outfile
	echo  &>> $outfile
	
	# get SurfaceX data interpolated linearly to y=0
	# sort output by nearest-neighbor in tau-rT-vT space and on tau alone
	nnSortedSurfaceFile=$workingDirectoryStem`echo $i`/vT_vs_X_nnSORTED.out
	tauSortedSurfaceFile=$workingDirectoryStem`echo $i`/vT_vs_X_tauSORTED.out
	python interpolate_FOsurface_and_SORT.py $newSurfaceFile &>> $outfile
	sort -k1,1n $nnSortedSurfaceFile > $tauSortedSurfaceFile
	
	# get indexed files
	nnIndexedSurfaceFile=$workingDirectoryStem`echo $i`/vT_vs_X_nnINDEXED.out
	tauIndexedSurfaceFile=$workingDirectoryStem`echo $i`/vT_vs_X_tauINDEXED.out
	awk '{printf NR"   "; for (i=2; i<=NF; i++) {printf $i"   "}; printf "\n"}' $nnSortedSurfaceFile > $nnIndexedSurfaceFile
	awk '{printf NR"   "; for (i=2; i<=NF; i++) {printf $i"   "}; printf "\n"}' $tauSortedSurfaceFile > $tauIndexedSurfaceFile
done

python get_mean_and_variance_transverseflowprofile.py &>> $outfile

















# End of file
