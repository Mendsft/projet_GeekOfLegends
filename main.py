
import fonction as fct
import class_c as cls 

# Instanciation 

# Boss
sauron = cls.boss("Sauron",{},350,10)
chronos = cls.boss("Chronos",{},400,10)
lilith = cls.boss("Lilith",{},250,10)

# Héros 
guerrier = cls.guerrier("Guerrier",[],100,[],"guerrier","",100,8,0)
mage = cls.mage("Mage",[],100,[],"mage","",80,9,10)
archer = cls.archer("Archer",[],100,[],"archer","",60,6,10)

# Lieu 
cimetiere =cls.Lieu("Cimetière ",[])
shop = cls.Shop("Shop",["Vendeur"],[],[],100)

# Armes 
baguette = cls.Armes("archmage",12,"mage",100)
epee = cls.Armes("Sabre",15,"guerrier",100)
arc = cls.Armes("ShieldBow",14,"archer",100)

# Objets ◊
potion_vie =  cls.Objet("Potion de vie","Augmente la vie de 50 PV ","",20)
potion_rage =  cls.Objet("Potion de rage","Augmente les degats de 1 par nombres de rage ",guerrier,20)
potion_mana =  cls.Objet("Potion de mana","Augmente la mana de 15",mage,20)
potion_fleche =  cls.Objet("Potion de fleche","Augmente les fleches de 10 ",archer,20)


# Création des variables : 

list_boss = [sauron,chronos,lilith]
list_heros = [guerrier,mage,archer]
list_armes = [baguette,epee,arc]
list_objets =[potion_vie,potion_rage,potion_mana,potion_fleche]

# Stocker les enigmes dans un dico afin de faire correspondre plus tard la keys la value OU créer une classe enigme 
list_enigme = {
    "Qu'est-ce qui peut être dans la mer et dans le ciel ?":'etoile',
    "Qu'est-ce qui fait le tour de la maison sans bouger ?":'mur',
    "Qu'est-ce qui est plein de trous mais arrive quand même à retenir l'eau ?":'eponge',
}

def game ():
    fct.rajout(shop.armes,list_armes)
    fct.rajout(shop.objets,list_objets)
    fct.intro()
    boss_select=fct.choix_boss(list_boss,list_enigme) #pour avoir le nom du boss qui se trouve dans une liste
    fct.nom_hero(list_heros)
    fct.display_shopping(shop,list_heros,list_objets)
    fct.tour(boss_select,list_heros,guerrier,mage,archer,cimetiere,list_enigme,list_boss)

game()

