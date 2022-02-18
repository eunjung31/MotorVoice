#!/bin/bash

header="header"

for i in *.txt;
do
    cat "$header" "$i" > etc/xx.$$
    mv etc/xx.$$ "$i"

done
