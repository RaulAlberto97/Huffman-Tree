def getHistogram(datos):
    histogram = []
    for i in range(256):
        histogram.append(0);
    for dato in datos:
        #print(dato,ord(dato),end=" ")
        histogram[ord(dato)] += 1
    return histogram

def showHistogram(histogram):
    i=0
    for f in histogram:
        if f > 0:
            print(chr(i),f)
        i+=1
		
def getListFromHistogram(histogram):
    #(ascii,carcater,frecuencia)
    frecuency_list = []
    i = 0
    for f in histogram:
        if f > 0:
            frecuency_list.append((i,chr(i),f,[]))
        i += 1
    return frecuency_list
	
	
	
	
	
	
	
	