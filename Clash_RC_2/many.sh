#!/bin/bash

i=0

while [ $i != 1 ]
do
docker run -d -it --name test_container$i -v /home/vboxuser/Downloads/Clash-RC-2/Clash_RC_2/Code_Runner/container$i:/src --security-opt seccomp=/home/vboxuser/Downloads/Clash-RC-2/Clash_RC_2/seccomp/default.json python bash
((i++))
done
