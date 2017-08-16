import os
import subprocess
import sys
import argparse


def get_all_input(directory,extention):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
             # Join the two strings in order to form the full filepath.
            if extention:
                if filename[-3:] == '.' + extention:                 
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)  # Add it to the list.
            else:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
    
    return file_paths  # Self-explanatory. 



def write_gdb(bp,arg):
    f = open('cmd.gdb','w')
    f.write('b* '+bp + '\nr ' + arg)
    f.close()


def main():
    if len(sys.argv) < 4:
        print "Using: python scan.py <input_source_file> <excutable> <breakpoint> [extention(.py ...)]"
        sys.exit()
    input_souce = sys.argv[1]
    excutable = sys.argv[2]
    breakpoint = sys.argv[3]
    extention = sys.argv[4] if len(sys.argv) == 5 else None
    
    all_input = get_all_input(input_souce,extention)

    cmd = ['gdb', '--batch','--command=cmd.gdb','--args',excutable]
  
    
    for i in all_input:
    
        write_gdb(breakpoint,i)
        print '[+] Scanning file',i
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        out, err = p.communicate()
        #print out,err
        if 'Breakpoint 1,' in out:
            print "--------------------------- FOUNDED -----------------------",i
            break


if __name__ == "__main__":
    main()