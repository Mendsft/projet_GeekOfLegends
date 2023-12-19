import random
import time
import class_c as cls 


def intro ():
    print("\nHello to GeeksOfLegends , in this game you will fight a boss between 3 terrible monster\n")
    
def choix_boss(list_boss,list_enigme):
    boss_fight = random.choice(list_boss)
    print(f"For this game, you will fight {boss_fight}")
    boss_fight.enigme = random.choice(list(list_enigme.keys()))
    print(boss_fight.enigme)
    return boss_fight,boss_fight.enigme

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
            print(hero.posture)
            hero.postures(boss)
            print(hero)
            print(hero.posture)
            print(hero.atk)
            return hero.posture
        elif posture == "d":
            hero.posture = "Défense"
            # hero.posture(boss)

            print(hero.posture)
            return hero.posture
        
def tour (boss,list_hero,guerrier,mage,archer):
    nbr_tour = 1
    reset_atk_guerrier = list_hero[0].atk
    reset_atk_mage = list_hero[1].atk
    reset_atk_archer = list_hero[2].atk
    reset_atk_boss = boss.atk
    while boss.vie > 0 or len(list_hero) >0 : 
        print(f"Debut du {nbr_tour} tours ")

        for hero in list_hero:
            print(f"For this round will fight one by one  , the first to begin is : {hero}")
            posture =choix_posture(hero,boss)
            if hero == guerrier:
                if posture == "Attaque":
                    hero.attaque_guerrier(boss)
                    print(f" attaque du hero {hero.atk}, vie du boss{boss.vie},")
                    if boss.vie <= 0 :
                        break
                elif posture == "Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
            if hero == mage:
                if posture == "Attaque":
                    hero.attaque_mage(boss)
                    print(f" attaque du hero {hero.atk}, vie du boss{boss.vie},")
                    if boss.vie <=0:
                        break
                elif posture =="Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
                    
            if hero == archer:
                if posture == "Attaque":
                    hero.attaque_archer(boss)
                    print(f" attaque du hero {hero.atk}, vie du boss{boss.vie},")
                    if boss.vie <=0 :
                        break
                elif posture =="Défense":
                    boss.atk = reset_atk_boss
                    hero.postures(boss)
        if boss.vie <=0 :
            print(f"GG ! , you fought the boss !!")
            break
        elif len(list_hero) == 0:
            print("Everybody is dead .. You LOOSE ")
            break
        else:    
            print("Its the end of heros'tours , now it's BOSS TIME ")
            
            aim = random.choice(list_hero)
            boss.atk_boss(aim)
            if aim.vie <= 0 :
                print(f"{boss.nom} a tué {aim.vie} ,vie de la cible {aim.vie}")
                list_hero.remove(aim)
            else:
                print(f"degats du boss {boss.atk}, vie de la cible {aim.vie}")
                
            nbr_tour +=1
           
            archer.atk = reset_atk_archer
            guerrier.atk = reset_atk_guerrier
            mage.atk = reset_atk_mage
            boss.atk = reset_atk_boss
            print(f"Fin du tour {nbr_tour}")
 