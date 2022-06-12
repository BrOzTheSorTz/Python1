
#Creamos listas de articulos, sujetos, verbos y adverbios
import random

articulos =["La","Un","El","Aquella"] 
sujetos=["Reina","Principe","Caballo","Mama"]
verbos=["salta","come","rie","baila","traga"]
adverbios =["malamente","rapidamente","mal","regular"]

#Usaremos random.choice() para elegir un articulo,...
#Usaremos random.randint() para elegir una estructura:
#   -Articulo + Sujeto + Verbo + Adverbio
#   -Articulo +sujeto + verbo


#To make the awful poetry program more versatile, add some code to it so that if the user enters a 
# number on the command line (between 1 and 10 inclusive), the program will output that many lines.
#If no command-line argument is given, default to printing five lines as before. 
def get_int(msg,default):
    while True:
        try:    
            i=input(msg)
            if not i:
                return default
            else:
                num= int(i)
                if num >10 or num <0:
                    print("No puede ser")
                else:
                    return num

            
        except ValueError as error1:
            print(error1)



i=0
hasta=get_int("Introduzca el numero de lineas entre 0 o 10 (Enter para 5): ",5 )

while i <hasta:
    estructura=random.randint(1,2)
    if estructura ==1:
        frase =random.choice(articulos)+" "+random.choice(sujetos)+" "+random.choice(verbos)+" "+random.choice(adverbios)
    else:
        frase=random.choice(articulos)+" "+random.choice(sujetos)+" "+random.choice(verbos)+" "  
    
    i +=1
    print(frase)  