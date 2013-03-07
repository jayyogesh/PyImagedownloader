#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imgur
import lxml.html
from os.path import join, getsize, isfile

class TestImgur(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://imgur.com/ysu1C'
        self.image_url = 'http://i.imgur.com/ysu1C.jpg'
        self.example_iur_page = """<!doctype html><html lang="en"><head><title>imgur: the simple image sharer </title><meta name="robots" content="follow,index" /><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><meta name="keywords" content="images, funny pictures, twitter photo, tweet photo, image host, image upload, image sharing, image resize" /><meta name="description" content="Imgur is used to share photos with social networks and online communities, and has the funniest pictures from all over the Internet." /><link rel="icon" href="//imgur.com/include/favicon.ico" type="image/x-icon" /><link rel="shortcut icon" href="//imgur.com/include/favicon.ico" type="image/x-icon" /><link rel="stylesheet" href="//imgur.com/include/styles/main-style.css?060611" type="text/css" /><link rel="alternate" type="application/rss+xml" title="Imgur Gallery" href="http://feeds.feedburner.com/ImgurGallery?format=xml" /><meta name="medium" content="image" /><link rel=image_src href=http://i.imgur.com/ysu1C.jpg /><link rel="stylesheet" href="/include/styles/trending-inside.css?050511" type="text/css" /><link rel="stylesheet" href="/include/styles/referrer.css?042711" type="text/css" /><!--[if IE 9]><link rel="stylesheet" href="//imgur.com/include/styles/ie-sucks.css?050511" type="text/css" /><![endif]--><script type='text/javascript' src='//partner.googleadservices.com/gampad/google_service.js'></script><script type='text/javascript'> if(typeof GS_googleAddAdSenseService == 'function') { GS_googleAddAdSenseService("ca-pub-4470792243209857"); GS_googleEnableAllServices(); } </script><script type='text/javascript'> if(typeof GA_googleAddSlot == 'function') { GA_googleAddSlot("ca-pub-4470792243209857", "Moderated_300x250"); GA_googleAddSlot("ca-pub-4470792243209857", "Unmoderated_300x250"); } </script><script type='text/javascript'> if(typeof GA_googleAddSlot == 'function') { GA_googleFetchAds(); } </script></head><body><div id="topbar"><div class="left"><ul><li><a href="http://imgur.com/tools/">tools</a></li><li><a href="http://imgur.com/gallery/">gallery</a></li></ul></div><div class="right"><ul><li><a class="dot" href="https://imgur.com/signin">sign in</a></li><li><a href="https://imgur.com/register">register</a></li></ul></div></div><div id="underbar" class="clear"></div>   <div class="nodisplay"> Imgur is used to share photos with social networks and online communities, and has the funniest pictures from all over the Internet. </div><div id="header"><a href="/"><img alt="the simple image sharer" src="/images/imgur-small.gif" /></a></div><div id="content" class="inside"><div class="left"><div class="panel"><div class="image textbox"><a href="http://i.imgur.com/ysu1C.jpg"><img src="http://i.imgur.com/ysu1C.jpg" /></a></div><div id="under-image"><div class="info textbox nobottom"> Submitted 4 months ago : 2,674 views : 739.22 MB bandwidth </div><div id="social"><ul><li title="Tweet This"><span class="twitter_custom" onclick="javascript:new_window('http://twitter.com/share?url=http://imgur.com/ysu1C', 550, 425)">&nbsp;</span></li><li title="Share This on Facebook"><span class="facebook_custom" onclick="javascript:new_window('http://www.facebook.com/sharer.php?u=http://imgur.com/ysu1C', 755, 425)">&nbsp;</span></li><li title="Submit This to Reddit"><span class="reddit_custom" onclick="javascript:new_window('http://reddit.com/submit?url=http://imgur.com/ysu1C', 900, 720)">&nbsp;</span></li><li title="Submit This to Digg"><span class="digg_custom" onclick="javascript:new_window('http://digg.com/submit?phase=2&url=http://imgur.com/ysu1C', 1060, 655)">&nbsp;</span></li><li title="Submit This to Stumble Upon"><span class="stumbleupon_custom" onclick="javascript:new_window('http://www.stumbleupon.com/submit?url=http://imgur.com/ysu1C', 1060, 500)">&nbsp;</span></li><li title="Email This"><a href="javascript:void(0)" class="addthis_button_email st_email_custom"><span>&nbsp;</span></a></li><li title="More Sharing Options"><span class="addthis_button st_sharethis_custom"><span>&nbsp;</span></span></li></ul></div><div class="clear"></div></div><div class="small links"><div class="right"><a href="/download/ysu1C">Download full resolution</a> : <a href="/ysu1C?tags">Get embed codes</a></div><div class="clear"></div></div></div><div id="footer"><div id="copyright">© 2011 Imgur, LLC. All rights reserved.</div><div class="right"><a href="http://imgur.com/blog/" title="the simple imgur blog">blog</a><a href="http://imgur.userecho.com/" title="have something to say?">feedback</a><a href="http://imgur.com/stats/" title="view site statistics">site stats</a><a href="http://imgur.com/faq" title="have a question?">faq</a><a href="http://imgur.com/removalrequest" title="submit an image removal request">request deletion</a><a href="http://imgur.com/contact" title="contact imgur">contact</a><a href="http://imgur.com/tos" title="terms of service">terms</a><a href="http://imgur.com/register/upgrade" title="imgur pro">go pro</a><a href="http://api.imgur.com" title="the imgur API">api</a></div><div class="clear"></div></div></div><div class="right"><div class="panel"><div class="next-prev"><h2 class="textbox left">Today's best images</h2><div class="right"><a href="/gallery" class="browse" ><input type="button" class="button-medium" value="browse" onclick="javascript:window.location='/gallery'" /></a></div><div class="clear"></div></div><div class="thumbnails"><div class="thumb"><a href="/gallery/8JKXo"><img src="http://i.imgur.com/8JKXob.jpg" title="The Land Before What?<p>147,296 views : 3 hours ago</p>" /></a></div><div class="thumb"><a href="/gallery/UU9y1"><img src="http://i.imgur.com/UU9y1b.jpg" title="Work.<p>157,689 views : 11 hours ago</p>" /></a></div><div class="thumb"><a href="/gallery/w1zDT"><img src="http://i.imgur.com/w1zDTb.jpg" title="Best pickup line ever.<p>146,397 views : 11 hours ago</p>" /></a></div><div class="thumb"><a href="/gallery/i7zEm"><img src="http://i.imgur.com/i7zEmb.jpg" title="I should have known.<p>73,457 views : 9 hours ago</p>" /></a></div><div class="thumb"><a href="/gallery/vNwc9"><img src="http://i.imgur.com/vNwc9b.jpg" title="How we sleep while we&amp;#039;re single.<p>113,139 views : 13 hours ago</p>" /></a></div><div class="thumb"><a href="/gallery/Ugjb2"><img src="http://i.imgur.com/Ugjb2b.jpg" title="Lebowski Fest: Lego Walter<p>34,481 views : 13 hours ago</p>" /></a></div><div class="clear"></div></div></div><div class="advertisement"><div class="imgur-ad"><script type='text/javascript'>
 GA_googleFillSlot("Unmoderated_300x250");
 </script>

 </div><div class="ad-text"> Advertisement: <a href="/register/upgrade">pro users don't see ads</a></div></div></div><div class="clear"></div></div>  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script><script type="text/javascript" src="//imgur.com/include/js/base.js?60211"></script><script type="text/javascript" src="//s7.addthis.com/js/250/addthis_widget.js#username=imgur"></script><script type="text/javascript"> $('.thumbnails img').tipsy({ gravity: 'n', opacity: 1, offset: -8, html: true });  $('#social li').tipsy({ gravity: 'sw', opacity: 1 }); </script><script type="text/javascript"> var _gaq = _gaq || []; _gaq.push(['_setAccount', 'UA-6671908-2']); _gaq.push(['_setDomainName', 'none']); _gaq.push(['_trackPageview']);  (function() {   var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;   ga.src = ('https:' == document.location.protocol ? 'https://ssl' : '//www') + '.google-analytics.com/ga.js';   var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })(); </script><script type="text/javascript"> var _qevents = _qevents || []; (function() { var elem = document.createElement('script'); elem.src = (document.location.protocol == "https:" ? "https://secure" : "//edge") + ".quantserve.com/quant.js"; elem.async = true; elem.type = "text/javascript"; var scpt = document.getElementsByTagName('script')[0]; scpt.parentNode.insertBefore(elem, scpt); })(); </script><script type="text/javascript"> _qevents.push({ qacct:"p-f8oruOqDFlMeI" }); </script><noscript><div class="nodisplay"><img src="//pixel.quantserve.com/pixel/p-f8oruOqDFlMeI.gif" border="0" height="1" width="1" alt="Quantcast"/></div></noscript>    </body></html>"""
        self.iur = imgur.ImgurParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.iur.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imgur_get_image_src(self):
        self.imgur_src = self.iur.imgur_get_image_src(lxml.html.fromstring(self.example_iur_page))
        self.assertIsInstance(self.imgur_src, list)

    def test_imgur_save_image(self):
        urllist = [ self.image_url ]
        savefile = join(self.basedir, 'ysu1C.jpg')
        self.iur.imgur_save_image(urllist)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImgur)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
