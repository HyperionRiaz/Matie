from numpy import genfromtxt
import csv
import pydot
from cStringIO import StringIO
from tokenize import generate_tokens

plainCsv = csv.reader(open('testoutputclean.csv', 'U'), delimiter=',', quotechar='"')
names = plainCsv.next()
numNodes = len(names)
imported = genfromtxt('testoutputclean.csv', delimiter=',')[1:,:]
#print imported

threshold = float(raw_input("Please enter threshold value"))

graph = pydot.Dot('graphname', graph_type='graph')
for name in names:
        graph.add_node(pydot.Node(name))

for (i,nameI) in enumerate(names):
	for (j,nameJ) in enumerate(names):
		if (i>j)&(imported[i][j] >= threshold):
			graph.add_edge(pydot.Edge(nameI, nameJ))
			#print(nameI + " " + nameJ)
			
graph.write('wtf.png', prog='sfdp', format='png')