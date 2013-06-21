#Creating a .json file for radial graph display for One Vs All (OVR)
#Written by Riaz Moola, 2012
from numpy import genfromtxt
import csv
import pydot
import sys

#arguments: path threshold scale
path = sys.argv[1]
threshold =  0
scale = 1


plainCsv = csv.reader(open(path+'outputOVR.csv', 'U'), delimiter=',', quotechar='"')

allrows = list(reader)
names = plainCsv.next()
numNodes = len(allrows)-1
imported = genfromtxt(path+'outputOVR.csv', delimiter=',')[1:,:]
#spearman = genfromtxt(path+'spearmanCODoutput.csv', delimiter=',')[1:,:]

#preNonLin = imported-spearman
#preNonLin[preNonLin<0]=0
#nonLin = preNonLin/(imported+0.0001)

#print nonLin

colorlookup = ["blue1","blue2","blue3","blue4","purple","red4","red3","red2","red1"]

#threshold = float(raw_input("Please enter threshold value"))

#adj display
file = open(path + "radial.json", "w")
file.write('{"nodes":[')

#graph = pydot.Dot('graphname', graph_type='graph')
for (i, nameI) in range(0, numNodes):
        #graph.add_node(pydot.Node(names[i]))
        if i == numNodes-1:
                file.write('{"name":"' + allrows[i][0] + '","group":0}')
        else:
                file.write('{"name":"' + allrows[i][0] + '","group":0},')
                
                
       

file.write('], "links":[')

for (i,nameI) in enumerate(names):
        for (j,nameJ) in enumerate(names):
                if (i>j)&(imported[i][j] >= threshold):
      #                  graph.add_edge(pydot.Edge(nameI, nameJ,len=scale/(imported[i][j]+0.05),weight=(imported[i][j]*imported[i][j]),penwidth=imported[i][j]*2,color=colorlookup[int(round(nonLin[i][j]/(1.0/(len(colorlookup)-1))))]))
                        #file.write('{"source":'+str(i)+',"target":'+str(j)+',"value":'+str(imported[i][j])+',"nonlin":'+str(nonLin[i][j])+'},')
						file.write('{"source":'+str(i)+',"target":'+str(j)+',"value":'+str(0)+',"nonlin":0},')
                elif (i==j) and i==(len(names)-1):
                        file.write('{"source":'+str(i)+',"target":'+str(j)+',"value":'+str(0)+',"nonlin":0}')
                else:
                        file.write('{"source":'+str(i)+',"target":'+str(j)+',"value":'+str(0)+',"nonlin":0},')
                        
                                
                        
                      
file.write("]}")
file.close()
			
#graph.write(path + 'Agraph.png', prog='neato', format='png')
#graph.write(path + 'Agraph.dot', prog='neato', format='raw')
