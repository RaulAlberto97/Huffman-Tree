import histograma
import Comprimir

texto = "Este es mi texto de prueba para construir un arbol de Huffman a la \
medida"


#texto = "abbcccdddd"
histo = histograma.getHistogram(texto)
#histograma.showHistogram(histo)
frecuency_list = histograma.getListFromHistogram(histo)

frecuency_list.sort(key=lambda tupla: tupla[2])

for tupla in frecuency_list:
    print(tupla)


for i in range(84):
    print("-",end="")


print()
huffman = Comprimir.Huffman()
t = huffman.getHuffmanTree(frecuency_list)
huffman.preOrden(t,"")
"""print(t.left.tupla)
print(t.rigth.tupla)
print(t.rigth.left.tupla)
print(t.rigth.rigth.tupla)
print(t.rigth.rigth.left.tupla)
print(t.rigth.rigth.rigth.tupla)"""

"""frecuency_list.sort(key=lambda tupla: tupla[2],reverse=True)
for tupla in frecuency_list:
    print(tupla)"""
	
"""for c in texto:    
    tupla = filter(lambda tuple: tuple[1]==chr(c),frecuency_list)
    print(tupla as (a,b,c,[]))"""