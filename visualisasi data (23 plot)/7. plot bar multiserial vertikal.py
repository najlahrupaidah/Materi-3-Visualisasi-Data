import numpy as np 
import matplotlib.pyplot as plt 
 
index = np.arange(5) 
values1 = [1,7,5,4,9] 
values2 = [3,5,4,5,5] 
values3 = [2,6,3,6,8] 
bw = 0.3 
plt.axis([0,5,0,8]) 
plt.title('Diagram Batang Multiserial',fontsize=20) 
plt.bar(index,values1,bw,color='b') 
plt.bar(index+bw,values2,bw,color='g') 
plt.bar(index+2*bw,values3,bw,color='y') 
plt.xticks(index+1.5*bw,['A','B','C','D','E']) 
plt.show() 
