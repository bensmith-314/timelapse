#!/bin/bash

printf "Do you want to remove all images stored? [y] or [n]\n"
printf ":"
read confirmation

if [[ $confirmation = "y" ]]; then
  eval rm -dr /Users/bensmith/scripts/timelapse/images/
  eval mkdir /Users/bensmith/scripts/timelapse/images/
fi
