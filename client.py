#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Simple client web per saber el Free eBook actual de packtpub.com

@author: albeertito7 ajkghfksdah
"""

import urllib2
from bs4 import BeautifulSoup

class Client(object):

	def get_webpage(self, page):
		f = urllib2.urlopen(page)
		htmlpage = f.read()
		f.close()
		return htmlpage

	def search_title(self, html):
		bs = BeautifulSoup(html, "lxml")
		title = bs.find("div", "dotd-title").text
		return title
	
	def print_results(self, title):
		print '\nFree eBook Title ----------> %s\n' % title.strip()

	def main(self):
		webpag = self.get_webpage('http://www.packtpub.com/packt/offers/free-learning/')
		title = self.search_title(webpag)
		self.print_results(title)
	
	
if __name__ == "__main__":
	c = Client()
	c.main()
