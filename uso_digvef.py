def verificar_rut(rut,ver):
    # Definición de variables a utilizar
    rut, factor, total = rut, 2, 0
    
    # Cálculo de la parte entera del RUT
    while rut != 0:
        total = total + ((rut%10)*factor)
        factor = factor + 1
        if factor > 7: factor = 2
        rut = rut//10

    # Obtención del dígito verificador   
    verificador = 11 - (total%11)
    if verificador == 11:
        verificador = 0
    elif verificador == 10:
        verificador = 'k'
    
    """
        Verifica si el rut ingresado por el usuario es válido
        Es necesario realizar el cast de la variable "verificador", porque el input realizado por el
        usuario es del tipo "String". Además, es necesario considerar el caso en que el dígito 
        verificador sea igual a "k"
    """
    if str(verificador) == ver:
        return True
    else:
        return False

print("Ingresar parte entera del rut")
rut_entero = int(input())
print("Ingresar dígito verificador")
dig_ver = input()

if verificar_rut(rut_entero,dig_ver):
    print("El rut es válido")
else:
    print("El rut no es válido")