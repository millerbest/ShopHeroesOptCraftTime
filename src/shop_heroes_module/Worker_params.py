import numpy as np

class Worker_params():
    def __init__(self, *args):
        if len(args) == 0:
            self.textile = 0
            self.armor = 0
            self.metal = 0
            self.weapon = 0
            self.wood = 0
            self.alchemy = 0
            self.magic = 0
            self.tinker = 0
            self.jewel = 0
            self.arts_crafts = 0
            self.rune = 0
            self.mastery = 0
        
        elif len(args) == 1:
            self.textile = args[0]["textile"]
            self.armor = args[0]["armor"]
            self.metal = args[0]["metal"]
            self.weapon = args[0]["weapon"]
            self.wood = args[0]["wood"]
            self.alchemy = args[0]["alchemy"]
            self.magic = args[0]["magic"]
            self.tinker = args[0]["tinker"]
            self.jewel = args[0]["jewel"]
            self.arts_crafts = args[0]["arts_crafts"]
            self.rune = args[0]["rune"]
            self.mastery = args[0]["mastery"]
        
        else:
            raise Exception("wrong number of input")
    
    def _get_max_skill_points(self):
        return np.max([self.textile,
                      self.armor,
                      self.metal,
                      self.weapon,
                      self.wood,
                      self.alchemy,
                      self.magic,
                      self.tinker,
                      self.jewel,
                      self.arts_crafts,
                      self.rune,
                      self.mastery])


    def _minus_filter(self, value):
        if value < 0 :
            return 0
        else: 
            return value

    def set_null(self):
        self.textile = -1
        self.armor = -1
        self.metal = -1
        self.weapon = -1
        self.wood = -1
        self.alchemy = -1
        self.magic = -1
        self.tinker = -1
        self.jewel = -1
        self.arts_crafts = -1
        self.rune = -1
        self.mastery = -1
        return 
        
    def __add__(self, other):
        result = Worker_params()
        result.textile = self._minus_filter(self.textile) + self._minus_filter(other.textile)
        result.armor = self._minus_filter(self.armor) + self._minus_filter(other.armor)
        result.metal = self._minus_filter(self.metal) + self._minus_filter(other.metal)
        result.weapon = self._minus_filter(self.weapon) + self._minus_filter(other.weapon)
        result.wood = self._minus_filter(self.wood) + self._minus_filter(other.wood)
        result.alchemy = self._minus_filter(self.alchemy) + self._minus_filter(other.alchemy)
        result.magic = self._minus_filter(self.magic) + self._minus_filter(other.magic)
        result.tinker = self._minus_filter(self.tinker) + self._minus_filter(other.tinker)
        result.jewel = self._minus_filter(self.jewel) + self._minus_filter(other.jewel)
        result.arts_crafts = self._minus_filter(self.arts_crafts) + self._minus_filter(other.arts_crafts)
        result.rune = self._minus_filter(self.rune) + self._minus_filter(other.rune)
        result.mastery = self._minus_filter(self.mastery) + self._minus_filter(other.mastery)
        return result

    def __sub__(self, other):
        result = Worker_params()
        result.textile = self._minus_filter(self.textile) - self._minus_filter(other.textile)
        result.armor = self._minus_filter(self.armor) - self._minus_filter(other.armor)
        result.metal = self._minus_filter(self.metal) - self._minus_filter(other.metal)
        result.weapon = self._minus_filter(self.weapon) - self._minus_filter(other.weapon)
        result.wood = self._minus_filter(self.wood) - self._minus_filter(other.wood)
        result.alchemy = self._minus_filter(self.alchemy) - self._minus_filter(other.alchemy)
        result.magic = self._minus_filter(self.magic) - self._minus_filter(other.magic)
        result.tinker = self._minus_filter(self.tinker) - self._minus_filter(other.tinker)
        result.jewel = self._minus_filter(self.jewel) - self._minus_filter(other.jewel)
        result.arts_crafts = self._minus_filter(self.arts_crafts) - self._minus_filter(other.arts_crafts)
        result.rune = self._minus_filter(self.rune) - self._minus_filter(other.rune)
        result.mastery = self._minus_filter(self.mastery) - self._minus_filter(other.mastery)
        return result

    def __str__(self):
        text = "textile: %s\narmor: %s\nmetal: %s\nweapon: %s\nwood: %s\nalchemy: %s\nmagic: %s\ntinker: %s\n\
jewel: %s\narts_crafts: %s\nrune: %s\nmastery: %s\n" %\
               (self.textile,
                self.armor,
                self.metal,
                self.weapon,
                self.wood,
                self.alchemy,
                self.magic,
                self.tinker,
                self.jewel,
                self.arts_crafts,
                self.rune,
                self.mastery)
        return text

if __name__ == "__main__":
    w_p = Worker_params()
    print (w_p)