import sys
import os
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import least_squares
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from shop_heroes_module.Worker import WorkerLoader
from shop_heroes_module.Worker_params import Worker_params

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

class LargestGradientOptimizer():
    def __init__(self, item, worker, *args):
        self.item = item
        self.worker = worker
    
        if len(args) == 0:
            self.other_workers_params = None
        else:
            self.other_workers_params = args[0]
        
    def _getGradient(self, worker, craft_time_1):
        if self.other_workers_params is not None:
            craft_time_2 = self.item.getCraftTime(worker.get_worker_params()+self.other_workers_params)
        else:
            craft_time_2 = self.item.getCraftTime(worker.get_worker_params())
        return (craft_time_1 - craft_time_2)
        

    def _getGradients(self):
        g = []
        if self.other_workers_params is not None:
            t1 = self.item.getCraftTime(self.worker.get_worker_params()+self.other_workers_params)
        else:
            t1 = self.item.getCraftTime(self.worker.get_worker_params())

        if self.worker.textile != -1:
            self.worker.textile += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.textile -= 1
        else:
            g.append(-1)

        if self.worker.armor != -1:
            self.worker.armor += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.armor -= 1
        else:
            g.append(-1)
        if self.worker.metal != -1:
            self.worker.metal += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.metal -= 1
        else:
            g.append(-1)
        if self.worker.weapon != -1:
            self.worker.weapon += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.weapon -= 1
        else:
            g.append(-1)
        if self.worker.wood != -1:
            self.worker.wood += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.wood -= 1
        else:
            g.append(-1)
        if self.worker.alchemy != -1:
            self.worker.alchemy += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.alchemy -= 1
        else:
            g.append(-1)
        if self.worker.magic != -1:
            self.worker.magic += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.magic -= 1
        else:
            g.append(-1)
        if self.worker.tinker != -1:
            self.worker.tinker += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.tinker -= 1
        else:
            g.append(-1)
        if self.worker.jewel != -1:
            self.worker.jewel += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.jewel -= 1
        else:
            g.append(-1)
        if self.worker.arts_crafts != -1:
            self.worker.arts_crafts += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.arts_crafts -= 1
        else:
            g.append(-1)
        if self.worker.rune != -1:
            self.worker.rune += 1
            g.append(self._getGradient(self.worker, t1))
            self.worker.rune -= 1
        else:
            g.append(-1)
        
        return g
    
    def _add_point_to_largest_gradient(self, gradients):
        if self.worker.get_remaining_skill_points() > 0:
            if np.max(gradients) > 0:
                if np.argmax(gradients) == 0:
                    self.worker.textile += 1
                elif np.argmax(gradients) == 1:
                    self.worker.armor += 1
                elif np.argmax(gradients) == 2:
                    self.worker.metal += 1
                elif np.argmax(gradients) == 3:
                    self.worker.weapon += 1
                elif np.argmax(gradients) == 4:
                    self.worker.wood += 1
                elif np.argmax(gradients) == 5:
                    self.worker.alchemy += 1
                elif np.argmax(gradients) == 6:
                    self.worker.magic += 1
                elif np.argmax(gradients) == 7:
                    self.worker.tinker += 1
                elif np.argmax(gradients) == 8:
                    self.worker.jewel += 1
                elif np.argmax(gradients) == 9:
                    self.worker.arts_crafts += 1
                elif np.argmax(gradients) == 10:
                    self.worker.rune += 1
        return 

    def run(self):
        gradients = self._getGradients()
        self._add_point_to_largest_gradient(gradients)

class LargestGlobalGradientOptimizer():
    def __init__(self, item, worker_list):
        self.item = item
        self.worker_list = worker_list
        self.updated_worker_list = []
    
    def _get_sum_worker_params(self, list_workers):
        result_params = Worker_params()
        for worker in list_workers:
            result_params += worker.get_worker_params()
        return result_params

    def _getGradient(self, list_workers, t1):
        craft_time_1 = t1
        params = self._get_sum_worker_params(list_workers)
        craft_time_2 = self.item.getCraftTime(params)
        return (craft_time_1 - craft_time_2)

    def _getGradients(self):
        g = np.zeros([8, 11])
        params = self._get_sum_worker_params(self.worker_list)
        t1 = self.item.getCraftTime(params)

        for worker_idx, worker in enumerate(self.worker_list):
            new_worker_list = self.worker_list
            g[worker_idx] = self._getGraidentOfOneWorker(new_worker_list, worker_idx, t1)
        return g

    def _getGraidentOfOneWorker(self, list_worker, idx_worker, t1):
        current_worker = list_worker[idx_worker]
        g = []
        if current_worker.textile != -1:
            list_worker[idx_worker].textile += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].textile -= 1
        else:
            g.append(-1)

        if current_worker.armor != -1:
            list_worker[idx_worker].armor += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].armor -= 1
        else:
            g.append(-1)

        if current_worker.metal != -1:
            list_worker[idx_worker].metal += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].metal -= 1
        else:
            g.append(-1)
        if current_worker.weapon != -1:
            list_worker[idx_worker].weapon += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].weapon -= 1
        else:
            g.append(-1)
        if current_worker.wood != -1:
            list_worker[idx_worker].wood += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].wood -= 1
        else:
            g.append(-1)
        if current_worker.alchemy != -1:
            list_worker[idx_worker].alchemy += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].alchemy -= 1
        else:
            g.append(-1)
        if current_worker.magic != -1:
            list_worker[idx_worker].magic += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].magic -= 1
        else:
            g.append(-1)
        if current_worker.tinker != -1:
            list_worker[idx_worker].tinker += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].tinker -= 1
        else:
            g.append(-1)
        if current_worker.jewel != -1:
            list_worker[idx_worker].jewel += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].jewel -= 1
        else:
            g.append(-1)
        if current_worker.arts_crafts != -1:
            list_worker[idx_worker].arts_crafts += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].arts_crafts -= 1
        else:
            g.append(-1)
        if current_worker.rune != -1:
            list_worker[idx_worker].rune += 1
            g.append(self._getGradient(list_worker, t1))
            list_worker[idx_worker].rune -= 1
        else:
            g.append(-1)
        return g

    def _add_point_to_largest_gradient(self, gradients):
        indice_for_adding = self._get_next_indices_to_add(gradients)
        # while indice_for_adding is None and np.max(gradients) > 0:
        #     indices = np.where(gradients==gradients.max())
        #     #if indices[0].size > 1:
        #     indice_for_adding = self._choose_from_indices(indices)
        #     if indice_for_adding is None:
        #         for i in range(0, indices[0].size):
        #             gradients[indices[0][i]][indices[1][i]] = 0

        if indice_for_adding is not None:
            if indice_for_adding[1] == 0:
                self.worker_list[indice_for_adding[0]].textile += 1
            elif indice_for_adding[1] == 1:
                self.worker_list[indice_for_adding[0]].armor += 1
            elif indice_for_adding[1] == 2:
                self.worker_list[indice_for_adding[0]].metal += 1
            elif indice_for_adding[1] == 3:
                self.worker_list[indice_for_adding[0]].weapon += 1
            elif indice_for_adding[1] == 4:
                self.worker_list[indice_for_adding[0]].wood += 1
            elif indice_for_adding[1] == 5:
                self.worker_list[indice_for_adding[0]].alchemy += 1
            elif indice_for_adding[1] == 6:
                self.worker_list[indice_for_adding[0]].magic += 1
            elif indice_for_adding[1] == 7:
                self.worker_list[indice_for_adding[0]].tinker += 1
            elif indice_for_adding[1] == 8:
                self.worker_list[indice_for_adding[0]].jewel += 1
            elif indice_for_adding[1] == 9:
                self.worker_list[indice_for_adding[0]].arts_crafts += 1
            elif indice_for_adding[1] == 10:
                self.worker_list[indice_for_adding[0]].rune += 1
        return

    def _choose_from_indices(self, indices):
        candidate = []
        for idx in np.arange(0, indices[0].size):
            candidate.append(self._get_worker_param_by_indice((indices[0][idx], indices[1][idx])))
        
        if np.max(candidate) <= 0:
            return 
        else:        
            return (indices[0][np.argmax(candidate)], indices[1][np.argmax(candidate)])


    def _get_worker_param_by_indice(self, indice):
        worker = self.worker_list[indice[0]]
        return worker.get_remaining_skill_points()

        # if indice[1] == 0:
        #     return worker.textile
        # elif indice[1] == 1:
        #     return worker.armor
        # elif indice[1] == 2:
        #     return worker.metal
        # elif indice[1] == 3:
        #     return worker.weapon
        # elif indice[1] == 4:
        #     return worker.wood
        # elif indice[1] == 5:
        #     return worker.alchemy
        # elif indice[1] == 6:
        #     return worker.magic
        # elif indice[1] == 7:
        #     return worker.tinker
        # elif indice[1] == 8:
        #     return worker.jewel
        # elif indice[1] == 9:
        #     return worker.arts_crafts
        # elif indice[1] == 10:
        #     return worker.rune
        # else:
        #     return 
    
    def _get_next_indices_to_add(self, gradients):
        indice_for_adding = None
        while indice_for_adding is None and np.max(gradients) > 0:
            indices = np.where(gradients==gradients.max())
            #if indices[0].size > 1:
            indice_for_adding = self._choose_from_indices(indices)
            if indice_for_adding is None:
                for i in range(0, indices[0].size):
                    gradients[indices[0][i]][indices[1][i]] = 0
        return indice_for_adding

    def get_next_indices(self):
        gradients = self._getGradients()
        return self._get_next_indices_to_add(gradients)

    def run(self):
        gradients = self._getGradients()
        self._add_point_to_largest_gradient(gradients)

class Optimal_next_skill_point_calculator():
    def __init__(self, item, worker_name_level_list, list_worker_params):
        self.item = item
        self.list_workers = self._load_workers(worker_name_level_list, list_worker_params)
        
    def _load_workers(self, worker_name_level_list, list_worker_params):
        list_workers = []
        for idx, worker_name_level in enumerate(worker_name_level_list):
            worker_loader = WorkerLoader(worker_name_level[0], worker_name_level[1])
            worker = worker_loader.get_worker()
            worker.set_worker_params(list_worker_params[idx])
            list_workers.append(worker)
        return list_workers

    def run(self):
        time_craft = []
        points_left = []
        mastery_rate = []
        
        lggo = LargestGlobalGradientOptimizer(self.item, self.list_workers)
        next_indice = lggo.get_next_indices()

        return next_indice
        #return self.list_workers, time_craft, points_left, mastery_rate


class Optimial_craft_time_calculator():
    def __init__(self, item, worker_name_level_list, total_investigated_skill_points):
        self.item = item
        self.list_workers = self._load_workers(worker_name_level_list)
        self.total_investigated_skill_points = total_investigated_skill_points 
    
    def _load_workers(self, worker_name_level_list):
        list_workers = []
        for worker_name_level in worker_name_level_list:
            worker_loader = WorkerLoader(worker_name_level[0], worker_name_level[1])
            worker = worker_loader.get_worker()
            list_workers.append(worker)
        return list_workers

    def _get_mastery_rate(self, point):
        green_rate = 2.5+0.025*point
        blue_rate = 1 + 0.0125*point
        flawless_rate =  0.25 + 0.005*point
        epic_rate = 0.01 + 0.0005*point
        legendary_rate = 0.001 + 0.00005*point
        
        return (green_rate, 
                blue_rate,
                flawless_rate,
                epic_rate,
                legendary_rate)

    def run(self):
        time_craft = []
        points_left = []
        mastery_rate = []
        for i in range(0, self.total_investigated_skill_points): #50*12*8
            lggo = LargestGlobalGradientOptimizer(self.item, self.list_workers)
            lggo.run()
            self.list_workers = lggo.worker_list

            sum_w_param = Worker_params()
            for worker in self.list_workers:
                sum_w_param += worker.get_worker_params() 
            time_craft.append(self.item.getCraftTime(sum_w_param))
            total_mastery = 0
            for worker in self.list_workers:
                total_mastery += worker.get_available_mastery()
            mastery_rate.append(self._get_mastery_rate(total_mastery))

            ## old method:
            # current_worker = self.list_workers[i%len(self.list_workers)]
            # rest_worker_params = [w.get_worker_params() for idx,w in\
            #                          enumerate(self.list_workers) if idx != i%8]
        
            # sum_w_param = Worker_params()
            # for w_param in rest_worker_params:
            #     sum_w_param = sum_w_param + w_param
            # lgo = LargestGradientOptimizer(self.item, current_worker, sum_w_param)
            # lgo.run()

            # self.list_workers[i%8] = lgo.worker
            # time_craft.append(self.item.getCraftTime(sum_w_param+lgo.worker.get_worker_params()))

            # total_mastery = 0
            # for worker in self.list_workers:
            #     total_mastery += worker.get_available_mastery()
            # mastery_rate.append(self._get_mastery_rate(total_mastery))

        
        return self.list_workers, time_craft, points_left, mastery_rate


if __name__ == "__main__":
    from Worker_params import Worker_params
    from Worker import Worker, WorkerLoader
    from Item import Item, ItemLoader
    
    il = ItemLoader("gfg")
    item = il.get_item()

    worker_name_level_list = [("master",35),
                              ("seamstress",37),
                              ("sculptor",39),
                              ("artisan",39),
                              ("wizard",38),
                              ("alchemist",36),
                              ("the-giant",36),
                              ("luthier",31)]

    
    
    octc = Optimial_craft_time_calculator(item, worker_name_level_list, 1000)
    list_workers, time_craft, points_left, mastery_rate = octc.run()

    import matplotlib.pyplot as plt
    
    fig, ax1 = plt.subplots()
    ax1.plot(time_craft, color = "r")
    ax2 = ax1.twinx()
    ax2.plot(np.array(mastery_rate)[:,0], color = "g", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,1], color = "b", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,2], color = "c", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,3], color = "purple", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,4], color = "orange", linestyle = "--")
    #plt.plot(points_left)
    ax1.set_xlabel("Points added")
    ax1.set_ylabel("Craft time [min]")
    ax2.set_ylabel("Percentage [%]")
    plt.grid()
    plt.show()
    


    # skillRandom = SkillRandom(item, list_workers, 10000)
    # skillRandom.run()

    #skill_opt = SkillOptimizer(item, list_workers)
    #skill_opt.optimize()