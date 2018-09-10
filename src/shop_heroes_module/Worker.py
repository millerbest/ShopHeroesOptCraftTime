import numpy as np
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "db"))
from worker_db import worker_db
from shop_heroes_module.Worker_params import Worker_params

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

    def set_rough_init_skill_points(self):
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
        return 

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
    
    def get_total_used_skill_points(self):
        result = 0
        for item in [self.textile,
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
                     self.mastery]:
            if item >= 0:
                result += item
        result = result - self.get_init_total_skill_points()
        return result

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

    def get_total_skill_points(self):
        """Get the constraints that will be used for scipy optimizer""" 
        total_free_skills_points = self.level * self.skill_per_level
        total_used_skill_points = self.get_total_used_skill_points()
        total_skills_points = total_free_skills_points - total_used_skill_points
        #Not finished
        return total_skills_points
    
    def get_init_total_skill_points(self):
        counter = 0
        if self.textile != -1:
            counter += 1
        if self.armor != -1:
            counter += 1
        if self.metal != -1:
            counter += 1
        if self.weapon != -1:
            counter += 1
        if self.wood != -1:
            counter += 1
        if self.alchemy != -1:
            counter += 1
        if self.magic != -1:
            counter += 1
        if self.tinker != -1:
            counter += 1
        if self.jewel != -1:
            counter += 1
        if self.arts_crafts != -1:
            counter += 1
        if self.rune != -1:
            counter += 1
        if self.mastery != -1:
            counter += 1
        return counter * self.init_skill_points

    def get_worker_params(self):
        result = Worker_params({"textile":self.textile,
                                "armor":self.armor,
                                "metal":self.metal,
                                "weapon":self.weapon,
                                "wood":self.wood,
                                "alchemy":self.alchemy,
                                "magic":self.magic,
                                "tinker":self.tinker,
                                "jewel":self.jewel,
                                "arts_crafts":self.arts_crafts,
                                "rune":self.rune,
                                "mastery":self.mastery})
        return result

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

class WorkerLoader():
    def __init__(self, worker_name, level):
        self.db = worker_db
        self.worker_data = self.db[worker_name]
        self.worker_params = self._get_worker_parameters()
        self.worker_level = level
        
    def _get_worker_parameters(self):
        worker_params = Worker_params({"textile":-1,
                                       "armor":-1,
                                       "metal":-1,
                                       "weapon":-1,
                                       "wood":-1,
                                       "alchemy":-1,
                                       "magic":-1,
                                       "tinker":-1,
                                       "jewel":-1,
                                       "arts_crafts":-1,
                                       "rune":-1,
                                       "mastery":0})

        for k in self.worker_data.keys():
            if k.startswith("skill"):
                if self.worker_data[k][0] == 'textile-working':
                    worker_params.textile = self.worker_data[k][1]
                elif self.worker_data[k][0] == "armor-crafting":
                    worker_params.armor = self.worker_data[k][1]
                elif self.worker_data[k][0] == 'metal-working':
                    worker_params.metal = self.worker_data[k][1]
                elif self.worker_data[k][0] == "weapon-crafting":
                    worker_params.weapon = self.worker_data[k][1]
                elif self.worker_data[k][0] == "wood-working":
                    worker_params.wood = self.worker_data[k][1]
                elif self.worker_data[k][0] == "alchemy":
                    worker_params.alchemy = self.worker_data[k][1]
                elif self.worker_data[k][0] == "magic":
                    worker_params.magic = self.worker_data[k][1]
                elif self.worker_data[k][0] == "tinkering":
                    worker_params.tinker = self.worker_data[k][1]
                elif self.worker_data[k][0] == "jewelry":
                    worker_params.jewel = self.worker_data[k][1]
                elif self.worker_data[k][0] == "arts-and-crafts":
                    worker_params.arts_crafts = self.worker_data[k][1]
                elif self.worker_data[k][0] == "rune-writing":
                    worker_params.rune = self.worker_data[k][1]
        return worker_params

    def get_worker(self):
        worker = Worker(self.worker_params)
        worker.level = self.worker_level
        worker.skill_per_level = self.worker_data['per-level']
        return worker

if __name__ == "__main__":
    worker_name = "master"
    wl = WorkerLoader(worker_name, 30)
    worker = wl.get_worker() 
    print (worker)