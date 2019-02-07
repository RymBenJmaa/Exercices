#!/bin/bash

#Certain database and spreadsheet packages use save-files with the fields separated by commas, commonly referred to as comma-separated values or CSVs. Other applications often need to parse these files.
#Reformat the data and print it out to stdout in labeled, evenly-spaced columns.
parse(){

awk  -F',' 'BEGIN{print "LastName\t FirstName\t Address\t City\t State\t PostalCode\t PhoneNumber"
              print "-------------\t-------------\t-------------\t-------------\t-------------\t-------------\t------------- " }
           {   print $1, "\t", substr( gsub(" ", "")$2,2), "\t", substr( gsub(" ", ".")$3,2), "\t", substr( gsub(" ", "")$4,2), "\t",substr( gsub(" ", "")$5,2), "\t", substr( gsub(" ", "")$6,2), "\t",substr( gsub(" ", "")$7,2) }' $1

}
parse $1| column -t
