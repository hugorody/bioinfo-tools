#!/usr/bin/python3

from urllib.request import urlopen

url = urlopen('http://www.....html')
urldata = url.read().decode('utf8').splitlines()

for i in urldata:
  i = i.rstrip()
  print (i)
