class boss():
    def __init__(self,nom,vie ,atk,enigme):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk
        self.enigme = enigme
        
    def atk_boss ():
        pass
    
    def enigme_boss():
        pass
    
class heros():
    def __init__(self,nom,vie,atk =int ):
        self.nom = nom 
        self.vie = vie 
        self.atk = atk 
        
    def posture ():
        pass
class guerrier (heros):
    def __init__(self, nom, vie, atk,rage =int ):
        super().__init__(nom, vie, atk)
        self.rage = rage

class mage (heros):
    def __init__(self, nom, vie, atk, mana =int):
        super().__init__(nom, vie, atk)
        self.mana = mana
    
class archer (heros):
    def __init__(self, nom, vie, atk, fleche = int):
        super().__init__(nom, vie, atk)
        self.fleche = fleche 
    
        
        