#!/usr/bin/env python
# coding: utf-8

# In[36]:


porcentaje = float(input("Introduce el porcentaje del alumno: "))
if porcentaje > 90:
    grado = 'A'
    print(f"El grado del alumno es: {grado}")
elif porcentaje > 80 and porcentaje <= 90:
    grado = 'B'
    print(f"El grado del alumno es: {grado}")
elif porcentaje >= 60 and porcentaje <= 80:
    grado = 'C'
    print(f"El grado del alumno es: {grado}")
else:
    grado = 'D'
    print(f"El grado del alumno es: {grado}")


# In[9]:


precio_bicicleta = float(input("Introduce el precio de la bicicleta "))
if precio_bicicleta > 100000:
    impuesto = precio_bicicleta * 0.15
    print(f"El impuesto a pagar por la bicicleta es: {impuesto}")
elif precio_bicicleta > 50000 and precio_bicicleta <= 100000:
    impuesto = precio_bicicleta * 0.10
    print(f"El impuesto a pagar por la bicicleta es: {impuesto}")
else:
    impuesto = precio_bicicleta * 0.05
    print(f"El impuesto a pagar por la bicicleta es: {impuesto}")


# In[5]:


año = float(input("Inserta el año que deseas consultar si es biciesto "))
if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
    print(f"El año {año} es biciesto.")
else:
    print(f"El año {año} no es biciesto. ")


# In[15]:


numero = int(input("Ingresa un número del 1 al 7: "))
dias = "Domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "Sabado"
if 1 <= numero <= 7:
    print(f"El día {numero} es {dias[numero]}")
else:
    print("Número fuera de rango. Ingresa un número entre 1 y 7.")


# In[27]:


numero = int(input("Ingresa un número del 1 al 12: "))
meses = ("Enero", 31),("Febrero", 28),("Marzo", 31),("Abril", 30),("Mayo", 31),("Junio", 30),("Julio", 31),("Agosto", 31),("Septiembre", 30),("Octubre", 31),("Noviembre", 30),("Diciembre", 31)
if 1 <= numero <= 12:
    mes, dias = meses[numero]
    print(f"{mes} tiene {dias} días")
else:
    print("Número fuera de rango. Ingresa un número entre 1 y 12.")


# In[ ]:




