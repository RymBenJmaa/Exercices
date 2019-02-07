#!/bin/bash
#Given a process ID (PID) as an argument, this script will check, at user-specified intervals, whether the given process is still running. You may use the ps and sleep commands.


watch -n $2 ps $1 

