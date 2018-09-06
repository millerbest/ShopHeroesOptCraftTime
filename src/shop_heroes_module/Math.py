import numpy as np
from scipy.optimize import minimize
from scipy.optimize import least_squares

class SkillOptimizer():
    def __init__(self, item, list_workers):
        self.item = item
        self.list_workers = list_workers
        self.item_param = self._get_item_parameters()
        self.init_param = self._get_init_parameters()
        self.constraints = self._get_constraints()
        self.bounds = self._get_bounds()

    def fun_craft_time(self, x, p):
        return np.sum(p/x)
    
    def _get_constraints(self):
        print (self._get_total_skill_points())
        constraint = {'type': 'eq',
                      'fun' : lambda x: np.sum(x) - self._get_total_skill_points()}

        return constraint

    def _get_bounds(self):
        return ((0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None),
                (0, None))

    def _get_init_parameters(self):
        result = []
        item_parameter = self._get_item_parameters()
        total_skill_points = self._get_total_skill_points()
        skill_per_attr = total_skill_points/np.count_nonzero(item_parameter)

        for v in item_parameter:
            if v > 0:
                result.append(skill_per_attr)
            else:
                result.append(0.00001)

        return result

    def _get_total_skill_points(self):
        result = 0
        for worker in self.list_workers:
            result += worker.get_total_skill_points()
        return result


    def _get_item_parameters(self):
        return [self.item.textile,
                self.item.armor,
                self.item.metal,
                self.item.weapon,
                self.item.wood,
                self.item.alchemy,
                self.item.magic,
                self.item.tinker,
                self.item.jewel,
                self.item.arts_crafts,
                self.item.rune]

    def optimize(self):
        #print (self._get_constraints())
        #print (self.item_param)
        #print (self.init_param)
        
        res = minimize(self.fun_craft_time,
                       self.init_param,
                       args = self.item_param,
                       constraints = self._get_constraints(),
                       bounds = self.bounds)
        print (res)
        return res

if __name__ == "__main__":
    from Worker_params import Worker_params
    from Worker import Worker
    from Item import Item
    from Item import Item_params

    param1 = {"textile":5,
              "armor":5,
              "metal":5,
              "weapon":5,
              "wood":5,
              "alchemy":-1,
              "magic":-1,
              "tinker":-1,
              "jewel":-1,
              "arts_crafts":-1,
              "rune":-1,
              "mastery":5}
    
    params_worker1 = Worker_params(param1)
    worker1 = Worker(params_worker1)
    worker1.level = 50
    worker1.skill_per_level = 5
    
    param2 = {"textile":-1,
              "armor":5,
              "metal":-1,
              "weapon":5,
              "wood":-1,
              "alchemy":5,
              "magic":-1,
              "tinker":5,
              "jewel":-1,
              "arts_crafts":5,
              "rune":-1,
              "mastery":5}
    
    params_worker2 = Worker_params(param2)
    worker2 = Worker(params_worker2)
    worker2.level = 45
    worker2.skill_per_level = 10

    param3 = {"textile":5,
              "armor":-1,
              "metal":5,
              "weapon":5,
              "wood":-1,
              "alchemy":-1,
              "magic":-1,
              "tinker":5,
              "jewel":-1,
              "arts_crafts":-1,
              "rune":5,
              "mastery":5}
    
    params_worker3 = Worker_params(param3)
    worker3 = Worker(params_worker3)
    worker3.level = 40
    worker3.skill_per_level = 12
    
    param_item  =   {"textile":500,
                    "armor":0,
                    "metal":1500,
                    "weapon":2500,
                    "wood":0,
                    "alchemy":200,
                    "magic":0,
                    "tinker":0,
                    "jewel":0,
                    "arts_crafts":0,
                    "rune":0}
    
    params = Item_params(param_item)
    item = Item(params)
    
    list_workers = [worker1, worker2, worker3]
    skill_opt = SkillOptimizer(item, list_workers)
    skill_opt.optimize()