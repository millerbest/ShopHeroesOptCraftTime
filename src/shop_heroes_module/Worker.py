import numpy as np
import random

class Worker():
    def __init__(self, params):
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
        self.params = params
        self._parse_property(params)

        self.level = 0
        self.skill_per_level = 0
        self.init_skill_points = 0

    def _parse_property(self, params):
        self.textile = params.textile
        self.armor = params.armor
        self.metal = params.metal
        self.weapon = params.weapon
        self.wood = params.wood
        self.alchemy = params.alchemy
        self.magic = params.magic
        self.tinker = params.tinker
        self.jewel = params.jewel
        self.arts_crafts = params.arts_crafts
        self.rune = params.rune
        self.mastery = params.mastery

    def _init_skills(self):
        if self.textile != -1:
            self.textile = self.init_skill_points
        if self.armor != -1:
            self.armor = self.init_skill_points
        if self.metal != -1:
            self.metal = self.init_skill_points
        if self.weapon != -1:
            self.weapon = self.init_skill_points
        if self.wood != -1:
            self.wood = self.init_skill_points
        if self.alchemy != -1:
            self.alchemy = self.init_skill_points
        if self.magic != -1:
            self.magic = self.init_skill_points
        if self.tinker != -1:
            self.tinker = self.init_skill_points
        if self.jewel != -1:
            self.jewel = self.init_skill_points
        if self.arts_crafts != -1:
            self.arts_crafts = self.init_skill_points
        if self.rune != -1:
            self.rune = self.init_skill_points
        if self.mastery != -1:
            self.mastery = self.init_skill_points

    def random_skills(self):
        total_skill_points = self.level * self.skill_per_level
        self._init_skills()
        list_skills = [self.textile,
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
                       self.mastery]
        list_index = [idx for idx, val in enumerate(list_skills) if val != -1]
        i = 0
        while i < total_skill_points:
            random_index = random.choice(list_index)
            list_skills[random_index]+=1
            i += 1
        
        self.textile = list_skills[0]
        self.armor = list_skills[1]
        self.metal = list_skills[2]
        self.weapon = list_skills[3]
        self.wood = list_skills[4]
        self.alchemy = list_skills[5]
        self.magic = list_skills[6]
        self.tinker = list_skills[7]
        self.jewel = list_skills[8]
        self.arts_crafts = list_skills[9]
        self.rune = list_skills[10]
        self.mastery = list_skills[11]
        return

    def __str__(self):
        return ("\
                textile: %s\n\
                armor: %s\n\
                metal: %s\n\
                weapon: %s\n\
                wood: %s\n\
                alchemy: %s\n\
                magic: %s\n\
                tinker: %s\n\
                jewel: %s\n\
                arts_crafts: %s\n\
                rune: %s\n\
                mastery: %s\n") %  (self.textile,
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



if __name__ == "__main__":
    from Worker_params import Worker_params
    param1 = {"textile":5,
              "armor":5,
              "metal":5,
              "weapon":5,
              "wood":-1,
              "alchemy":-1,
              "magic":-1,
              "tinker":-1,
              "jewel":-1,
              "arts_crafts":-1,
              "rune":-1,
              "mastery":5}
    
    params = Worker_params(param1)
    worker = Worker(params)
    worker.level = 30
    worker.skill_per_level = 5
    worker.random_skills()
    print (worker)