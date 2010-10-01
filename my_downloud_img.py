# -*- coding: utf8 -*-
'''
Created on 27.09.2010

@author: i.saltykov
'''
import sys
from os import path
import urllib2
#import re
import urllib
#from urlparse import urlparse
from BeautifulSoup  import BeautifulSoup

def parse(integer):
    url = 'http://bmx.transworld.net/category/ugc-images/page/'
    tt = []
    soup = BeautifulSoup(urllib2.urlopen(url+str(integer)+'/'))
    print """
          URL
          """
    print url+str(integer)+'/'      
    for resourge in soup.findAll('img',{'class' : 'no-border'}):
        try:
            print resourge['src'].replace('-225x150','')
            tt.append(resourge['src'].replace('-225x150',''))
        except UnicodeEncodeError:  
            print 'SORY'  
    """ 
        for i in soup.findAll('img',height="150",width="225"):
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
      """
    tt = [i for i in list(set(tt))] 
    #list(set(tt)) убирает все повторяющиеся записи в списки
    return tt
def downloud(urls):
    for url in urls:
        outpath = path.abspath(__file__).replace(sys.argv[0],'')+'\\IN\\'+url.split('/')[-1]
        try:
            urllib.urlretrieve(url, outpath)
            print outpath
        except UnicodeError:
            print """
            SORY"""        

if __name__ == '__main__':
    for i in range(1,127):
        downloud(parse(i))