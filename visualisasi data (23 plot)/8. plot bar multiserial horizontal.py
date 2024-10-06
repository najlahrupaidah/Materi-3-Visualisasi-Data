import numpy as np 
import matplotlib.pyplot as plt 
 
index = np.arange(5) 
values1 = [1,7,5,4,6] 
values2 = [3,5,4,5,5] 
values3 = [2,4,3,1,6] 
bw = 0.3 
plt.axis([0,10,0,5]) 
plt.title('Diagram Batang Multiserial',fontsize=20) 
plt.barh(index,values1,bw,color='b') 
plt.barh(index+bw,values2,bw,color='g') 
plt.barh(index+2*bw,values3,bw,color='y') 
plt.yticks(index+1.5*bw,['A','B','C','D','E']) 
plt.show()
plt.show()
