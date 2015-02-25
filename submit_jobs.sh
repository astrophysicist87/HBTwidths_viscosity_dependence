#! /usr/bin/env bash

# first argument: index of first results folder to process
# second argument: index of final results folder to process

if [ ! -d "PlayGround" ]
then
	mkdir PlayGround
fi

for ((idx=$1; idx<=$2; idx++))
do
	#cp -r EBE-Node PlayGround/copy`echo $idx`
	cp -r ~/iEBE/EBE-Node PlayGround/copy`echo $idx`
	#bash background_driver.sh $idx PlayGround/copy`echo $idx` &
        #bash background_driver_alternate.sh $idx PlayGround/copy`echo $idx` &
        bash background_driver_AVG.sh PlayGround/copy`echo $idx` &
	#CORRECT: bash background_driver_etaBYs_of_T.sh $idx PlayGround/copy`echo $idx` &
	#bash background_driver_etaBYs_of_T_AVG.sh $idx PlayGround/copy`echo $idx` &
	#bash background_driver_etaBYs_of_T_AVG.sh 1 PlayGround/copy`echo $idx` $idx &
done

wait
