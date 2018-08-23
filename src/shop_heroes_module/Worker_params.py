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

    def __add__(self, other):
        result = Worker_params()
        result.textile = self.textile + other.textile
        result.armor = self.armor + other.armor
        result.metal = self.metal + other.metal
        result.weapon = self.weapon + other.weapon
        result.wood = self.wood + other.wood
        result.alchemy = self.alchemy + other.alchemy
        result.magic = self.magic + other.magic
        result.tinker = self.tinker + other.tinker
        result.jewel = self.jewel + other.jewel
        result.arts_crafts = self.arts_crafts + other.arts_crafts
        result.rune = self.rune + other.rune
        result.mastery = self.mastery + other.mastery
        return result

    def __sub__(self, other):
        result = Worker_params()
        result.textile = self.textile - other.textile
        result.armor = self.armor - other.armor
        result.metal = self.metal - other.metal
        result.weapon = self.weapon - other.weapon
        result.wood = self.wood - other.wood
        result.alchemy = self.alchemy - other.alchemy
        result.magic = self.magic - other.magic
        result.tinker = self.tinker - other.tinker
        result.jewel = self.jewel - other.jewel
        result.arts_crafts = self.arts_crafts - other.arts_crafts
        result.rune = self.rune - other.rune
        result.rune = self.mastery - other.mastery
        return result

