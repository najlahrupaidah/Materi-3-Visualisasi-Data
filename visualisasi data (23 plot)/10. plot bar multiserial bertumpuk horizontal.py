import numpy as np 
import matplotlib.pyplot as plt 
 
series1 = np.array([3,4,5,6]) 
series2 = np.array([1,2,3,5]) 
series3 = np.array([2,3,5,4]) 
index = np.arange(4) 
plt.axis([0,15,-0.5,3.5]) 
plt.title('Diagram Batang Bertumpuk Multiserial') 
plt.barh(index,series1,color='y') 
plt.barh(index,series2,color='b',left=series1) 
plt.barh(index,series3,color='g',left=(series2+series1)) 
plt.yticks(index+0.4,['Jan21','Feb21','Mar21','Apr21']) 
plt.show()
