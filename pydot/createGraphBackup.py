from numpy import genfromtxt
import csv
import pydot
#from cStringIO import StringIO
#from tokenize import generate_tokens
import sys

#arguments: path threshold scale
path = sys.argv[1]
threshold = float(sys.argv[2])
scale = float(sys.argv[3])

plainCsv = csv.reader(open(path+'output.csv', 'U'), delimiter=',', quotechar='"')
names = plainCsv.next()
numNodes = len(names)
imported = genfromtxt(path+'output.csv', delimiter=',')[1:,:]
spearman = genfromtxt(path+'spearmanCODoutput.csv', delimiter=',')[1:,:]

preNonLin = imported-spearman
preNonLin[preNonLin<0]=0
nonLin = preNonLin/(imported+0.0001)

colorlookup = ["blue1","blue2","blue3","blue4","purple","red4","red3","red2","red1"]

#threshold = float(raw_input("Please enter threshold value"))

graph = pydot.Dot('graphname', graph_type='graph')
for name in names:
        graph.add_node(pydot.Node(name))

for (i,nameI) in enumerate(names):
	for (j,nameJ) in enumerate(names):
		if (i>j)&(imported[i][j] >= threshold):
			graph.add_edge(pydot.Edge(nameI, nameJ,len=scale/(imported[i][j]+0.05),weight=(imported[i][j]*imported[i][j]),penwidth=imported[i][j]*2,color=colorlookup[int(round(nonLin[i][j]/(1.0/(len(colorlookup)-1))))]))
			#print(nameI + " " + nameJ)
			
graph.write(path + 'Agraph.png', prog='neato', format='png')
graph.write(path + 'Agraph.dot', prog='neato', format='raw')