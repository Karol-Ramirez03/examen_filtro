import json
import os
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
def cargarproductos():
    try:
        with open('productos.json','r') as archivo:
            productos=json.load(archivo)
    except FileNotFoundError:
        productos=[]
        return productos
    

def guardar_productos(productos):
    with open('productos.json','w') as archivo:
        json.dump(productos,archivo,indent=4)
        
def add_productos(productos):#identificacion
    os.system('cls')
    #pedir datos
    print('ingrese los datos del producto')
    print('ingrese el numero de identificacion')
    id=val_num()
    print('ingrese el nombre del producto')
    nombre=input('-')
    print('ingrese el valor unitario')
    stockmin=val_num()
    print('ingrese el stock maximo')
    stockmax=val_num()
    print('ingrese el stock minimo')
    valorunitario=valfloat()
    producto={
        'id':id,
        'nombre':nombre,
        'stock minimo': stockmin,
        'stock maximo': stockmax,
        'valor unitario': valorunitario
    }

    
    #guardar datos:
    #cargar las productos
    productos=cargarproductos()###
    #agregar el nueva producto
    productos.append(producto)
    
    #guardar la lista actualizada
    guardar_productos(productos)
  
    
    
    