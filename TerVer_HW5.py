#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from scipy import stats

#z критерий для задачи 2
alpha = 0.05
t1=stats.norm.ppf(alpha)
t1


# In[10]:


#задача 4: нулевая гипотеза M_mothers = M-daughters; альтернативная M_mothers =! M_daughters
mothers = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
daughters = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
mothers, daughters


# In[14]:


#среднее в выборке матарей
m_mean=np.mean(mothers)
m_mean


# In[15]:


#среднее в выборке дочерей
d_mean=np.mean(daughters)
d_mean


# In[16]:


#найдем несмещенную дисперсию в выборках
d_var=np.var(daughters, ddof=1)
m_var=np.var(mothers, ddof=1)
m_var, d_var


# In[17]:


#найдем СКО
d_std=np.std(daughters)
m_std=np.std(mothers)
m_std, d_std


# In[18]:


#найдем кол-во элементов в выборке
m_len=len(mothers)
d_len=len(daughters)
m_len, d_len


# In[19]:


#найдем наблюдаемое значение
t_emp=(m_mean - d_mean)/np.sqrt(m_var/m_len + d_var/d_len)
t_emp


# In[20]:


#найдем критические значения по статистике стьюдента для двусторонней критической области (тк нет уверенности, что она односторонняя)
alpha=0.05
t1=stats.t.ppf(alpha/2, df=2*(m_len-1))
t2=stats.t.ppf(1-alpha/2, df=2*(m_len-1))
t1, t2


# In[22]:


#Вывод: нулеая гипотеза не отвергается, проверим тестом : p_value >альфа - H0 не отвергается
#t1<t_emp<t2
stats.ttest_ind(mothers, daughters)


# In[ ]:




