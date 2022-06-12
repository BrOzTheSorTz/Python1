from importlib.metadata import FileHash
import random

#Creamos un programa que que cree una cuadrilla
#con enteros de manera random

def get_int(msg,minimo,default):
    while True:
        try:
            line=input(msg)
            #Al poner default is not None
            #Estamos diciendo que el usuario no puede presionar
            #directamente el enter sino que necesita poner un número

            if not line and default is not None:
                return default
            i=int(line)
            if i< minimo:
                print("must be >=", minimo)
            else:
                return i
        except ValueError as error:
            print (error)


filas = get_int("filas: ",1,None)
columnas = get_int("columnas: ",1,None)
minimo =get_int("minimo(o Enter para 0): ",-1000000,0)

default =1000
maximo = get_int("maximo (Enter para 1000):",minimo,default)#Por defecto es 1000 y como minimo obviamente lo minimo

#Una vez que sabemos cuantas filas y columnas
#el usuario requiere y el valor maximo y minimo de valores

fila =0
while fila < filas:
    linea=""
    columna =0
    while columna<columnas:
        i=random.randint(minimo,maximo)
        s=str(i)
        while len(s)<10:
            s=" "+s#Nos permite separar cada digito 10 caracteres
        linea +=s #Usamos esta variable para acumular los numeros de cada fila
        columna +=1
    print(linea)
    fila +=1

