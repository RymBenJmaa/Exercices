#!/bin/bash
#Print (to stdout) all prime numbers between 60000 and 63000. The output should be nicely formatted in columns (hint: use printf).
factor {60000..63000} | awk 'NF==2{printf "------- \n %s \n", $2}'

 

