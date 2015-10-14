#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
from BeautifulSoup import BeautifulSoup






palavra=sys.argv[1]


URL='http://www.dicio.com.br/'+palavra+'/'

req = urllib2.Request(URL)
resposta = urllib2.urlopen(req)
resultadoHTML = resposta.read()


soup = BeautifulSoup(resultadoHTML)
print soup.prettify()
