#!/bin/bash

njobs=50	# defines batch size

outfilename="History/submit_jobs_record_`date +%F`.out"
outfile=`get_filename $outfilename`		# get_filename checks to see if outfilename already exists
						# and attaches an appropriate index to the end to ensure that it is a new file

for ((i=1; i<=1000; i += $njobs))
do
	bvar1=$i
	bvar2=$[i+$njobs-1]
	echo 'Run jobs from' $bvar1 'to' $bvar2 'at' `date` >> $outfile
	bash submit_jobs.sh $bvar1 $bvar2
	#bash submit_get_anisotropic_flows_jobs.sh $bvar1 $bvar2
	#bash submit_process_event_jobs.sh $bvar1 $bvar2
	#bash submit_get_EdNd3p_cfs_jobs.sh $bvar1 $bvar2
done
