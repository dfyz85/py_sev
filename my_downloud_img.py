# -*- coding: utf8 -*-
'''
Created on 20.09.2010

@author: i.saltykov
'''
import urllib2
import re
import urllib
from urlparse import urlparse
from BeautifulSoup  import BeautifulSoup

def downloud(url):
    soup = BeautifulSoup(urllib2.urlopen(url))
    tt = []
    host = urlparse(url)
    for i in soup.findAll('img'):
        try:
            if i['src']:
                img = str(i['src'])
                if 'http' not in img:
                    img_url = 'http:/'+host.hostname+img.replace('..', '')
                else:
                    img_url = img
                tt.append(img_url.replace('//','/'))
        except KeyError:
            print 'sory'
    tt = [i for i in list(set(tt))] 
    #list(set(tt)) убирает все повторяющиеся записи в списки
    return tt
if __name__ == '__main__':
    ff = downloud('http://sevastopol.info')
    for i in ff:
        print i
    tt = [i for i in list(set(tt)) if 'http' in i] 
    #list(set(tt)) убирает все повторяющиеся записи в списки
    
        
        