import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shop_heroes_module.Worker_params import Worker_params
from shop_heroes_module.Worker import Worker, WorkerLoader
from shop_heroes_module.Item import Item, ItemLoader
from shop_heroes_module.Math import Optimial_craft_time_calculator
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #Parameters
    item_name = "GuZheng"  
    worker_name_level_list = [("master",35),
                              ("seamstress",37),
                              ("sculptor",39),
                              ("artisan",39),
                              ("wizard",38),
                              ("alchemist",36),
                              ("the-giant",36),
                              ("luthier",31)]


    
    il = ItemLoader(item_name)
    item = il.get_item()
    octc = Optimial_craft_time_calculator(item, worker_name_level_list)
    list_workers, time_craft, points_left, mastery_rate = octc.run()
    worker_params = Worker_params()
    for idx, worker in enumerate(list_workers):
        worker_params += worker.get_worker_params()
        print (worker_name_level_list[idx][0])
        print (worker.get_worker_params())
        print ("\n")
    print (worker_params)
    print (item.getCraftTime(worker_params))
    #start plot
    fig, ax1 = plt.subplots()
    ax1.plot(time_craft, color = "r")
    ax2 = ax1.twinx()
    ax2.plot(np.array(mastery_rate)[:,0], color = "g", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,1], color = "b", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,2], color = "c", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,3], color = "purple", linestyle = "--")
    ax2.plot(np.array(mastery_rate)[:,4], color = "orange", linestyle = "--")

    ax1.set_xlabel("Points added")
    ax1.set_ylabel("Craft time [min]")
    ax2.set_ylabel("Percentage [%]")
    plt.grid()
    plt.show()
    