import random
import time
# import main 
import class_c as cls 

def intro ():
    print("Hello to GeeksOfLegends , in this game you will fight a boss between 3 terrible monster\n")
    
def choix_boss(list_boss):
    boss_fight = random.choice(list_boss)
    print(f"For this game, you will fight {boss_fight}")
    return boss_fight

def nom_hero(list_hero):
    print("To begin, please choose the name of your heros : \n")
    print(f"Here you ar the hero you will play : {list_hero} \n")
    for hero in list_hero:
        name_choice = input(f"Please choice their name {hero} ")
        hero.nom = name_choice
        print(hero.nom)

def choix_posture(hero):
    while True :
        posture = str(input(f"Please choice your posture, fight(F) or defense(D) ")).lower().strip()
        if posture == "f":
            hero.posture = "Attaque"
            print(hero.posture)
            
            return hero.posture
        elif posture == "d":
            hero.posture = "Défense"
            print(hero.posture)
            
            return hero.posture