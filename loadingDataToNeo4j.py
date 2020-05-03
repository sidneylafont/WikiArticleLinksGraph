from py2neo import Graph, Node, Relationship
import json

graph = Graph(password="####") #insert own neo4j password

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



