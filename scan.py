import os
import subprocess


def get_all_input():
    return ['1','2','3','4']


def write_gdb(bp,arg):
    f = open('cmd.gdb','w')
    f.write('b* '+bp + '\nr ' + arg)

bp = 'b'

all_input = get_all_input()

cmd = ['gdb', '--batch','--command=cmd.gdb','--args','core']
for i in all_input:
    
    write_gdb(bp,i)
    print '[+] Scanning file',i
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out, err = p.communicate()
    #print out,err
    if 'Breakpoint 1,' in out:
        print "--------------------------- FOUNDED -----------------------",i
        #break
