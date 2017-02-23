#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Simple client web per saber el Free eBook actual de packtpub.com

@author: albeertito7
"""

import urllib2
from bs4 import BeautifulSoup

class Client(object):

	def get_webpage(self, page):
		f = urllib2.urlopen(page)
		html = f.read()
		f.close()
		return html

	def search_title(self, html):
		bs = BeautifulSoup(html, "lmxl")
		title = bs.find("div", "dotd-title").text
		return title
	
	def print_results(title):
		print '\nFree eBook Title ----------> %s\n' % title

	def main(self):
		web = self.get_webpage('http://www.packtpub.com/packt/offers/free-learning/')
		results = self.search_title(web)
		print_results(results)
	
	
if __name__ == "__main__":
	c = Client()
	c.main()
