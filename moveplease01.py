#!/usr/bin/env python3

''' move and rename files folders
'''
# import libs
import shutil # shell utilities
import os # os operations

def main():
    """ Called at runtime """
    os.chdir('/home/student/mycode/')   # change to dir
    shutil.move('raynor.obj', 'ceph_storage/') # move to storage

    xname = input('What is the new name for kerrigan.obj? ') # prompt for name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() # calls our main function
