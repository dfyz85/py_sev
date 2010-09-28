# -*- coding: utf8 -*-
'''
Created on 20.09.2010

@author: i.saltykov
'''
import urllib2
import re
import urllib
from BeautifulSoup  import BeautifulSoup

def downloud(url):
    soup = BeautifulSoup(urllib2.urlopen(url))
    tt = []
    for i in soup.findAll('img'):
        try:
            if i['src']:
                tt.append(i['src'])
        except KeyError:
            print 'sory'
    tt = [i for i in list(set(tt)) if 'http' in i] 
    #list(set(tt)) убирает все повторяющиеся записи в списки
    
        
        