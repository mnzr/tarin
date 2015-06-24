#!/usr/bin/env python
# tfile = tarfile.open(filename)
# tfile.extractall('/opt')


from sys import argv
import tarfile


script, filename = argv

txt = tarfile.open(filename)

print "Here's your file %r:" % filename
'''
list = []
list = txt.list(verbose=False)
print list[1]
'''
print txt.getnames()[0]

"""
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
"""
