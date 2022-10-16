import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url=input('Enter- ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#retrieve tags
tags=soup('a')
for tag in tags:
    tag=tag.get('href', None)
    print(tag)