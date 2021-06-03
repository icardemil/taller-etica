# Definicón de variables a utilizar
rut = 30686957
factor = 2
total = 0

#Cálculo de la parte entera del RUT
while rut != 0:
    total = total + ((rut%10)*factor)
    factor = factor + 1
    if factor > 7:
        factor = 2
    rut = rut//10

#Obtención del dígito verificador
verificador = 11 - (total%11)
if verificador == 11:
    verificador = 0
elif verificador == 10:
    verificador = 'k'

#Mostrar dígito verificador
print(verificador)