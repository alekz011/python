#! /usr/bin/python3

# kxcd.py  --> Load and save KXCD images

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page
   print('Downloading the page %s...' % url)
   res = requests.get(url)
   res.raise_for_status()

   soup = bs4.BeautifulSoup(res.text, "lxml")

    # TODO: Find the URL of the comic image
   comicElem = soup.select('#comic img')
   if comicElem == []:
       print('Could not find comic image')
   else:
       comicUrl = 'http:' + comicElem[0].get('src')
       # Download the image
       print('Downloading image %s...' % (comicUrl))
       res = requests.get(comicUrl)
       res.raise_for_status()
    # TODO: Save the image to ./xkxd
   imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
   for chunk in res.iter_content(100000):
       imageFile.write(chunk)
   imageFile.close()


    # TODO: Get the Prev buttonś url
   prevLink = soup.select('a[rel="prev"]')[0]
   url = 'http://xkcd.com' + prevLink.get('href')

print('Done')

