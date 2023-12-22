
import fonction as fct
import class_c as cls 

# Instanciation gu

# Boss
sauron = cls.boss("Sauron",{},350,10)
chronos = cls.boss("Chronos",{},400,10)
lilith = cls.boss("Lilith",{},250,10)

# Héros 
guerrier = cls.guerrier("Guerrier",[],200,[],"guerrier","",200,8,0)
mage = cls.mage("Mage",[],200,[],"mage","",180,9,10)
archer = cls.archer("Archer",[],200,[],"archer","",160,6,10)

# Lieu 
cimetiere =cls.Lieu("Cimetière ",[])
boss_cimetier = cls.Lieu("Cimetiere des boss",[])
shop = cls.Shop("Shop",["Vendeur"],[],[],100)
forgeron = cls.Forgeron("Forgeron",["Ornn"],[],1000)

# Armes 
baguette = cls.Armes("archmage",12,"mage",100)
epee = cls.Armes("Sabre",15,"guerrier",100)
arc = cls.Armes("ShieldBow",14,"archer",100)

# Armes Amélioré
grosse_baguette =cls.ArmesAmerliore("ArchAnge",18,"mage",200)
gross_epee = cls.ArmesAmerliore("Hache",20,"guerrier",200)
gros_arc = cls.ArmesAmerliore("Bowlder",20,"archer",200)

# Objets ◊
potion_vie =  cls.Objet("Potion de vie","Augmente la vie de 50 PV ","guerrier,mage,archer",20)
potion_rage =  cls.Objet("Potion de rage","Augmente les degats de 2","guerrier",20)
potion_mana =  cls.Objet("Potion de mana","Augmente la mana de 15","mage",20)
potion_fleche =  cls.Objet("Potion de fleche","Augmente les fleches de 10 ","archer",20)


# Création des variables : 

list_boss = [sauron,chronos,lilith]
list_heros = [guerrier,mage,archer]
list_armes = [baguette,epee,arc]
list_objets =[potion_vie,potion_rage,potion_mana,potion_fleche]
list_armes_ameliore =[gros_arc,grosse_baguette,gross_epee]

# Stocker les enigmes dans un dico afin de faire correspondre plus tard la keys la value OU créer une classe enigme 
list_enigme = {
    "Qu'est-ce qui peut être dans la mer et dans le ciel ?":'etoile',
    "Qu'est-ce qui fait le tour de la maison sans bouger ?":'mur',
    "Qu'est-ce qui est plein de trous mais arrive quand même à retenir l'eau ?":'eponge',
}

def game ():
    
    try:
        fct.rajout(shop.armes,list_armes)
        fct.rajout(shop.objets,list_objets)
        fct.rajout(forgeron.armes,list_armes_ameliore)
        fct.intro()
        fct.nom_hero(list_heros)
        # fct.display_shopping(shop,list_heros,forgeron)
        
        # fct.display_forgeron(forgeron,list_heros,shop)
    
        print(list_boss)
        for boss in list_boss:
            if len(list_heros) == 0 :
                break
            
            fct.display_shopping(shop,list_heros,forgeron)
            boss=fct.choix_boss(list_boss,list_enigme,boss_cimetier) #pour avoir le nom du boss qui se trouve dans une liste
            fct.tour(boss,list_heros,guerrier,mage,archer,cimetiere,boss_cimetier)

        if len(list_heros) == 0 :
                return False 
        else:
            fct.display_shopping(shop,list_heros,forgeron)
            boss=fct.choix_boss(list_boss,list_enigme,boss_cimetier) #pour avoir le nom du boss qui se trouve dans une liste
            fct.tour(boss,list_heros,guerrier,mage,archer,cimetiere,boss_cimetier)
            print(f"{list_boss} Voici la liste des boss en vie \n")
            print(f"{boss_cimetier.lieu} Voici la liste des boss Mort ")
            print("------------------------------------------------------------------------")
            print(fct.display_recap(list_heros))
            print(cimetiere.lieu)
            print("------------------------------------------------------------------------")
            print("                | Fin de tous les boss |                ")
            print("------------------------------------------------------------------------")
    except KeyboardInterrupt:
        print('Interrupted')
            
game()
# print(fct.display_armes(list_armes))


