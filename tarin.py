#!/usr/bin/env python
import os
import stat
import click
import tarfile

"""
TODO:
    1. Extract the file according to type   [DONE]
    2. Find the executable file             [IN PROGRESS]
    3. Shortcut to right places
"""


# The default command is tarin
@click.command()
@click.option('--exe', help='Name of the executable to create symlink.')
@click.argument('filename', required=False)
def tarin(exe, filename):
    """ This script takes a compressed file and uncompresses it."""
    # Extractibg the file to /opt
    tfile = tarfile.open(filename)
    tfile.extractall('/opt')
    exec_folder = '/opt/' + tfile.getnames()[0] + '/'
    print "Folder copied to " + exec_folder

    # Finding the executable

    if not exe:
        executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
        list = []
        i = 1
        print "Executable files found:"
        os.chdir(exec_folder)
        for filename in os.listdir('.'):
            if os.path.isfile(filename):
                st = os.stat(filename)
                mode = st.st_mode
                if mode & executable:
                    list.append(filename)
                    print("[" + str(i) + "] " + filename)
                    i += 1

        inp = input("Which executable do you want to link?\n> ")
        choice = list[inp - 1]
        print"Your choice: " + choice

    else:
        choice = exe

    os.symlink(choice, '/usr/local/bin/' + choice)



if __name__ == '__main__':
    tarin()
