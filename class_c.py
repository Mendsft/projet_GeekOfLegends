
import fonction as fct 

class boss():
    def __init__(self,nom,enigme={},vie =int,atk = int):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk
        self.enigme = enigme
        
    def atk_boss (self,hero):
        print(f"{self.nom} Va attaquer {hero}")
        hero.vie -= self.atk
    
    def enigme_boss(self,vie):
        if self.vie <= (vie*20)/100:
            print(f"----------------{self.nom} :  Here your enigma : {self.enigme} ---------------")
        
    def __repr__(self):
        return self.nom
class heros():
    def __init__(self,nom,armes=[],argent =int,inventaire = [],posture ="",vie = int,atk =int ):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk 
        self.posture = posture
        self.inventaire = inventaire
        self.argent = argent
        self.armes = armes
    
    def equiper_arme(self):
        if len(self.armes) == 1:
            print("j'ai une arme nen main")
            for arme in self.armes :
                self.atk = arme.atk
        else:
            print("You don't have weapons ")
    def equiper_objet (self):
        if len(self.inventaire) != 0:
            print("vous avez des objets :")
            for objet in self.inventaire :
                print(objet)
            print("What do you want to use ? : ")
        else:
            print("You have nothings in your inventory")
            
    def vendre_armes (self):
        if len(self.armes) != 0 :
            for i in self.armes :
                self.argent += (i.prix*0.7)
                self.armes.remove(i)
                print(f"Vous avez vendu {i} et vous avez mtn {self.argent}")
                break
        else :
            print(" you have ,nothing to sell ")
                
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
    def __init__(self,nom,armes=[],argent=int,inventaire =[],type= "guerrier",posture ="",vie = int, atk = int ,rage =int ):
        super().__init__(nom,armes,argent,inventaire,posture, vie, atk)
        self.rage = rage
        self.type = type
        
    def attaque_guerrier(self,ennemi):
        print(f"Voici le nombre de rage {self.rage}")
        if self.rage < 4:
            ennemi.vie -= self.atk
        else :
            self.atk *=1.25
            ennemi.vie -= self.atk
        self.rage+=1
        
    def __repr__(self):
        return self.nom
class mage (heros):
    def __init__(self, nom,armes=[],argent=int,inventaire =[],type="mage",posture ="" ,vie = int , atk =int , mana =int):
        super().__init__(nom,armes,argent,inventaire,posture, vie, atk)
        self.mana = mana
        self.type = type
        
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
            
    def __repr__(self):
        return self.nom
class archer (heros):
    def __init__(self, nom,armes=[],argent=int,inventaire =[],type = "archer" ,posture ="", vie = int, atk = int, fleche = int):
        super().__init__(nom,armes,argent,inventaire,posture, vie, atk)
        self.fleche = fleche
        self.type = type
    
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
            
    def __repr__(self):
        return self.nom
class Lieu ():
    def __init__(self,nom, lieu = []):
        self.nom = nom
        self.lieu = lieu 
        
    def __repr__(self):
        return self.nom
class Shop (Lieu):
    def __init__(self, nom, lieu=[],armes = [],objets=[],caisse =int):
        super().__init__(nom, lieu)
        self.armes = armes
        self.objets = objets 
        self.caisse = caisse 

    def vendre_arme (self,_hero,_item):
        _hero.armes.append(_item)
        _hero.argent -= _item.prix 
        self.caisse +=_item.prix    
            
    def vendre_objet (self,_hero,_item):
        # self.objets.remove(_item)
        _hero.inventaire.append(_item)
        _hero.argent -= _item.prix 
        self.caisse +=_item.prix
        
class Forgeron(Shop):
    def __init__(self, nom, lieu=[], armes=[], caisse=int):
        super().__init__(nom, lieu, armes,caisse)
        
    def vendre_arme_ameliore (self,_hero,_item):
        _hero.armes.pop()
        _hero.armes.append(_item)
        _hero.argent -= _item.prix 
        # self.caisse +=_item.prix    
class Armes ():
    def __init__(self,nom,atk,type,prix =int):
        self.nom = nom
        self.atk = atk 
        self.type = type 
        self.prix = prix 
        
    def __repr__(self):
        return self.nom
        
class ArmesAmerliore(Armes):
    def __init__(self, nom, atk, type,prix =int):
        super().__init__(nom, atk, type,prix)
        
class Objet():
    def __init__(self,nom,effets,type = "",prix =int):
        self.nom = nom
        self.effets = effets
        self.type = type
        self.prix = prix

    def popo_vie(self):
        self.vie +=50
        self.inventaire.pop()
        
    def popo_rage (self):
        self.atk += 2
        self.inventaire.pop()
        
    def popo_mana (self):
        self.mana +=15
        self.inventaire.pop()
        
    def popo_fleche (self):
        self.fleche += 10
        self.inventaire.pop()
        
    def __repr__(self):
        return self.nom
        
