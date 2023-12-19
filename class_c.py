import random
import time
from typing import Any
# import main 
import fonction as fct 

class boss():
    def __init__(self,nom,enigme,vie =int,atk = int):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk
        self.enigme = enigme
        
    def atk_boss (self,hero):
        print(f"{self.nom} Va attaquer {hero}")
        hero.vie -= self.atk
    
    def enigme_boss(self,vie):
        if self.vie <= (vie*20)/100:
            print(f"{self.nom} Here your enigma : {self.enigme} ")
        
    def __repr__(self):
        return self.nom
class heros():
    def __init__(self,nom,posture ="",vie = int,atk =int ):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk 
        self.posture = posture
        
    def mourrir (self):
        if self.vie < 0 :
            print(f"{self.nom} is dead because he didn't have enough life point")  
    def postures(self,boss) :
        if self.posture == "Attaque":
            self.atk *= 1.4
        elif self.posture == "Défense":
            boss.atk = boss.atk/2

    def __repr__(self):
        return self.nom
    
class guerrier (heros):
    def __init__(self, nom,posture ="",vie = int, atk = int ,rage =int ):
        super().__init__(nom,posture, vie, atk)
        self.rage = rage
        
    def attaque_guerrier(self,ennemi):
        print(f"Voici le nombre de rage {self.rage}")
        if self.rage < 4:
            # self.atk *=1.25
            ennemi.vie -= self.atk
        else :
            self.atk *=1.25
            ennemi.vie -= self.atk
            
        self.rage+=1

class mage (heros):
    def __init__(self, nom,posture ="" ,vie = int , atk =int , mana =int):
        super().__init__(nom,posture, vie, atk)
        self.mana = mana
        
            
    def attaque_mage(self,ennemi):
        print(f"voici le nombre de mana {self.mana}")
        if self.mana >= 2:
            self.mana -= 2
            ennemi.vie -= self.atk
            
        else:
            print(f"You don't have enough mana {self.mana}")
            if self.mana < 2 :
                self.mana += 7
            print(f"You regen 7 mana , here your mana {self.mana} ")
    
class archer (heros):
    def __init__(self, nom,posture ="", vie = int, atk = int, fleche = int):
        super().__init__(nom,posture, vie, atk)
        self.fleche = fleche 
    
    def attaque_archer(self,ennemi):
        print(f"voici le nombre de fleche {self.fleche}")
        if self.fleche >= 2:
            self.fleche -= 2
            ennemi.vie -= self.atk
        else:
            print(f"You don't have enought arrow {self.fleche}")
            if self.fleche < 2 :
                self.fleche += 6
            print(f"you regen your bow, you have 6 , here your bow {self.fleche}")

class Lieu ():
    def __init__(self,nom, lieu = []):
        self.nom = nom
        self.lieu = lieu 
    def __repr__(self):
        return self.nom
        
