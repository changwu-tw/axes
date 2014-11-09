# -*- coding: utf-8 -*-

import json
import sys
import urllib

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    url = 'http://axe-level-1.herokuapp.com/lv2/'
    content = urllib.urlopen(url).read()

    pages = int(BeautifulSoup(content).findAll('a')[-1].text)

    info = []
    for page in range(pages):
        url = 'http://axe-level-1.herokuapp.com/lv2/?page=%d' % (page+1)
        content = urllib.urlopen(url).read()

        tr_doms = BeautifulSoup(content).findAll('tr')[1:]
        for tr_dom in tr_doms:
            td_dom = tr_dom.findAll('td')
            info.append({
                'town': td_dom[0].text,
                'village': td_dom[1].text,
                'name': td_dom[2].text
                }
            )
    f = open('phase2.txt', 'w')
    f.write(json.dumps(info, ensure_ascii=False))
    f.close()
