#!/bin/bash

index=$1


function compute {
    n=$1
    value=$(cat "instances/${index}/in${index}_${n}.txt" | ./schedule.py --eval)
    echo $value
}


for ((n=50; n<=500; n+=50)); do
    compute $n
done
