#!/bin/bash
#Backup
#Archive as a "tarball" (*.tar.gz file) all the files in your home directory tree (/home/your-name) that have been modified in the last 24 hours. Hint: use find.

#Optional: you may use this as the basis of a backup script.


OF=myBackup$(date +%Y%m%d).tar.gz
 
sudo find /home/rym -mtime -1 -type f -print | sudo xargs tar czvf $OF
