import re

text = '''
--cover--
title: 这里是名字
author: simdd
date: 2019/02/10
--cover--

--page--
page1
--page--

--page--
page2
--page--
'''

info = re.search("--cover--([\\w\\W]*)--cover--", text)
pages = re.findall("--page--([\\w\\W]*)--page--", text)

print(info)

for x in pages:
    print(x)
