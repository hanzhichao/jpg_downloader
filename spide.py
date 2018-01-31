# coding:utf8

import urllib
import re
import Queue

base = 'http://localhost:90'
treated_list = []
untreat_list= []


def url_is_in_site(url):
    if True:
        return True
    else:
        return False

def get_form(url):
    html = urllib.urlopen(url).read()
    #print html
    print "*******************************"
    reg = r'<form.*\r.*form>'
    form_list = re.findall(reg, html,re.S)
    with open('form.txt', 'w') as f:
        f.write(form_list[0])
    print 'OK'
    
    #iframe情况

    #js writeForm情况，iframe+js writeForm

def get_url(url):
    html = urllib.urlopen(url).read()
    #print html
    reg_php = r'href=["\'](.*?\.php.*?)["\']>'
    url_list = re.findall(reg_php, html)
    url_list = list(set(url_list))
    return url_list
    
def get_jpg(url):
    html = urllib.urlopen(url).read()
    reg = r'src=[\'\"](.*\.jpg)[\'\"]'
    jpg_list = re.findall(reg, html)
    jpg_list = list(set(jpg_list))
    return jpg_list

uq = Queue.Queue(maxsize=-1)
uq.put(base+'/iwebshop/')

jpg_count = 0
down_jpg = []
while not uq.empty():
    print uq.qsize()
    url = uq.get()
    print url
    print '=================================================================='

    jpg_list = get_jpg(url)
    
    for jpg_url in jpg_list:
        if jpg_url[:4] != 'http':
            jpg_url = base + jpg_url
            if jpg_url not in down_jpg:
                print jpg_url
                jpg_count += 1
                try:
                    urllib.urlretrieve(jpg_url,'jpg/%s.jpg' % jpg_count)
                    down_jpg.append(jpg_url)
            #except IOError:
            #    print "url wrong!!!"
                except Exception:
                    print "url wrong!!!"
        else:
            print '[wrong jpg url]: %s' % jpg_url

    treated_list.append(url)
    try:
        url_list = get_url(url)
    except Exception:
        print "Error"

    for url in url_list:
        if url[:10] != 'javascript':
            url = base+url
            if url not in treated_list or untreat_list:
                uq.put(url)
                untreat_list.append(url)
    else:
        print '[wrong url: %s]' % url
    #print untreat_list
    print "--------------------------------"
    #print treated_list
    
  


