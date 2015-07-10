#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dirs):
    abspaths=[]
    for dirname in dirs:
        filenames=os.listdir(dirname)
        for filename in filenames:
            q=re.search(r'\w*__\w+__\w*[.]*\w*',filename)
            if q:
                special_fn= q.group()
                abspaths.append(os.path.join( os.path.abspath(dirname),special_fn))
    return abspaths


def copy_to(src,dst):
    try:
        os.mkdir(dst)
    except OSError,e:
        if e.errno==13:
            print "Can't create: Permission Denied"
            return
    for path in src:
        shutil.copy(path, dst)
    print "Copied"
    return

def zip_to(paths,zippath):
    cmd="zip -j "+ zippath
    for path in paths:
        cmd = cmd+' '+ path
    print "Command to run:", cmd   
    (status, output) = commands.getstatusoutput(cmd)
    if status:    
        sys.stderr.write(output)
        sys.exit(1)
    print output 
    return
    
                
        



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  #from pudb import set_trace;set_trace()
  specialPaths=get_special_paths(args)
  print str(specialPaths)
  if todir:
         copy_to(specialPaths, todir)
  if tozip:
         zip_to(specialPaths, tozip)
                
  
if __name__ == "__main__":
  main()
