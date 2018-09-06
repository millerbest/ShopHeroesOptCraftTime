import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "db"))

from item_db import item_db

class Item():
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
        self._parse_property(params)

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

    def getCraftTime(self, param_worker):
        return (self.textile / param_worker.textile + \
                self.armor / param_worker.armor +
                self.metal / param_worker.metal +
                self.weapon / param_worker.weapon +
                self.wood / param_worker.wood +
                self.alchemy / param_worker.alchemy +
                self.magic / param_worker.magic +
                self.tinker / param_worker.tinker +
                self.jewel / param_worker.jewel +
                self.arts_crafts / param_worker.arts_crafts +
                self.rune / param_worker.rune)

class Item_params():
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

        else:
            raise Exception("wrong number of input")

class ItemLoader():
    def __init__(self, item_name):
        self.db = item_db
        self.item_data = self.db[item_name]
        self.item_params = self._get_skills()

    def _get_skills(self):
        skills = self.item_data["skills"]
        item_params = Item_params()
        for k in skills.keys():
            if k ==  'textile-working':
                item_params.textile = skills[k]
            elif k == "armor-crafting":
                item_params.armor = skills[k]
            elif k == 'metal-working':
                item_params.metal = skills[k]
            elif k == "weapon-crafting":
                item_params.weapon = skills[k]
            elif k == "wood-working":
                item_params.wood = skills[k]
            elif k == "alchemy":
                item_params.alchemy = skills[k]
            elif k == "magic":
                item_params.magic = skills[k]
            elif k == "tinkering":
                item_params.tinker = skills[k]
            elif k == "jewelry":
                item_params.jewel = skills[k]
            elif k == "arts-and-crafts":
                item_params.arts_crafts = skills[k]
            elif k == "rune-writing":
                item_params.rune = skills[k]
        return item_params
            
    def get_item(self):
        item = Item(self.item_params)
        return item

        

if __name__ == "__main__":
    item_name = "nordic-lute"
    itemLoader = ItemLoader(item_name)
    item = itemLoader.get_item()
    print (item.alchemy)
    print (item.wood)
    print (item.textile)
    print (item.arts_crafts)
    print (item.jewel)