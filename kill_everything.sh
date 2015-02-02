#!/bin/bash

# get original pid for submitting job
PID1=`greppid wrapper_submit_jobs | awk '{print $2}'`

# get pid for job submitted by PID1
PID2=`ps -ef | awk -v pid=$PID1 '$3==pid' | awk '{print $2}'`

# get pids for all sub-jobs submitted by PID2
PID3=`ps -ef | awk -v pid=$PID2 '$3==pid' | awk '{print $2}'`

#PID4=''
#for ipid in $PID3
#do
#	temp=`ps -ef | awk -v pid=$ipid'$3==pid' | awk '{print $2}'`
#	PID4=`echo $PID4`" $temp"
#done

#echo $PID1
#echo $PID2
#echo $PID3
#echo $PID4

echo 'Killing jobs...'
echo '   --> Killing wrapper_submit_jobs.sh...'
kill -9 $PID1 &> /dev/null
echo '   --> Killing submit_jobs.sh...'
kill -9 $PID2 &> /dev/null
echo '   --> Killing sub-jobs...'
kill -9 $PID3 &> /dev/null
echo '   --> Killing all sub-processes still running...'
kill -9 $PID4 &> /dev/null
echo 'Killed everything.'
