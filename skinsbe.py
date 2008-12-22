#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
from urllib import FancyURLopener, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer



# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def skinsbe_parse(link):
    skinsbe_list = [] # the list that will contain the href tags
    skinsbe_list.append(link['href'])
    for i in skinsbe_list:
        print i
        # get every page linked from the skinsbe links
        image_page = myopener.open(i)
        Rimage_page = image_page.read()
        page_soup = BeautifulSoup(Rimage_page)
        # find the src attribute which contains the real link of skinsbe's images
        src_links = page_soup.findAll('img', id='theimage')
        skinsbe_src = []
        for li in src_links:
            print li
            skinsbe_src.append(li['src']) # add all the src part to a list

        # Close the page
        image_page.close()

        # generate just the filename of the image to be locally saved
        save_extension = re.sub('^\./files/', '', skinsbe_src[0]) 
        download_url = 'http://skinsbe.com/files/' + save_extension

        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
