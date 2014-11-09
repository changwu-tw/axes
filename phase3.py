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

    info = []
    for page in range(1, 77):
        if page == 1:
            url = 'http://axe-level-1.herokuapp.com/lv3/'
        else:
            url = 'http://axe-level-1.herokuapp.com/lv3/?page=next'
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

    f = open('phase3.txt', 'w')
    f.write(json.dumps(info, ensure_ascii=False))
    f.close()
