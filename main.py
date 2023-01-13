import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplot() 

ax.plot([1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]);

plt.savefig("my_graph.png")