import numpy as np 
import matplotlib.pyplot as plt 
labels = ['Lain-lain','jempol','telunjuk','tengah','manis','kelingking'] 
values = [42,21,14,9,8,7] 
colors = ['purple','green','pink','blue','yellow','orange'] 
explode = [0,1,0,0,0,0] #fokus pada jempol 
plt.title('Diagram Pie Market Share jempol') 
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180) 
plt.axis('equal') 
plt.show()
