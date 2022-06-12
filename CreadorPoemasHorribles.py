
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

i=0
while i <5:
    estructura=random.randint(1,2)
    if estructura ==1:
        frase =random.choice(articulos)+" "+random.choice(sujetos)+" "+random.choice(verbos)+" "+random.choice(adverbios)
    else:
        frase=random.choice(articulos)+" "+random.choice(sujetos)+" "+random.choice(verbos)+" "  
    
    i +=1
    print(frase)  