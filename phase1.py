# -*- coding: utf-8 -*-

import json
import sys
import urllib

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    url = 'http://axe-level-1.herokuapp.com/'
    content = urllib.urlopen(url).read()

    info = []
    tr_doms = BeautifulSoup(content).findAll('tr')[1:]
    for tr_dom in tr_doms:
        td_dom = tr_dom.findAll('td')
        info.append({
            'name': td_dom[0].text,
            'grades': {
                '國語': int(td_dom[1].text),
                '數學': int(td_dom[2].text),
                '自然': int(td_dom[3].text),
                '社會': int(td_dom[4].text),
                '健康教育': int(td_dom[5].text)
            }
        })

    f = open('phase1.txt', 'w')
    f.write(json.dumps(info, ensure_ascii=False))
    f.close()
