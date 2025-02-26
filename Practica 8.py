#Practica 8
#Erick Otoniel Soto Hdez
#25/02/25
#2do "J"


#!/usr/bin/env python
# coding: utf-8

# In[9]:


monumentos={
    "Delhi":"Red fort",
    "Paris":"Torre Eifel",
    "Nueva york":"Estatua de la libertad",
    "Rio de janeiro":"Cristo redentor"
    
}
ciudad=input("Ingresa el nombre de la ciudad")
print("El monumento es ", monumentos[ciudad]) 


# In[13]:


edad = float(input("Ingresa la edad que deseas saber si es posible votar"))
if edad >= 18:
    print("es posible votar")
else:
    print("Eres menor de edad, no puedes votar")
  
    


# In[9]:


numero1=input("Ingresa el primer numero")
numero2=input("Ingresa el segundo numero")
if numero1>numero2:
    print(numero1," es mayor que ",numero2)
elif numero2>numero1:
    print(numero2," es mayor que ",numero1) 


# In[15]:


edades=[]
edad1=int(input("Ingresa tu edad"))
edades.append(edad1)
edad2=int(input("Ingresa tu edad"))
edades.append(edad2)
edad3=int(input("Ingresa tu edad"))
edades.append(edad3)
edad4=int(input("Ingresa tu edad"))
edades.append(edad4)
print("La edad menor es ",min(edades))



# In[19]:


minus="qwertyuiopñlkjhgfdsazxcvbnm"
mayus="QWERTYUIOPÑLKJHGFDSAZXCVBNM"
palabra=input("Ingresa tu palabra")
letras=list(palabra)
for letra in letras:
    if letra in minus:
        print("Letra minuscula ",letra)
    elif letra in mayus:
        print("Letra mayuscula ",letra)
    else:
        print("Es un simbolo o numero ",letra)

