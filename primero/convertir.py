import os
""" Elabore un programa en Python que permita convertir de pesos a dólares, de
pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
1 yen = 26.30 pesos
1 dólar = 3944 pesos
1 euro = 4279 pesos"""



def valfloat():
    try:
        op=float(input('-'))
        return op
    except ValueError:
        print('opcion no valida')
        return valfloat()
        
def tranf_yen():
    print('ingrese el valor a tranformar ')
    val=valfloat()
    calculo=val/26.30
    print(f'{calculo} pesos')
def tranf_dolares():
    print('ingrese el valor a tranformar de dolares a pesos')
    val=valfloat()
    calculo=val/3944
    print(f'{calculo} pesos')
def tranf_euros():
    print('ingrese el valor a tranformar de euros a pesos')
    val=valfloat()
    calculo=val/4279
    print(f'{calculo} pesos')

def menu():
    os.system('cls')
    titulo="""
    ____________________
    CALCULADORA de PESOS
    ____________________
    """
    print(titulo)
    
    list_opciones=[1,2,3]
    try:
        op=int(input('1. tranformar de pesos a yen\n2. tranformar pesos a dolares\n3. tranformar de pesos a euros\n-'))
        if not(op in list_opciones):
            print('la opcion no esta')
            return menu()
    except ValueError:
        print('dato no valido')
        return menu()
    else:
        if op==1:
            os.system('cls')
            tranf_yen()
            os.system('pause')
            return menu()
        elif op==2:
            os.system('cls')
            tranf_dolares()
            os.system('pause')
            return menu()
        elif op==3:
            os.system('cls')
            tranf_euros()
            os.system('pause')
            return menu()
    
    