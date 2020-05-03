# WikiArticleLinksGraph

A python script that creates the graph of Wikipedia articles that link to each other leveraging the graph database 
neo4j. Provided a starting Wikipedia link and the number of levels to travel from the starting Wikipedia link, it
creates a graph in Neo4j containing a node for every Wikipedia link within the certain number of levels of the starting 
Wikipedia link and a relationship for every Wikipedia page that links to another Wikipedia page within the graph.

to create the Neo4j graph:

        $ cd WikiArticleLinksGraph
        $ python linksToNeo4j.py link-of-starting-Wikipedia-page number-of-levels-to-travel 

# Example

For example to create a graph starting at https://en.wikipedia.org/wiki/Rainbow and traveling 3 layers

        $ cd Blur
        $ python linksToNeo4j.py https://en.wikipedia.org/wiki/Rainbow 3
        
Notes:
- you have to insert your own Neo4j password into linksToNeo4j.py on line 34    

# Packages

- py2neo
- bs4
- urllib.request
- json
- sys

# Database Technologies

- Neo4j

