#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Materia:
    __calificacion=""
    def evaluar(self):
        print("evaluando a los alumnos")

class Matematicas(Materia):
    __calificacion=""
    def evaluar(self):
        print("realisando operaciones")

class codificacion(Materia):
    __calificacion=""
    def evaluar(self):
        print("evaluando a los alumnos")

unamateria=Materia()
unamateria.evaluar()

unamateria=Matematicas()
unamateria.evaluar()

unamateria=codificacion()
unamateria.evaluar()


# In[ ]:




