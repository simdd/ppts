import re


def parseUser(text):
    reCover = r"--cover--(.*)--cover--"
    reTitle = r"title:\s*([^\n\r]*)\n"
    reAuthor = r"author:\s*([^\n\r]*)\n"
    reDate = r"date:\s*([^\n\r]*)\n"

    cover = re.search(reCover, text, re.S).group(1)
    title = re.search(reTitle, cover, re.S).group(1)
    author = re.search(reAuthor, cover, re.S).group(1)
    date = re.search(reDate, cover, re.S).group(1)

    return {title: title, author: author, date: date}
