# coding: cp437
import treelib
from treelib import Node, Tree

niveles=input("Digite el número de niveles del árbol: ")
nHijosT=input("Digite el número de hijos por cada nodo: ")
valores=[]

for x in range(0,pow(nHijosT,niveles-1)):
    #valores.append(input("digite el valor "+str(x+1)+": "))
    valores.append(x+1)

def LlenarArbol(hijo,niv,nivT,nhijo,nhijT,tag):
    print niv
    if(len(valores)>0):
    	print("hey!")
        if(nhijo<>nhijT):
                if(niv<(nivT-1)):
                    tree.create_node({"alpha":-20,"beta":20},tag,hijo.identifier)
                    tag+=1
                    #tree.show()
                    #raw_input("test")
                    LlenarArbol(tree.get_node(tag-1),niv+1,nivT,nhijo,nhijT,tag)
                else:
                    for i in range(0,nhijT):
                        tree.create_node(valores[0],tag,parent=hijo.identifier)
                        tag+=1
                        valores.remove(valores[0])
                    #tree.show()
                    #raw_input(str(len(valores))+"test")
                    LlenarArbol(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,tag+1)
        else:
        	LlenarArbol(tree.get_node(hijo._bpointer),niv-1,nivT,0,nhijT,tag+1)

tree=Tree()
tree.create_node({"alpha":-20,"beta":20},0)
LlenarArbol(tree.get_node(0),1,niveles,0,nHijosT,1)
tree.show(0,0)