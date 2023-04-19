#!/bin/bash

i=0

while [ $i != 1 ]
do
docker run -d -it --name test_container$i -v $PWD/container$i:/src --security-opt seccomp=/PATH/TO/JSON/FILE python bash
((i++))
done