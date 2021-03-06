#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2015, Gianluca Fiore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
import os
import string
import htmlentitydefs
import locale
from os.path import join
from urlparse import urlparse
import lxml.html
import logging

# Set locale for string.letters to include all valid characters in it and not only in Ascii
locale.setlocale(locale.LC_ALL, '')
ACCEPTEDCHARS = frozenset(string.letters + string.digits + '(){}[]@-_+"&')

class SaveSource():
    """Class to save an url to a file in the given directory and, optionally,
    also the name given as creditor in another file in the same directory"""

    def __init__(self, page, basedir, url, creditor=""):
        # the variables we'll need
        self.page = page
        self.basedir = basedir
        self.url = url
        self.creditor = creditor
        self.output_dir = ''
        self.response = ''
        self.page_title = ''
        self.neat_title = ''
        self.logger = logging.getLogger('pyimagedownloader')

    def get_page_title(self, response):
        """extract title page"""

        page_title_parsed = lxml.html.fromstring(response)

        try:
            self.page_title = page_title_parsed.find(".//title").text
        except AttributeError:
            # in the case there is no title tag on the page, use the url
            self.logger.debug("No title tag found on %s" % self.url)
            self.page_title = str(self.url)

        # some pages don't return AttributeError but page_title is still None.
        # use the url then
        if not self.page_title:
            self.page_title = str(self.url)
        
        return self.page_title

    def clean_title(self, title):
        """clean title of the page of difficult for the shell characters,
        preserving unicode ones"""
        neat_title = self.decode_htmlentities(title)

        # remove all characters in the regexp plus any whitespace
        neat_title = filter(ACCEPTEDCHARS.__contains__, neat_title) # filter solution
#        neat_title = "".join(re.sub('[\(\)\{\}\[\]"\&\'\’/«»:<>.|,;]', '', neat_title).split()) # manual substitution solution
        self.logger.info("Title of page is %s" % neat_title)
        print(neat_title)

        return neat_title

    def output_dir_exist(self, directory):
        """check whether the output directory already exist and if not creat it"""
        if os.path.isdir(directory):
            os.chdir(directory)
        else:
            os.mkdir(directory, 0740)
            os.chdir(directory)

    def save_source_file(self, url, creditor=""):
        """write the source file (source.txt) and the credits file (credits.txt)"""
        with open('source.txt', "w") as source_file:
            source_file.write("\n\n\nfonte:%s\n" % url)

        if creditor:
            domain_name = self.extract_domain(url)
            with open('credits.txt', "w") as credits_file:
                credits_file.write("\n\ncredits: %s @%s \n" % (creditor, domain_name))

    def save_markdown_source_file(self, url, creditor=""):
        """write a Markdown version of the source (source.txt) and of the credits file (credits.txt)"""
        domain_name = self.extract_domain(url)
        with open('source.mdown', "w") as source_file:
            source_file.write("\n\n\nfonte:[%s](%s)\n" % (domain_name, url))

        if creditor:
            with open('credits.mdown', "w") as credits_file:
                credits_file.write("\n\ncredits: %s @[%s](%s) \n" % (creditor, domain_name, url))
        
    def link_save(self):
        """main method linking all the others in SaveSource class"""
        self.page_title = self.get_page_title(self.page)
        
        self.neat_title = self.clean_title(self.page_title)

        self.output_dir = join(self.basedir, self.neat_title)

        self.output_dir_exist(self.output_dir)

        self.save_markdown_source_file(self.url, self.creditor)

        return self.output_dir

    def extract_domain(self, url):
        """Given an url extract only the domain name (without 'www' and 'com' for
        example)"""
        u = urlparse(url)[1].split('.')
        if len(u) > 3: # for tld like co.uk or com.br
            return u[1] + '.' + u[2] + '.' + u[3]
        else:
            if u[0] == 'www' or 'forum':
                try:
                    return u[1] + '.' + u[2]
                except IndexError:
                    return u[0] + '.' + u[1]
            else:
                return u[0] + '.' + u[1]

    def decode_htmlentities(self, s):
        # Thanks to http://github.com/sku/python-twitter-ircbot/blob/321d94e0e40d0acc92f5bf57d126b57369da70de/html%5Fdecode.py
        def substitute_entity(match):
            ent = match.group(3)
            if match.group(1) == "#":
                # decoding by number
                if match.group(2) == '':
                    # number is in decimal
                    return unichr(int(ent))
                elif match.group(2) == 'x':
                    # number is in hex
                    return unichr(int('0x'+ent, 16))
            else:
                # using a name
                cp = htmlentitydefs.name2codepoint.get(ent)
                if cp:
                    return unichr(cp)
                else:
                    return match.group()
        entity_re = re.compile(r'&(#?)(x?)(\w+);')
        return entity_re.subn(substitute_entity, s)[0]
