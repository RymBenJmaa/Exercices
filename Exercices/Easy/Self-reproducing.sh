#!/bin/bash
#Write a script that backs itself up, that is, copies itself to a file named backup.sh.

#Hint: Use the cat command and the appropriate positional parameter.
cat $0 > backup.sh
