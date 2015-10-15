#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import re


def tsplit(string, delimiters):
    #Behaves str.split but supports multiple delimiters.
    
    delimiters = tuple(delimiters)
    stack = [string,]

    
    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)
    
       
    return stack


definicoes=tsplit(textoprincipal.text, ('adj.', 'Adj.', 's.m', 'S.m','P.ext.', 'Etm. do latim:'))




