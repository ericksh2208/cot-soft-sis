#Matería:CodSofSisln.
#Fecha:19/02/25|Grupo 2° "J".
#Alumno:Erick Otoniel Soto Hdez.
#Nombre de la practica:Tuplas.


#!/usr/bin/env python
# coding: utf-8

# In[19]:


tupla_1 = (1,2,3,4,5)
print(tupla_1)


# In[17]:


tupla_2 = (6,7,8,9,10)
print(tupla_2[2])


# In[1]:


tupla_1 = (1,2,3,4,5)
tupla_2 = (6,7,8,9,10)
tupla_nueva= tupla_1 + tupla_2
print(tupla_nueva)


# In[5]:


tupla = ('a','b','c')
print(tupla[0],tupla[1],tupla[2])


# In[17]:


tupla = (1,2,3,4,5)
print(2 in tupla)


# In[27]:


tupla = (0,1,2,3,4,5)
print(tupla[2:4])


# In[29]:


tupla =  (10,20,30,40,50)
print(len(tupla))


# In[31]:


tupla = (1,2,3,4,5)
tupla_repetida=tupla*3
print(tupla_repetida)


# In[33]:


lista = [1,2,3,]
tupla =tuple(lista)
print(tupla)


# In[39]:


tupla = (5,12,3,8,15)
print(min(tupla))
print(max(tupla))

