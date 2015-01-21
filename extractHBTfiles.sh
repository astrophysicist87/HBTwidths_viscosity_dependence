#!/bin/bash

zipfile=$1			#name of zipfile to extract file(s) from
basedirectoryname=$2		#probably something like 'results'
index=$3			#third argument to script specifies results folder (from which) to extract
targetdirectoryname=$4		#where to extract file(s) to
scope=$5			#looks for specified file(s) to extract
				#options are:
				#	- 'FOsurface'
				#	- 'all'
overwriteflag=true		#if file exists, "true" means to overwrite it
suppressoutflag=false

function extract () {
	if [[ $overwriteflag == "true" ]]
	then
		if [[ -e $basedirectoryname-`echo $index`/$1 ]]
		then
			\rm $basedirectoryname-`echo $index`/$1
		fi
		unzip $zipfile $basedirectoryname-`echo $index`/$1 -d $targetdirectoryname/
	elif [[ $overwriteflag == "false" ]]
	then
		if [[ -e $basedirectoryname-`echo $index`/$1 ]]
		then
			:
		else
			unzip $zipfile $basedirectoryname-`echo $index`/$1 -d $targetdirectoryname/
		fi
	else
		\rm -i $basedirectoryname-`echo $index`/$1
		unzip $zipfile $basedirectoryname-`echo $index`/$1 -d $targetdirectoryname/
	fi
}

function extractall () {
	unzip $zipfile $basedirectoryname-`echo $index`/* -d $targetdirectoryname/
	if [[ $suppressoutflag == "limited" ]]
	then
		echo 'Successfully extracted all files in' $basedirectoryname-`echo $index`/ 'to' $targetdirectoryname/
	fi
}

if [[ $5 == 'FOsurface' ]]
then
	if [[ $suppressoutflag == "true" ]]
	then
		extract decdat2.dat &> /dev/null
		extract decdat_mu.dat &> /dev/null
		extract surface.dat &> /dev/null
	elif [[ $suppressoutflag == "limited" ]]
	then
		extract decdat2.dat &> /dev/null
		echo 'Successfully extracted to' $targetdirectoryname/$basedirectoryname-`echo $index`/decdat2.dat
		extract decdat_mu.dat &> /dev/null
		echo 'Successfully extracted to' $targetdirectoryname/$basedirectoryname-`echo $index`/decdat_mu.dat
		extract surface.dat &> /dev/null
		echo 'Successfully extracted to' $targetdirectoryname/$basedirectoryname-`echo $index`/surface.dat
	else
		extract decdat2.dat
		extract decdat_mu.dat
		extract surface.dat
	fi
elif [[ $5 == 'all' ]]
then
	if [[ $suppressoutflag == "true" ]]
	then
		extractall &> /dev/null
	else
		extractall
	fi
else
	echo 'Error in extractHBTfiles.sh: specified options not currently supported'
	exit 1
fi
