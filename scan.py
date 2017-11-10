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


def check_gdb(breakpoint,cmd):
    write_gdb(breakpoint,"test")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out, err = p.communicate()
    print out
    if "Error in sourced command file:" in err:
        print "[-]Error:" + str(err)
        return False
    return True



def main():
 

    parser = argparse.ArgumentParser(description='Gdb scanner.')

    parser.add_argument('-s', action="store", dest="source",required=True,help='input source folder')
    parser.add_argument('-i', action="store", dest="binary",required=True,help='executable')
    parser.add_argument('-b', action="store", dest="bp",required=True,help="breakpoint")

    args = parser.parse_args()
    input_souce = args.source
    excutable = args.binary
    breakpoint = args.bp
    extention = None



    all_input = get_all_input(input_souce,extention)

    print "[+]Total:"+ str(len(all_input))


    cmd = ['gdb', '--batch','--command=cmd.gdb','--args',excutable]
  
    if check_gdb(breakpoint,cmd):

        for i in all_input:
        
            write_gdb(breakpoint,i)
            print '[+] Scanning file',i
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            out, err = p.communicate()
            #print out,err
            if 'Breakpoint 1,' in out:
                print "--------------------------- FOUNDED -----------------------",i


if __name__ == "__main__":
    main()