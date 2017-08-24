#!/usr/bin/python
#
# Purpose: gather compare and display OS/NB hostname(s)/IP(s) of current localhost 
#
#

from __future__ import print_function
import os, commands, re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


self = commands.getoutput('hostname')

def mynameis():

    # Obtain OS hostname:
    self = commands.getoutput('hostname')
    print (bcolors.WARNING + 'OS hostname is: ' + self + bcolors.ENDC)
    print(' ')

    # Display all /etc/hosts entries containing the hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    #print(bcolors.OKBLUE + self + ' appears in /etc/hosts file as:' + bcolors.ENDC)
    print(' ')
    hstsfile = open('/etc/hosts', 'r')
    for line in hstsfile:
        if str(self) in line:
            print(bcolors.WARNING + self + ' appears in hosts file as ' + line, end='' + bcolors.ENDC)
            #print(re.findall(self, line))
        else:
            print(bcolors.FAIL + self + ' does not appear in /etc/hosts file!' + bcolors.ENDC)
            return()
    hstsfile.close()
    print(' ')
    print(' ')

    # Resolve hostname with dig:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print(bcolors.OKBLUE + 'dig reports for ' + self + ':' + bcolors.ENDC)
    dignfo = commands.getoutput('dig ' + str(self))
    answrregex = re.compile(r'ANSWER: \d')
    hits = answrregex.search(dignfo)
    answrvalregex = re.compile(r'\d')
    answrval = answrvalregex.search(hits.group())
    if (hits.group()) == 'ANSWER: 0':
        print(bcolors.FAIL + 'DNS has no record of ' + self + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + 'DNS resolved ' + self + bcolors.ENDC)
        print(dignfo)
    print(' ')
    print(' ')


def nbthinksiam():

    # Display all bp.conf entries containing the hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print(bcolors.OKBLUE + self + ' appears in bp.conf file as:' + bcolors.ENDC)
    print(' ')

    # Open bp.conf to read, read it:
    bpconf = open('/usr/openv/netbackup/bp.conf', 'r')
    for line in bpconf:
        if str(self) in line:
            print(bcolors.WARNING + line, end='' + bcolors.ENDC)

    # Close bp.conf file:
    bpconf.close()
    print(' ')
    print(' ')

    # Display all vm.conf entries with hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    vmconf = open('/usr/openv/volmgr/vm.conf', 'r')
    print(bcolors.OKBLUE + self + ' appears in vm.conf file as:' + bcolors.ENDC)
    print(' ')
    for line in vmconf:
        if self in line:
            print(bcolors.WARNING + line + bcolors.ENDC)
    vmconf.close()
    print(' ')
    print(' ')

    # Display EMM db info about hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print(bcolors.OKBLUE + 'EMM info about' + self + ' :' + bcolors.ENDC)
    print(' ')
    emminfo = commands.getoutput('/usr/openv/netbackup/bin/admincmd/nbemmcmd -listhosts -verbose -display_server -machinename ' + self + ' -machinetype master | grep -v NBEMMCMD | grep -v "Command completed successfully"')
    print(bcolors.WARNING + emminfo + bcolors.ENDC)
    print(' ')
    print(' ')

    # Display nbdb configurations involving the hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    vxdbms = open('/usr/openv/db/data/vxdbms.conf', 'r')
    print(bcolors.OKBLUE + self + ' appears in vxdbms.conf file as:' + bcolors.ENDC)
    print(' ')
    for line in vxdbms:
        if self in line:
             print(bcolors.WARNING + line + bcolors.ENDC)
    vxdbms.close()
    print(' ')
    print(' ')
    srvrconf = open('/usr/openv/var/global/server.conf', 'r')
    print(bcolors.OKBLUE + self + ' appears in server.conf file as:' + bcolors.ENDC)
    print(' ')
    for line in srvrconf:
        if self in line:
           print(bcolors.WARNING + line + bcolors.ENDC)

    srvrconf.close()
    print(' ')
    print(' ')
 
    srvrname = open('/usr/openv/db/bin/servername', 'r')
    print(bcolors.OKBLUE + self + ' appears in /usr/openv/db/bin/servername as:' + bcolors.ENDC)
    print(' ')
    for line in srvrname:
        if self in line:
            print(bcolors.WARNING + line + bcolors.ENDC)
    srvrname.close()
    print(' ')
    print(' ')
    print(' ')


def peername():
    self = commands.getoutput('hostname')
    # Display peername info about hostname:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    print(bcolors.OKBLUE + 'Peername info about' + self + ' :' + bcolors.ENDC)
    pn = commands.getoutput('/usr/openv/netbackup/bin/bpclntcmd -pn')    
    for line in pn:
        print(line.rstrip('\n'))
        #if "expecting" in line:
        #    print(bcolors.WARNING + self + ' is ' + line + bcolors.ENDC)
    #print(bcolors.WARNING + pn + bcolors.ENDC)
    print(' ')
    print(' ')


if __name__ == '__main__':
    mynameis()
    nbthinksiam()
    print ('completed')




# NB bptestbpcd/bpclntcmd outputs:


