import re
import os
import readline

with open('demo.ppts', 'r') as file:
    text = file.read()

reCover = r"--cover--(.*)--cover--"
rePages = r"--page--(.*)--page--"
reTitle = r"title:\s*([^\n\r]*)\n"
reAuthor = r"author:\s*([^\n\r]*)\n"
reDate = r"date:\s*([^\n\r]*)\n"

cover = re.search(reCover, text, re.S).group(1)
title = re.search(reTitle, cover, re.S).group(1)
author = re.search(reAuthor, cover, re.S).group(1)
date = re.search(reDate, cover, re.S).group(1)

print(title)
print(author)
print(date)
