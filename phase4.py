# -*- coding: utf-8 -*-

import cookielib
import json
import sys
import urllib2

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    url = 'http://axe-level-4.herokuapp.com/lv4'
    content = opener.open(url).read()
    pages = int(BeautifulSoup(content).findAll('a')[-1].text)

    info = []
    for page in range(pages):
        url = 'http://axe-level-4.herokuapp.com/lv4/?page=%d' % (page+1)
        if page != 0:
            ref = 'http://axe-level-4.herokuapp.com/lv4/?page=%d' % page
        else:
            ref = 'http://axe-level-4.herokuapp.com/lv4'
        opener.addheaders = [
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'),
            ('Referer', ref),
        ]
        content = opener.open(url).read()
        tr_doms = BeautifulSoup(content).findAll('tr')[1:]
        for tr_dom in tr_doms:
            td_dom = tr_dom.findAll('td')
            info.append({
                'town': td_dom[0].text,
                'village': td_dom[1].text,
                'name': td_dom[2].text
                }
            )

    f = open('phase4.txt', 'w')
    f.write(json.dumps(info, ensure_ascii=False))
    f.close()
