#!/bin/bash

#Parse /etc/passwd, and output its contents in nice, easy-to-read tabular form.

parse(){

awk  -F':' 'BEGIN{print "UserID\t Pwd\t UID\t GID\t UserInfo\t HomeDir\t Shell"
              print "---------------\t-----\t------\t -----\t-------------------------------\t\t-----------------------\t------------------ " }
           {   print $1, "\t", $2, "\t", $3, "\t", $4, "\t",substr( gsub(" ", "")$5,2), "\t", $6, "\t", $7 }' /etc/passwd

}
parse | column -t
