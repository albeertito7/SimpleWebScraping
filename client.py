#!/usr/bin/env-python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Simple client web per saber el Free eBook actual de packtpub.com

@author: albeertito7
"""

import urllib2


class Client(object):

	def get_webpage(self, page):
		f = urllib2.urlopen(page)
		html = f.read()
		f.close()
		return html

	def search(self, html):
		pass

	def main(self):
		web = self.get_webpage('http://www.packtpub.com/packt/offers/free-learning/')

if __name__ = __main__:
	c = Client()
	c.main()
