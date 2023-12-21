import random

def rajout (_shop_destination,_list_item):
    for item in _list_item :
        _shop_destination.append(item)
    
def intro ():
    print("\nHello to GeeksOfLegends , in this game you will fight a boss between 3 terrible monster\n")
    
def choix_boss(list_boss,list_enigme):
    boss_fight = random.choice(list_boss)
    print(f"For this game, you will fight {boss_fight}")
    boss_fight.enigme = random.choice(list(list_enigme.items()))
    print(boss_fight.enigme)
    return boss_fight

def nom_hero(list_hero):
    print(f"Here you ar the hero you will play : {list_hero} \n")
    
    for hero in list_hero:
        name_choice = input(f"Please choice their name {hero} ")
        hero.nom = name_choice
        print(hero.nom)
    print(f"Here your hero's name : {list_hero}")
        
def choix_posture(hero,boss):
    while True :
        posture = str(input(f"Please choice your posture, fight(F) or defense(D) ")).lower().strip()
        if posture == "f":
            hero.posture = "Attaque"
            print(f"Voici la posture de votre héros : {hero.posture}")
            hero.postures(boss)
            # print(hero)
            return hero.posture
        elif posture == "d":
            hero.posture = "Défense"
            print(hero.posture)
            return hero.posture
        
def enigme(boss,cimetiere,list_heros):
    essais = 3
    while essais > 0:
        enigme_reponse = str(input(f"Here your enigm {boss.enigme[0]}\nYou have {essais} try to find it or you loose : ")).strip().lower()
        if enigme_reponse != boss.enigme[1]:
            essais -= 1
            print(f"You re wrong ! You have {essais} left to find it  ")
        elif enigme_reponse == boss.enigme[1]:
            print("You won .. GG ")
            
            cimetiere.lieu.append(boss)
            print(cimetiere.lieu)
            
            return True
    else :
        print("You loose the game  ... MOUHAHAHHA")
        cimetiere.lieu.append(list_heros)
        print(cimetiere.lieu)
        return False
def verif_type_arme(hero,choix,shop):
    
    if hero.type == choix.type and hero.argent >= choix.prix:
        shop.vendre_arme(hero,choix)
        print ("c'est ok ")
    elif hero.type != choix.type :
        print("Vous ne pouvez pas acheter cette objet")
    elif hero.argent < choix.prix :
        print("Vous avez pas assez d'argent ")
        
def verif_type_objet(hero,choix,shop):
    
    if hero.type in choix.type and hero.argent >= choix.prix:
        shop.vendre_objet(hero,choix)
        print ("c'est ok ")
    elif hero.type != choix.type :
        print("Vous ne pouvez pas acheter cette objet")
    elif hero.argent < choix.prix :
        print("Vous avez pas assez d'argent ")
        
def display_shopping(shop,list_heros):
    for hero in list_heros :
        print(f"Welcome {hero} to my {shop} dear heros hopeless {hero.type} ")
        affichage = str(input(f"Enter what do you want to see : \n 1 : Armes \n 2 : Objets \n 3 : Exit \n ")).strip()
        
        while True : 
            if affichage == "1" :
                for (i, item) in enumerate(shop.armes, start=1):
                    print(i, item)
                    print(item.type)
                print(i+1,"Exit")
                print("")
                choix = str(input("Choose your item : "))
                if choix == "1":
                    choix = shop.armes[0]
                    verif_type_arme(hero,choix,shop)     
                elif choix == "2":
                    choix = shop.armes[1]
                    verif_type_arme(hero,choix,shop)    
                elif choix == "3":
                    choix = shop.armes[2]
                    verif_type_arme(hero,choix,shop)    
                elif choix == "4":
                    affichage = str(input(f"Enter what do you want to see : \n 1 : Armes \n 2 : Objets \n 3 : Exit \n ")).strip()
                         
            elif affichage == "2" :
                for (i, item) in enumerate(shop.objets, start=1):
                    print(i, item)
                    print(item.type)
                print(i+1,"Exit")
                print("")
                choix = str(input("Choose your item : "))
                if choix == "1":
                    choix = shop.objets[0]
                    verif_type_objet(hero,choix,shop)
                    print()    
                elif choix == "2":
                    choix = shop.objets[1]
                    verif_type_objet(hero,choix,shop)
                elif choix == "3":
                    choix = shop.objets[2]
                    verif_type_objet(hero,choix,shop)
                elif choix == "4":
                    choix = shop.objets[3]
                    verif_type_objet(hero,choix,shop)
                elif choix == "5":
                    affichage = str(input(f"Enter what do you want to see : \n 1 : Armes \n 2 : Objets \n 3 : Exit \n ")).strip()
                          
            elif affichage == "3":
                print("")
                print(f"{hero} est  sorti du shop")
                print("")
                break
        
    for hero in list_heros:
        print(hero.armes)
        print(hero.inventaire)
        
def tour (boss,list_hero,guerrier,mage,archer,cimetiere,list_enigme,list_boss):
    boss = choix_boss(list_boss,list_enigme)
    nbr_tour = 1
    reset_atk_guerrier = list_hero[0].atk
    reset_atk_mage = list_hero[1].atk
    reset_atk_archer = list_hero[2].atk
    reset_atk_boss = boss.atk
    vie_base_boss = boss.vie

    while boss.vie > 0 or len(list_hero) >0 : 
        print(f"---------------------- Debut du {nbr_tour} tours -------------------")
        for hero in list_hero:
            print("------------------------------------------------------------------------")
            print(f"For this round will fight one by one  , the next to play is: {hero}")
            print(f"Voici la vie du boss : {boss.vie}")
            posture =choix_posture(hero,boss)
            attaque_defense_guerrier(hero,guerrier,boss,reset_atk_boss,posture)
            attaque_defense_mage(hero,mage,boss,reset_atk_boss,posture)   
            attaque_defense_archer(hero,archer,boss,reset_atk_boss,posture)
                
        if boss.vie < (vie_base_boss * 0.1):
            enigme(boss,cimetiere,list_hero)
            if enigme == False or True:
                break
        # if boss.vie <=0 :
        #     print(f"GG ! You fought the boss !!")
        #     break
            
        elif len(list_hero) == 0:
            print("Everybody is dead .. You LOOSE ")
            print(cimetiere.lieu)
            break
        else: 
            print("-------------------------------------------------------")
            print("Its the end of heros'tours , now it's BOSS TIME ")
            aim = random.choice(list_hero)
            boss.atk_boss(aim)
            if aim.vie <= 0 :
                aim.mourrir()
                print(f"{boss.nom} a tué {aim} ,vie de la cible {aim.vie}")
                list_hero.remove(aim)
                print(list_hero)
                cimetiere.lieu.append(aim)
                print(cimetiere.lieu)
            else:
                print(f"degats du boss {boss.atk}, vie de la cible {aim.vie}") 
        print(f"----------------------- Fin du tour {nbr_tour} ------------------------")
        nbr_tour +=1
        archer.atk = reset_atk_archer
        guerrier.atk = reset_atk_guerrier
        mage.atk = reset_atk_mage
        boss.atk = reset_atk_boss
        

def attaque_defense_guerrier (_hero,_type_hero,_boss,_reset_atk_boss,posture):
    if _hero ==_type_hero :
        _type_hero.equiper_arme()
        if posture =="Attaque":
            _hero.attaque_guerrier(_boss)
            print(f"Attaque du hero {_hero.atk}, vie du boss après attaque  :{_boss.vie},")
            if _boss.vie <= 0 :
                return False
        elif posture == "Défense":
            _type_hero.equiper_objet()
            _boss.atk = _reset_atk_boss
            _hero.postures(_boss)
            
def attaque_defense_mage (_hero,_type_hero,_boss,_reset_atk_boss,posture):
    if _hero ==_type_hero :
        _type_hero.equiper_arme()
        if posture =="Attaque":
            _hero.attaque_mage(_boss)
            print(f"Attaque du hero {_hero.atk}, vie du boss après attaque  :{_boss.vie},")
            if _boss.vie <= 0 :
                return 
        elif posture == "Défense":
            _type_hero.equiper_objet()
            _boss.atk = _reset_atk_boss
            _hero.postures(_boss)
    
def attaque_defense_archer(_hero,_type_hero,_boss,_reset_atk_boss,posture):
    if _hero ==_type_hero :
        _type_hero.equiper_arme()
        if posture =="Attaque":
            _hero.attaque_archer(_boss)
            print(f"Attaque du hero {_hero.atk}, vie du boss après attaque  :{_boss.vie},")

            if _boss.vie <= 0 :
                return False
        elif posture == "Défense":
            _type_hero.equiper_objet()
            _boss.atk = _reset_atk_boss
            _hero.postures(_boss)
    
# Rajout fonction display les personnags et leurs point de vie et atk a la fin de chaque tour 
# rajout fonction display de l enigme 
# rajout fonction display endgame 


#rajout fonction utilisation d'armes
# rajout fonction utilisation d'objets
# rajout forgeron

