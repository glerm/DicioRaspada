#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import unicodedata
import re
import codecs



def lista_sinonimos(palavra):

	nfkd_form = unicodedata.normalize('NFKD', palavra)
   	palavra_semacento = nfkd_form.encode('ASCII', 'ignore')


	URL='http://www.sinonimos.com.br/'+palavra_semacento+'/'



	req = urllib2.Request(URL)
	resposta = urllib2.urlopen(req)
	resultadoHTML = resposta.read()

	soup = BeautifulSoup(resultadoHTML)


	classeS=soup.findAll("p",{"class": "sinonimos"})
	Sinonimos=[]

	for s in classeS:
		x=s.text[1:]
		x=x.rstrip('?:!.,;')
		x=x.split(',')
		Sinonimos.append(x)

	
	classePS=soup.findAll("p",{"class": "possiveis-sinonimos"})
	PSinonimos=[]
	for s in classePS:
		x=s.text
		x=x.rstrip('?:!.,;')
		x=x.split(',')
		PSinonimos.append(x)

	R=Sinonimos+PSinonimos

	
	RESULTADO=[item for sublist in R for item in sublist]


	return RESULTADO



palavra=u'mandinga'


P=lista_sinonimos(palavra)

Sinapses=[] #rede de palavras proximas

for m in P:
	try:
		Sinapses.append(lista_sinonimos(m))
	except:
		pass


SINAPSES=[item for sublist in Sinapses for item in sublist]

SINAPSES = set(SINAPSES)
SINAPSES = list(SINAPSES)

txt=''
for sinapse in SINAPSES:
	txt=txt+sinapse+', '



############# grava arquivo
file = codecs.open("Sinapses.txt", "w", "utf-8")
file.write(txt)
file.close()
