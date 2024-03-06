import os
"""2. Elabore un programa en Python que permita leer la información de un usuario
Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos)"""

#validacion de num enteros
def val_num():
    try:
        op=int(input('-'))
        return op
    except ValueError:
        print('opcion no valida')
        return val_num()
#validacion numero flotantes
def valfloat():
    try:
        op=float(input('-'))
        return op
    except ValueError:
        print('opcion no valida')
        return valfloat()
# pedir datos    
def almacenar_datos():
    
    os.system('cls')
    print('por favor, digite el numero de dentificacion')
    id=val_num()
    print('por favor, digita el nombre')
    nombres=input('-')
    print('por favor, digita el apellido')
    apellidos=input('-')
    print('por favor, digite tu ubicacion')
    ubicacion=input('-')
    print('por favor, digita la direccion de residencia')
    dir=input('-')
    print('por favor, digita la ciudad de residencia')
    ciu=input('-')
    print('por favor, digite el numero de longitud')
    long=valfloat()
    print('por favor, digite el numero de longitud')
    lat=valfloat()
    print('por favor, digite tu Email')
    email=input('-')
    print('por favor, digita tu edad')
    edad=val_num()
    print('por favor, digita tu ocupacion')
    ocupacion=input('-')
 #guardar datos en diccionario   
    persona={
        'id':id,
        'nombres':nombres,
        'apellidos':apellidos,
        'ubicación':ubicacion,
        'dirección':{
            'direccion':dir,
            'ciudad':ciu,
            'latitud':lat,
            'longitud':long   
        },
        'email':email,
        'edad':edad,
        'ocupacion':ocupacion 
    }

    print('¡la persona ha sido guardada con exito!')
    os.system('pause')
    os.system('cls')
    print(persona)
    return almacenar_datos()

    
    
    

    
    