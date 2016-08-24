# nbwhoami

Purpose: helpful cmdline tool to gather compare and display OS/NetBackup hostname(s)/IP(s) of current localhost

Usage: execute 'python nbwhoami.py'

TODO:
- add conditional to handle missing files during query attempts
- add hostname -f output
- hone the regex (on lines 43-47) to find only exact hostname excluding other characters added to the hostname for grep'ing from files
- add 'bpclntcmd -pn' query to master
- add/change some text colors
