
import fonction as fct
import class_c as cls 

# Instanciation 

# Boss
sauron = cls.boss("Sauron",{},350,10)
chronos = cls.boss("Chronos",{},400,10)
lilith = cls.boss("Lilith",{},250,10)

# Héros 
guerrier = cls.guerrier("Guerrier","guerrier","Défense",100,8,0)
mage = cls.mage("Mage","mage",None,80,9,10)
archer = cls.archer("Archer","archer",None,60,6,10)

# Lieu 
cimetiere =cls.Lieu("Cimetière ",[])
shop = cls.Shop("Shop",["Vendeur"],[],[])

# Armes 
baguette = cls.Armes("archmage",12,"mage")
epee = cls.Armes("Sabre",15,"guerrier")
archer = cls.Armes("ShieldBow",14,"archer")

# Objets 
objets =  cls.obet


# Création des variables : 

list_boss = [sauron,chronos,lilith]
list_heros = [guerrier,mage,archer]
list_armes =[baguette,epee,archer]

# Stocker les enigmes dans un dico afin de faire correspondre plus tard la keys la value OU créer une classe enigme 
list_enigme = {
    "Qu'est-ce qui peut être dans la mer et dans le ciel ?":'etoile',
    "Qu'est-ce qui fait le tour de la maison sans bouger ?":'mur',
    "Qu'est-ce qui est plein de trous mais arrive quand même à retenir l'eau ?":'eponge',
}

def game ():
    fct.intro()
    boss_select=fct.choix_boss(list_boss,list_enigme) #pour avoir le nom du boss qui se trouve dans une liste
    fct.nom_hero(list_heros)
    fct.tour(boss_select,list_heros,guerrier,mage,archer,cimetiere,list_enigme,list_boss)

game()
