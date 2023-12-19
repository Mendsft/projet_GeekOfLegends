import random
import time
import fonction as fct
import class_c as cls 

# Instanciation 

# Boss
sauron = cls.boss("Sauron","",350,10)
chronos = cls.boss("Chronos","",400,10)
lilith = cls.boss("Lilith","",250,10)

# Héros 
guerrier = cls.guerrier("Guerrier","Défense",100,8,0)
mage = cls.mage("Mage",None,80,9,10)
archer = cls.archer("Archer",None,60,6,10)

# Lieu 
cimetiere =cls.Lieu("Cimetière ",[])
# Création des variables : 

list_boss = [sauron,chronos,lilith]
list_heros = [guerrier,mage,archer]
# Stocker les enigmes dans un dico afin de faire correspondre plus tard la keys la value OU créer une classe enigme 
list_enigme = {
    'enigme1':'peter',
    'enigme2':'feter',
    'enigme3':'reter',
}

def game ():
    fct.intro()
    a=fct.choix_boss(list_boss,list_enigme) #pour avoir le nom du boss qui se trouve dans une liste
    print(a[0])
    fct.nom_hero(list_heros)
    fct.tour(sauron,list_heros,guerrier,mage,archer)

game()



