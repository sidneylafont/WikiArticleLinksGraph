import sys
import urllib.request as urllib
from bs4 import BeautifulSoup
import json
from py2neo import Graph, Node, Relationship
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

    graph = Graph(password="#####") #insert own neo4j password

    tx = graph.begin()

    with open('links.json') as json_file:
        data = json.load(json_file)

        nodes = {}
        for l in data:
            node = Node("Page", link=l)
            graph.create(node)
            nodes[l] = node

        for n in data:
            for l in data[n]:
                try:
                    r = Relationship(nodes[n], "LinksTo", nodes[l])
                    graph.create(r)
                except:
                    print("couldn't create relationship")


main()
