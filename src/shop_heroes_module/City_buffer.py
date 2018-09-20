import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from shop_heroes_module.Worker_params import Worker_params

class City_buffer(Worker_params):
    def __init__(self, *args):
        Worker_params.__init__(self, *args)

if __name__ == "__main__":
    wp = Worker_params()
    print (wp)