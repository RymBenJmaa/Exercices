#!/bin/bash

sumUp(){
Num=$1
while [ "$Num" -gt  0 ] 
do

    # get Remainder 
    k=$(( $Num % 10 ))  

    # get next digit 
    Num=$(( $Num / 10 )) 

    # calculate sum of digits   
    s=$(( $s + $k )) 
done   
echo $s 
}
lucky(){
result=$(sumUp $1)

if (( ${#result} > 1))
then 
result=$(sumUp $result)	
fi
if (($result == 7))
	then
	echo $1
fi
}
for i in {1000..10000}
do
  lucky $i
done
