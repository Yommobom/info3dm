import numpy as np
import matplotlib.pyplot as plt
from true_function import true_function

x = np.arange(-1,1,0.01)
y= true_function(x)

plt.plot(x,y,label="true function")
plt.legend()
plt.savefig("ex1.1.png")
plt.show()