import Trees

class Huffman:
    def __init__(self):
        pass

    def getHuffmanTree(self,f):
        """for tupla in f:
            print(tupla)
        input()"""
        if len(f)==2:
            """Crear y regresar arbol"""
            left = Trees.Tree(None,None,f[0])
            rigth = Trees.Tree(None,None,f[1])
            return Trees.Tree(left,rigth)
        etiqueta = str(f[0][2]) + "+" + str(f[1][2])
        fcopy = f.copy()
        del fcopy[0]
        del fcopy[0]
        fcopy.append((None,None,f[0][2]+f[1][2],[etiqueta]))
        fcopy.sort(key=lambda tupla: tupla[2])        
        
        t = self.getHuffmanTree(fcopy)
        left = Trees.Tree(None,None,f[0])
        rigth = Trees.Tree(None,None,f[1])
        self.insertarArbol(t,left,rigth,etiqueta)
        return t
    
    def insertarArbol(self,t,left,rigth,etiqueta):	
        if t.left != None:#si no tiene hijo izquierdo tampoco tiene derecho
            """print(t.left.tupla)	    
            print(t.rigth.tupla)	    
            input()"""
            if t.left.tupla[3] != []:
                if t.left.tupla[3][0] == etiqueta:
                    t.left.left = left
                    t.left.rigth = rigth
                    del t.left.tupla[3][0]
                    #print("Insertado en izq")					
                    return True                
            if self.insertarArbol(t.left,left,rigth,etiqueta):
                return True	
            if t.rigth.tupla[3] != []:
                if t.rigth.tupla[3][0] == etiqueta:
                    t.rigth.left = left
                    t.rigth.rigth = rigth
                    del t.rigth.tupla[3][0]                
                    #print("Insertado en der")					
                    return True
            if self.insertarArbol(t.rigth,left,rigth,etiqueta):
                return True
        return False

    def preOrden(self,t,codigo):
        if t.left!=None:
            self.preOrden(t.left,codigo+"1")
            self.preOrden(t.rigth,codigo+"0")
        else:
            print(t.tupla,codigo)			
