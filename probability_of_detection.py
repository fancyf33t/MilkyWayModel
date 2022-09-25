#create a model of milkyway 
from random import randint #library for random choice
from collections import Counter 
import numpy as np 
import matplotlib.pyplot as plt 

NUM_EQUIV_VOLUMES = 1000 #number of locations to place civs
MAX_CIVS = 5000 #maximum number of advanced civs
TRIALS = 1000 #number of times to model a given number of civs
CIV_STEP_SIZE = 100 #civilizations count step

x = [] # x values for polynomial fit
y = [] #y values for polynomial fit

# make a for loop
for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = []
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))
    # print ratio of civs-per-volume vs probability of 2+ civs per location
    print("{:.4f} {:.4f}".format(civs_per_vol, prob))
    x.append(civs_per_vol)
    y.append(prob)

# part2
coefficients = np.polyfit(x, y, 4) #4th order polynomial fit
p = np.poly1d(coefficients)
print('\n{}'.format(p))
xp = np.linspace(0,5)
_ = plt.plot(x, y, '.', xp, p(xp), '-')
plt.ylim(-0.5, 1.5)
plt.show()