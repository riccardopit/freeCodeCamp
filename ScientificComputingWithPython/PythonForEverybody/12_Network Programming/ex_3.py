# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#collections.Callable has been moved to collections.abc.Callable in python 3.10+.
#Added the reference back to collections before importing the problem library.
import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getsoup(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

myurl = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print('Retrieving: ',myurl)
for tag in range(count):
    actpos = 0  #actual position
    for newurl in getsoup(myurl)('a'):
        actpos = actpos + 1
        if actpos < position:
            continue
        break
    myurl = newurl.get('href', None)    #update url
    print('Retrieving: ',myurl)
print('Last url: ',myurl)