import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() 

ax.plot([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])

plt.savefig("MyGraph.png")