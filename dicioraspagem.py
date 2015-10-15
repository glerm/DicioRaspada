#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
['BARE_AMPERSAND_OR_BRACKET', 'XML_ENTITIES_TO_SPECIAL_CHARS', 'XML_SPECIAL_CHARS_TO_ENTITIES', '__add__', '__class__', '__contains__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_findAll', '_findOne', '_formatter_field_name_split', '_formatter_parser', '_invert', '_lastRecursiveChild', '_sub_entity', 'append', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'extract', 'fetchNextSiblings', 'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAllNext', 'findAllPrevious', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'format', 'index', 'insert', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'parent', 'parentGenerator', 'partition', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'replace', 'replaceWith', 'replaceWithChildren', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'setup', 'split', 'splitlines', 'startswith', 'strip', 'substituteEncoding', 'swapcase', 'title', 'toEncoding', 'translate', 'upper', 'zfill']"""

import sys
import urllib2
from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import re


palavra=sys.argv[1]


URL='http://www.dicio.com.br/'+palavra+'/'

req = urllib2.Request(URL)
resposta = urllib2.urlopen(req)
resultadoHTML = resposta.read()



soup = BeautifulSoup(resultadoHTML)

textoprincipal=soup.find("p",{"id": "significado"})


##################################################################
D=[] #lista de definições

print "\n§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\n" 

D.append(textoprincipal.contents[0])
for br in textoprincipal.findAll('br'):
    next = br.nextSibling
    if not (next and isinstance(next,NavigableString)):
        continue
    next2 = next.nextSibling
    if next2 and isinstance(next2,Tag) and next2.name == 'br':
        text = str(next).strip()
        if text:
            D.append(next)
D.append(textoprincipal.contents[-1])


for d in D:
	print "\n"+">>> "+d

print "\n§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\n" 
###########################################################################


S=textoprincipal.find("p",{"class": "adicional cols"})
# sinonimos
S=next.next.next.next




if (S):
	H=[]
	for t in S.contents[1]: 
		H.append(t.text)


	print '\n'+"Sinônimos:"
	for h in H:
		print h
	print '\n'
else:
	print "sem sinônimos no database \n"


for teste in textoprincipal.findAll("a"):
	print str(teste)


##################################
#print soup.prettify()
