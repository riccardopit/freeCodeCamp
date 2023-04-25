# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
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

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of content span tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
    # Look at the parts of span tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    count = count + 1
    sum = sum + int(tag.contents[0])
print('Count',count)
print('Sum',sum)