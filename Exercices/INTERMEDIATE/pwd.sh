#!/bin/bash
#Generate pseudorandom 8-character passwords, using characters in the ranges [0-9], [A-Z], [a-z]. Each password must contain at least two digits.
{ shuf -r -n6 -e {A..Z} {a..z}; shuf -r -n8 -e {0..9}{2,}; } | shuf  | tr -d $'\n'| fold -w 8 | head -n 1
