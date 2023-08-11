"""
rango de la contaseña:
0000 ---> mínimo
9999 ---> máximo
"""

#funcion para hackear tu contraseña
def hackear_contra():
    while True:
        try:
            contrasenia = int(input("Ingresa tu contraseña super segura:"))
            # este for recorre hasta encontrar tu contraseña
            for clave in range(0000,10000):
                print(clave)
                if clave == contrasenia:
                    print("Hackeado")
                    break
        except:
            print('solo numeros.')
hackear_contra()