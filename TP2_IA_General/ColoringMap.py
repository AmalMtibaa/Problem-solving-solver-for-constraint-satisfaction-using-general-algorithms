from csp import *
from cspUtil import *
import networkx as nx
import matplotlib.pyplot as plt #pour la visualisation


t=csp()
file = open("CSP\ColoringMap\Variables", "r")
ch = file.read().rstrip('\n')
t.ajoutVariable(ch)
file.close()
file = open("CSP\ColoringMap\Domaines", "r")
for i in range(0, len(t.variables)):
    ch = file.readline().rstrip('\n')
    t.ajoutDomaine(t.variables[i], ch.split(" "))
file.close()
file = open("CSP\ColoringMap\Contraintes", "r")
for i in range(0, len(t.variables)):
    ch = file.readline().rstrip('\n')
    while ch != "##":
        t.ajoutContrainte(t.variables[i], ch)
        ch = file.readline().rstrip('\n')
file.close()
e = []
for i in t.contraintes:
    for j in i:
        tmp = j.split(" ")
        e.append((tmp[0], tmp[2]))

G=nx.Graph()
G.add_edges_from(e)
for i in range(0,len(t.contraintes)):
    if len(t.contraintes[i])==0:
        G.add_node(t.variables[i])
color_intial=['white']*len(t.variables)
nx.draw_circular(G,node_color = color_intial,with_labels=True)
plt.savefig('intialMap.png',bbox_inches='tight') #Here we have the graph of nodes


def intializeContext():
    t = csp()
    file = open("CSP\ColoringMap\Variables", "r")
    ch = file.read().rstrip('\n')
    t.ajoutVariable(ch)
    file.close()
    file = open("CSP\ColoringMap\Domaines", "r")
    for i in range(0, len(t.variables)):
        ch = file.readline().rstrip('\n')
        t.ajoutDomaine(t.variables[i], ch.split(" "))
    file.close()
    file = open("CSP\ColoringMap\Contraintes", "r")
    for i in range(0, len(t.variables)):
        ch = file.readline().rstrip('\n')
        while ch != "##":
            t.ajoutContrainte(t.variables[i], ch)
            ch = file.readline().rstrip('\n')
    file.close()

    return t


def drawGraph(a,t,method):
    nx.draw_circular(G, node_color=a, with_labels=True)
    if method=='backtracking':
        plt.savefig('backtrackingColorMap.png', bbox_inches='tight')
    if method=='forward':
        plt.savefig('forward.png',bbox_inches='tight')
    if method=='forwardAC3':
        plt.savefig('forwardAC3.png',bbox_inches='tight')
