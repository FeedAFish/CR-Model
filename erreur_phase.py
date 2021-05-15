# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:09:02 2021

@author: KIET
"""

import numpy as np
import matplotlib.pyplot as plt
def Erreur_1(a,xi):
    res = a*xi-np.arccos((1-a*(1-np.cos(xi)))/(np.sqrt(1-2*a*(1-a)*(1-np.cos(xi)))))
    return res
def Erreur_2(a,xi):
    res = a*xi-np.arccos((1-a**2*(1-np.cos(xi)))/(np.sqrt(1-a**2*(1-a**2)*((1-np.cos(xi))**2))))
    return res
def Erreur_3(a,xi):
    res = a*xi-np.arccos((1-2*a*(np.sin(xi/2)**2)*(1-(1-a)*(np.cos(xi/2)**2)))/(np.sqrt((1-2*a*(np.sin(xi/2)**2)*(1-(1-a)*(np.cos(xi/2)**2)))**2+4*a**2*(np.sin(xi/2)**2)*(np.cos(xi/2)**2)*(1+(1-a)*(np.sin(xi/2)**2))**2)))
    return res

Xi = np.linspace(0,np.pi/8,201)
U11 = Erreur_1(0.8, Xi)
U12 = Erreur_1(0.5, Xi)
U13 = Erreur_1(0.2, Xi)
U21 = Erreur_2(0.8, Xi)
U22 = Erreur_2(0.5, Xi)
U23 = Erreur_2(0.2, Xi)
U31 = Erreur_3(0.8, Xi)
U32 = Erreur_3(0.5, Xi)
U33 = Erreur_3(0.2, Xi)

fig=plt.figure(1)
plt.title("Erreur de phase avec alpha=0.8")
plt.plot(Xi,U11,'-g',Xi,U21,'-b',Xi,U31,'-r')
plt.legend(['sch1','sch2','sch3'],loc='best')
plt.grid(True)     
plt.show(block=False)
plt.close('all')
fig=plt.figure(2)
plt.title("Erreur de phase avec alpha=0.5")
plt.plot(Xi,U12,'-g',Xi,U22,'-b',Xi,U32,'-r')
plt.legend(['sch1','sch2','sch3'],loc='best')
plt.grid(True)     
plt.show(block=False)
plt.close('all')
fig=plt.figure(3)
plt.title("Erreur de phase avec alpha=0.2")
plt.plot(Xi,U13,'-g',Xi,U23,'-b',Xi,U33,'-r')
plt.legend(['sch1','sch2','sch3'],loc='best')
plt.grid(True)     
plt.show(block=False)
plt.close('all')