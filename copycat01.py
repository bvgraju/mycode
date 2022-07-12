#!/usr/bin/env python3
''' this is for file processing
'''
# Import used libs
import shutil
import os

def main():
    # change to mycode dir
    os.chdir("/home/student/mycode/")

    # remove before if eists and make a back up copy
    os.system("rm -f /home/student/mycode/5g_research/sdn_network.txt.copy")
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # make an entire copy of directory
    os.system("rm -rf /home/student/mycode/5g_research_backup")    
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
