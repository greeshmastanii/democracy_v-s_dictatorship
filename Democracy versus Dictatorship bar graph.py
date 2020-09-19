#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
csv_data_file=pd.read_csv('/home/greesh/Documents/verdatumcode/Democracy-Dictatorship_Index.csv')
data=csv_data_file.set_index('Regime')['Type'].to_dict()  
democracy=[]
dictatorship=[]
count=0
for i in data.values():
    if i== 'Democracy':
        democracy.append(i)
    number_of_democracy=len(democracy)
    if i=='Dictatorship':
         dictatorship.append(i)
    number_of_dictatorship=len(dictatorship)
total_number=[]
total_number.append(number_of_democracy)
total_number.append(number_of_dictatorship)
plt.title('Democracy v/s Dictatorship in the world')
plt.xlabel('Type of government')
plt.ylabel('N.o of countries')
x = 1,2
plt.bar(1, height=total_number[0] ,color='yellow')
plt.bar(2, height=total_number[1], color='red')
plt.xticks(x, ['Democracy','Dictatorship'])
    


# In[ ]:





# In[ ]:




