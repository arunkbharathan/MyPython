#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def MyFun(link):
  match=re.search(r'-\w\w\w\w-(\w\w\w\w)',link)
  return match.group(1)


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  match1 = re.search(r'_(\w+[.]\w+[.]\w+)',filename)
  if match1:
    serverName = match1.group(1)
    fyle = open(filename,'rU')
    text = fyle.read()
    links=re.findall(r'\S+puzzle\S+',text)
    links=sorted(links)
    
    match=re.search(r'-\w\w\w\w-(\w\w\w\w)',links[1])
    if match:
      links=sorted(links,key=MyFun)
    
    
    Links=[]
    puzzleLinks=[]
    for link in links:
      if link not in puzzleLinks:
        puzzleLinks.append(link)
        Links.append('http://'+serverName+link)
    
    return Links
  
    
    

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
 
  try:
    path = os.path.abspath(dest_dir)
    os.mkdir(path)
  except OSError,e:
    if e.errno==13:
      print "Can't create : Permission Denied"
      return
  count=0
  total = len(img_urls)
  fyle=open(path+'/index.html','w')
  fyle.write('<verbatim>\n<html>\n<body>\n')

  print "Downloading Images"
  for img_url in img_urls:
    fyle.write('<img src="')
    urllib.urlretrieve(img_url,path+'/img'+str(count))
    fyle.write(path+'/img'+str(count))
    fyle.write('">')
    count+=1
    percent=(count*100)/total
    print "%d%%"%(percent)

  fyle.write('\n</body>\n</html>\n')
  fyle.close()
  print "\nOK"    
  
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
   
  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()


