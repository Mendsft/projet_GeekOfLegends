import random
import time
import main 
import fonction as fct 

class boss():
    def __init__(self,nom,vie ,atk,enigme):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk
        self.enigme = enigme
        
    def atk_boss (self,hero):
        print(f"{self.nom}Va attaquer {hero}")
        hero.vie -= self.atk
    
    def enigme_boss(self,vie):
        if self.vie <= (vie*20)/100:
            print(f"{self.nom} Here your enigma : {self.enigme} ")
        
class heros():
    def __init__(self,nom,vie,atk =int ):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk 
        
    def posture (self):
        pass
    
class guerrier (heros):
    def __init__(self, nom, vie, atk,rage =int ):
        super().__init__(nom, vie, atk)
        self.rage = rage
        
    def attaque_guerrier(self,ennemi):
        self.rage += 1
        ennemi.vie -= self.atk
    
    def rage_guerrier(self):
        if self.rage == 4 :
            return self.atk * 1.25

class mage (heros):
    def __init__(self, nom, vie, atk, mana =int):
        super().__init__(nom, vie, atk)
        self.mana = mana
        
    def attaque_mage(self,ennemi):
        if self.mana < 2:
            self.mana -= 2
            ennemi.vie -= self.atk
        else:
            print(f"You don't have enough mana {self.mana}")
            
    def regen_mage(self):
        if self.mana < 2 :
            self.mana += 7
    
class archer (heros):
    def __init__(self, nom, vie, atk, fleche = int):
        super().__init__(nom, vie, atk)
        self.fleche = fleche 
    
    def attaque_archer(self,ennemi):
        if self.fleche < 2:
            self.fleche -=2
            ennemi.vie -= self.atk
        else:
            print(f"You don't have enought arrow {self.fleche}")
        
        
        