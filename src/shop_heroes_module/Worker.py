import numpy as np
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "db"))
from worker_db import worker_db
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
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
        
        self.init_params = Worker_params()

        self.level = 0
        self.skill_per_level = 0

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
                     self.rune]:
            if item >= 0:
                result += item
        result = result - self.get_init_total_skill_points()
        return result

    def get_remaining_skill_points(self):
        """Get the available points after skill points are assigned""" 
        total_points = self.level * self.skill_per_level
        total_used_skill_points = self.get_total_used_skill_points()
        remaining_points = total_points - total_used_skill_points

        return remaining_points
    
    def get_init_total_skill_points(self):
        result = 0
        for item in [self.init_params.textile,
                    self.init_params.armor,
                    self.init_params.metal,
                    self.init_params.weapon,
                    self.init_params.wood,
                    self.init_params.alchemy,
                    self.init_params.magic,
                    self.init_params.tinker,
                    self.init_params.jewel,
                    self.init_params.arts_crafts,
                    self.init_params.rune]:
            if item >= 0:
                result += item

        return result

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

    def set_worker_params(self, params):
        if self.textile >= 0:
            self.textile = params.textile
        if self.armor >= 0:
            self.armor = params.armor
        if self.metal >= 0:
            self.metal = params.metal
        if self.weapon >= 0:
            self.weapon = params.weapon
        if self.wood >= 0:
            self.wood = params.wood
        if self.alchemy >= 0:
            self.alchemy = params.alchemy
        if self.magic >= 0:
            self.magic = params.magic
        if self.tinker >= 0:
            self.tinker = params.tinker
        if self.jewel >= 0:
            self.jewel = params.jewel
        if self.arts_crafts >= 0:
            self.arts_crafts = params.arts_crafts
        if self.rune >= 0:
            self.rune = params.rune
        return


    def get_available_mastery(self):
        max_skill_point = self.get_worker_params()._get_max_skill_points()
        remaining_skill_point = self.get_remaining_skill_points()
        max_mastery_point = min(remaining_skill_point + self.init_params.mastery,
                                int(self.init_params.mastery + remaining_skill_point -\
                                 (self.init_params.mastery + remaining_skill_point - max_skill_point)/2.))
        return max_mastery_point

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
    def __init__(self, worker_name, level=30):
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
            if k == "mastery":
                worker_params.mastery = self.worker_data[k]
        return worker_params

    def get_worker(self):
        worker = Worker(self.worker_params)
        worker.level = self.worker_level
        worker.skill_per_level = self.worker_data['per-level']
        worker.init_params = self.worker_params
        return worker

if __name__ == "__main__":
    worker_name = "master"
    wl = WorkerLoader(worker_name, 30)
    worker = wl.get_worker() 
    print (worker)