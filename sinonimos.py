#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


#palavra=sys.argv[1].encode('utf-8')  #resolver a conversão pra unicode ainda

palavra=u'feitiço'

palavra=remove_accents(palavra)




########### sinonimos

URL='http://www.sinonimos.com.br/'+palavra+'/'



req = urllib2.Request(URL)
resposta = urllib2.urlopen(req)
resultadoHTML = resposta.read()

soup = BeautifulSoup(resultadoHTML)

classeS=soup.findAll("p",{"class": "sinonimos"})

Sinonimos=[]

for s in classeS:
	Sinonimos.append(s.text)


classePS=soup.findAll("p",{"class": "possiveis-sinonimos"})

PSinonimos=[]

for s in classePS:
	PSinonimos.append(s.text)


print Sinonimos
print PSinonimos


#print soup.prettify()





##################################
#print soup.prettify()
