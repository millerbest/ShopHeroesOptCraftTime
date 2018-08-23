

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

if __name__ == "__main__":
    from Worker import Worker
    from Worker_params import Worker_params
    param1 = {"textile":500,
              "armor":500,
              "metal":500,
              "weapon":500,
              "wood":500,
              "alchemy":500,
              "magic":500,
              "tinker":500,
              "jewel":500,
              "arts_crafts":500,
              "rune":500}
    
    params = Item_params(param1)
    item = Item(params)

    param_w = {"textile":10,
               "armor":10,
               "metal":10,
               "weapon":10,
               "wood":10,
               "alchemy":10,
               "magic":10,
               "tinker":10,
               "jewel":10,
               "arts_crafts":10,
               "rune":10,
               "mastery":10}
    
    params = Worker_params(param_w)
    worker = Worker(params)
    worker.level = 30
    worker.skill_per_level = 5
    worker.random_skills()

    print (item.getCraftTime(worker))