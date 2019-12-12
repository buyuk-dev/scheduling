#!/bin/bash

index=$1


function compute {
    n=$1
    instance="instances/${index}/in${index}_${n}.txt"
    solution="output/out${index}_${n}.txt"

    value=$(./schedule.py --algorithm urgent $instance)
    runtime=$(echo "$value" | grep "duration")
    scheduling=$(echo "$value" | grep -v "duration")

    echo "$scheduling" > $solution

    validate=$(./validate.py --instance $instance --solution $solution)
    echo "$index_$n: $runtime $validate"
}


for ((n=50; n<=500; n+=50)); do
    compute $n
done
