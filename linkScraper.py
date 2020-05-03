import sys
import urllib.request as urllib
from bs4 import BeautifulSoup
import json


def main():
    baseHref = "https://en.wikipedia.org"
    firstArticleName = sys.argv[1]
    maxLinks = sys.argv[2]
    links = {}

    ongoingHrefs = [firstArticleName]
    levelHref = {firstArticleName: 1}

    for h in ongoingHrefs:
        if not (h in links.keys()) and levelHref[h] <= maxLinks:
            try:
                articlePage = urllib.urlopen(h)
                articleSoup = BeautifulSoup(articlePage.read(), 'html.parser')
                articleLinks = []
                for p in articleSoup.findAll("p"):
                    for a in p.findAll("a", title=True):
                        articleLinks.append(baseHref + a['href'])
                        ongoingHrefs.append(baseHref + a['href'])
                        levelHref[baseHref + a['href']] = levelHref[h] + 1
                        print(levelHref[baseHref + a['href']])
                links[h] = articleLinks
            except:
                print("invalid href")

    with open("links.json", 'w') as outfile:
        json.dump(links, outfile)


main()
