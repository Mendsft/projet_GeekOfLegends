import random


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
        
def enigme(boss,cimetiere):
    essais = 3
    while essais > 0:
        enigme_reponse = str(input(f"Here your enigm {boss.enigme[0]}\nYou have {essais} try to find it or you loose : ")).strip().lower()
        if enigme_reponse != boss.enigme[1]:
            essais -= 1
            print(f"You re wrong ! You have {essais} left to find it  ")
        elif enigme_reponse == boss.enigme[1]:
            print("You won .. GG ")
            cimetiere.lieu.append(boss)
            return True
    else :
        print("You loose the game  ... MOUHAHAHHA")
        return False
        
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
            if hero == guerrier:
                if posture == "Attaque":
                    hero.attaque_guerrier(boss)
                    print(f"Attaque du hero {hero.atk}, vie du boss après attaque  :{boss.vie},")
                    if boss.vie <= 0 :
                        break
                elif posture == "Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
            if hero == mage:
                if posture == "Attaque":
                    hero.attaque_mage(boss)
                    print(f" attaque du hero {hero.atk}, vie du boss :{boss.vie},")
                    if boss.vie <=0:
                        break
                elif posture =="Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
            if hero == archer:
                if posture == "Attaque":
                    hero.attaque_archer(boss)
                    print(f"attaque du hero :{hero.atk}, vie du boss : {boss.vie},")
                    if boss.vie <=0 :
                        break
                elif posture =="Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
                    
        if boss.vie < (vie_base_boss * 0.2):
            enigme(boss,cimetiere)
            if enigme == False  or True:
                break
        elif boss.vie <=0 :
            print(f"GG ! You fought the boss !!")
            break
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
# Rajout fonction display les personnags et leurs point de vie et atk a la fin de chaque tour 
# rajout fonction display de l enigme 
# rajout fonction display endgame 