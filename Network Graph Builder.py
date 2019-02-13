# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt
import csv

graphDict = list()

with open("test.csv") as file:
    reader = csv.reader(file)
    for row in reader:
       pair = (row[0], row[1])
       graphDict.append(pair)

file.close()
    

graph = nx.DiGraph()

for i in graphDict:  
    graph.add_edge(i[1],i[0]n) # default edge data=1

nx.draw(graph,with_labels=True)
plt.draw()
plt.show()