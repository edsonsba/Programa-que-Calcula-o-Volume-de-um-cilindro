#!/usr/bin/env python
# coding: utf-8

# In[16]:


# In[24]:

# Trabalho do menoti - programa que calcula o volume do cilindro 09/07/2020

import numpy as np
Altura = 2 ## ALTURA DE LÍQUIDO (%)Informar ##
Comprimento = 6           # m
Diametro = 2.4            # m
Raio = 1.2                # m
MassEspecificaAgua = 1000 # kg/m³
AlturaM = (Altura * Diametro)/ 100
m2 = ((3.141592 * ((Raio**2)/2))+((Raio**2)* np.arcsin((AlturaM-Raio)/Raio))-((Raio-AlturaM)*((((Raio**2)-(Raio-AlturaM)**2)**0.5))))
m3 = ( m2 * Comprimento)
VolumeLitro = m3 * 1000
MassDagua = m3 * MassEspecificaAgua
print('#######  Dados de entrada do programa #### ')
print('COMPRIMENTO TOTAL: ',Comprimento,'m')
print('DIAMETRO:',Diametro,'m')
print('RAIO: ',Raio,'m')
print('MASSA ESPECÍFICA ÁGUA: ',MassEspecificaAgua,'kg/m³')
print('########################################### ')
print('#### resultados de saídas do programa ##### ')
print('ALTURA DE LÍQUIDO (%): ',Altura)
print('ALTURA (m): ', AlturaM)
print('ÁREA LATERAL DE LÍQUIDO (m²): ',m2)
print('VOLUME DE LÍQUIDO (m³): ',m3)
print('VOLUME (LITROS):',VolumeLitro)
print('MASSA DE ÁGUA : ', MassDagua)









# In[ ]:




