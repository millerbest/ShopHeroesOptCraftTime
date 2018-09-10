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

class SkillRandom():
    def __init__(self, item, list_workers, n):
        self.item = item
        self.list_workers = list_workers
        self.item_param = self._get_item_parameters()
        self.n = n
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

    def _random(self):
        new_worker_list = []
        for worker in self.list_workers:
            worker.random_skills()
            new_worker_list.append(worker)
        return new_worker_list

    def run(self):
        list_results = []
        list_tried_wokers = []
        for i in range(0, self.n):
            worker_params = Worker_params()
            new_worker_list = self._random()
            for worker in new_worker_list:
                worker_params += worker.get_worker_params()
            list_results.append(self.item.getCraftTime(worker_params))
            list_tried_wokers.append(new_worker_list)

        import matplotlib.pyplot as plt
        print (np.min(list_results))
        for w in list_tried_wokers[np.argmin(list_results)]:
            print (w)
        


        plt.hist(list_results, bins=np.arange(0, 2000, 10))
        plt.show()



if __name__ == "__main__":
    from Worker_params import Worker_params
    from Worker import Worker, WorkerLoader
    from Item import Item, ItemLoader
    
    il = ItemLoader("wisdom-ocarina")
    item = il.get_item()

    worker_name_level_list = [("master",34),
                              ("seamstress",37),
                              ("sculptor",39),
                              ("artisan",39),
                              ("wizard",38),
                              ("alchemist",36),
                              ("the-giant",36),
                              ("luthier",31)]

    
    list_workers = []
    for worker_name_level in worker_name_level_list:
        worker_loader = WorkerLoader(worker_name_level[0], worker_name_level[1])
        list_workers.append(worker_loader.get_worker())
    

    skillRandom = SkillRandom(item, list_workers, 10000)
    skillRandom.run()

    #skill_opt = SkillOptimizer(item, list_workers)
    #skill_opt.optimize()