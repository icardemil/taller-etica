#Primera solución
lista_calcetines = [1,2,1,2,1,3,2]
cantidad = 0
for i in range(1,max(lista_calcetines)+1):
    cantidad += lista_calcetines.count(i)//2
print(cantidad)

#Segunda solución
lista_calcetines = [1,2,1,2,1,3,2]
cantidad = 0
def filtrar_lista(calcetin,lista):
    lista_aux = []
    for elem in lista:
        if elem != calcetin:
            lista_aux.append(elem)
    return(lista_aux)

for calcetin in lista_calcetines:
    cantidad += lista_calcetines.count(calcetin)//2
    lista_calcetines = filtrar_lista(calcetin,lista_calcetines)
print(cantidad)

#Tercera solución
lista_calcetines = [1,2,1,2,1,3,2]
cantidad = 0
for calcetin in lista_calcetines:
    cantidad += lista_calcetines.count(calcetin)//2
    lista_calcetines = list(filter(lambda x: x != calcetin, lista_calcetines))
print(cantidad)
