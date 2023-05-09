#!/bin/bash

i=0

while [ $i != 1 ]
do
sudo docker run -d -it --name test_container$i -v $(pwd)/Code_Runner/container$i:/src --security-opt seccomp=$(pwd)/seccomp/default.json python bash
((i++))
done

