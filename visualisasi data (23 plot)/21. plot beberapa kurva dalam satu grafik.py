import matplotlib.pyplot as plt 
import math 
import numpy as np 
t = np.arange(0,5,0.01) 
y1 = np.sin(math.pi*t) 
y2 = np.sin(math.pi*t+math.pi/2) 
y3 = np.sin(math.pi*t-math.pi/2) 
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'y-.') 
plt.show()
