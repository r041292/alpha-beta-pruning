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
    #print niv
    if(len(valores)>0):
        if(nhijo<>nhijT):
                if(niv<(nivT-1)):
                    tree.create_node({"alpha":-999,"beta":999,"visit":False,"hijosV":0},tag,hijo.identifier)
                    tag+=1
                    #tree.show()
                    #raw_input("test")
                    LlenarArbol(tree.get_node(tag-1),niv+1,nivT,nhijo,nhijT,tag)
                else:
                    for i in range(0,nhijT):
                        tree.create_node({"valor":valores[0],"visit":False},tag,parent=hijo.identifier)
                        tag+=1
                        valores.remove(valores[0])
                    #tree.show()
                    #raw_input(str(len(valores))+"test")
                    LlenarArbol(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,tag)
        else:
        	LlenarArbol(tree.get_node(hijo._bpointer),niv-1,nivT,0,nhijT,tag)

def prunning(hijo,niv,nivT,nhijo,nhijT,tag):
    #print niv
    if(tree.get_node(0).tag["hijosV"]<nhijT):
        print("Nodo en el que estoy",hijo.identifier)
        print("nodo que voy a revisar",tag)
        if(hijo.tag["hijosV"]<nhijT and niv<nivT-1):
            tree.get_node(hijo._fpointer[hijo.tag["hijosV"]]).tag["alpha"]=hijo.tag["alpha"]
            tree.get_node(hijo._fpointer[hijo.tag["hijosV"]]).tag["beta"]=hijo.tag["beta"]
            #EL PROBLEMA
            tag=hijo._fpointer[hijo.tag["hijosV"]]
            #tree.show()
            #raw_input("test")
            print("Este es el tag",tag," y este es el nodo ",tree.get_node(tag).identifier)
            print("el nodo que voy a ser es ",tree.get_node(tag).identifier)
            print("el hijo que voy a visitar es",tree.get_node(tag+1).identifier)
            prunning(tree.get_node(tag),niv+1,nivT,nhijo,nhijT,tag+1)
        else:
            a=raw_input("asd")
            tree.show()
            print("else")
            if(tree.get_node(tag).is_leaf()):
            	print(tree.get_node(tag).is_leaf())
                if(hijo.tag["alpha"]<hijo.tag["beta"]):
                    if(tree.level(hijo.identifier)%2==0):
                        if(hijo.tag["alpha"]<tree.get_node(tag).tag["valor"]):
                            print "alpha"
                            print tree.get_node(tag).tag["valor"]
                            hijo.tag["alpha"]=tree.get_node(tag).tag["valor"]
                    else:
                        if(hijo.tag["beta"]>tree.get_node(tag).tag["valor"]):
                            hijo.tag["beta"]=tree.get_node(tag).tag["valor"]
                    hijo.tag["visit"]=True
                    tree.get_node(tag).tag["visit"]=True
                    hijo.tag["hijosV"]+=1
                    tag+=1
                    #tree.show()
                    #raw_input(str(len(valores))+"test")
                    if(hijo.tag["hijosV"]<nhijT):
                        print("Regreso a: ",hijo.identifier)
                        prunning(hijo,niv,nivT,nhijo+1,nhijT,hijo._fpointer[hijo.tag["hijosV"]])
                    else:
                        print("Regreso se me acabaron los hijos: ",hijo._bpointer)
                        tree.get_node(hijo._bpointer).tag["hijosV"]+=1
                        print("Algo raro", hijo.tag["hijosV"])
                        if(hijo.identifier<>0):
                            pad=tree.get_node(hijo._bpointer)
                            if(pad.tag["alpha"]<pad.tag["beta"]):
                                if(tree.level(pad.identifier)%2==0):
                                    if(pad.tag["alpha"]<hijo.tag["beta"]):
                                        pad.tag["alpha"]=hijo.tag["beta"]
                                else:
                                    if(hijo.tag["beta"]>hijo.tag["alpha"]):
                                        print tree.get_node(tag).tag["alpha"]
                                        pad.tag["beta"]=hijo.tag["alpha"]
                                hijo.tag["visit"]=True
                            

                        print("AAAAAAAH",hijo._fpointer[hijo.tag["hijosV"]-2])
                        prunning(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,hijo.identifier+1)
                else:
                    #hijo.tag["hijosV"]=nhijT
                    print("ya casi", tag)
                    prunning(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,tag+1)
            else:
                if(hijo.tag["alpha"]<hijo.tag["beta"]):
                    if(tree.level(hijo.identifier)%2==0):
                        if(hijo.tag["alpha"]<tree.get_node(tag).tag["beta"]):
                            hijo.tag["alpha"]=tree.get_node(tag).tag["beta"]
                    else:
                        if(hijo.tag["beta"]>tree.get_node(tag).tag["alpha"]):
                            print tree.get_node(tag).tag["alpha"]
                            hijo.tag["beta"]=tree.get_node(tag).tag["alpha"]
                    tree.get_node(tag).tag["visit"]=True
                    #hijo.tag["hijosV"]+=1
                    tag+=1
                    #tree.show()
                    
                    if(hijo.tag["hijosV"]<nhijT):
                        prunning(hijo,niv,nivT,nhijo+1,nhijT,hijo._fpointer[hijo.tag["hijosV"]])
                    else:
                        prunning(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,hijo._fpointer[hijo.tag["hijosV"]])
                else:
                    tree.get_node(tag).tag["hijosV"]=nhijT
                    prunning(tree.get_node(hijo._bpointer),niv-1,nivT,nhijo+1,nhijT,hijo._fpointer[hijo.tag["hijosV"]])


                #prunning(tree.get_node(hijo._bpointer),niv-1,nivT,0,nhijT,tag+1)

tree=Tree()
tree.create_node({"alpha":-999,"beta":999,"visit":False,"hijosV":0},0)
LlenarArbol(tree.get_node(0),1,niveles,0,nHijosT,1)
tree.show(0,0)
print(tree.get_node(4).is_leaf())
prunning(tree.get_node(0),1,niveles,0,nHijosT,1)
tree.show()

