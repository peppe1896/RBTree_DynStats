import numpy as np
import random
from timeit import default_timer as timer


def create_rand_array(size, low_bound=0, upp_bound=10000):
    r = np.zeros(size, dtype=int)
    start = timer()
    for i in range(size):
        r[i] = random.randint(low_bound, upp_bound)
    end = timer()
    print("Temp creazione array (random):", (end-start), "secondi")
    return r
