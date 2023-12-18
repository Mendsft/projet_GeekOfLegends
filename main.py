import random
import time
import fonction as fct
import class_c as cls 

# Instanciation 

# Boss
sauron = cls.boss("Sauron","",350,10)
chronos = cls.boss("Chronos","",400,7)
lilith = cls.boss("Lilith","",250,12)

# Héros 
guerrier = cls.guerrier("Guerrier",100,5,0)
mage = cls.mage("Mage",80,7,10)
archer = cls.archer("Archer",60,6,10)

# Création des variables : 

list_boss = [sauron,chronos,lilith]
list_heros = [guerrier,mage,archer]

def game ():
    fct.intro()
    fct.choix_boss(list_boss)
    fct.nom_hero(list_heros)

game()