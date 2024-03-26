# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:12:34 2024

@author: Aniruddha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_csv(r"C:\Users\Aniruddha\Downloads\cosmo_distance_SI_unit.csv", skiprows=1)

z= df.iloc[:,0]
d_c= df.iloc[:,1]
d_l= df.iloc[:,2]
d_a= df.iloc[:,3]
d_p= df.iloc[:,4]

print("----- Welcome to the redshift to distance converter and vice versa ----- \n")

det= input("\n For more info about the cosmology model in use type: info \n enter here: ")
if det=='info':
    print("\n We use omega_matter0 = 0.270 \n omega_lambda0 = 0.729 \n omega_radiation0 = 8.24e-5 \n omega_curvature0 = 0 in flat lambda-CDM cosmology with h0 = 0.70 and H0 = 100*h0 \n km . s^-1 . Mpc^-1 and c = 3e5 # km . s^-1 \n")

time.sleep(3)
s1= input("\n Redshift to distance, type: ztod \n Distance to redshift, type: dtoz \n Please enter here: ")

if s1=="ztod":
    print("\n Redshift to distance converter: on \n")
    time.sleep(1)
    s2= input("\n Comoving distance: c \n Luminosity distance: l \n Angular-diameter distance: a \n Proper distance: p \n Please enter here: ")
    if s2=="c":
        print("\n Redshift to comoving distance calculator: on \n")
        z_input= input("\n Enter redshift: ")
        d=np.interp(z_input, z, d_c)
        print("\n The comoving distance for z=", z_input, " is ", d , " Mpc")
    if s2=="l":
        print("\n Redshift to luminosity distance calculator: on \n")
        z_input= input("\n Enter redshift: ")
        d=np.interp(z_input, z, d_l)
        print("\n The luminosity distance for z=", z_input, " is ", d , " Mpc")
    if s2=="a":
        print("\n Redshift to angular-diameter distance calculator: on \n")
        z_input= input("\n Enter redshift: ")
        d=np.interp(z_input, z, d_a)
        print("\n The angular diameter distance for z=", z_input, " is ", d , " Mpc")
    if s2=="p":
        print("\n Redshift to proper distance calculator: on \n")
        z_input= input("\n Enter redshift: ")
        d=np.interp(z_input, z, d_p)
        print("\n The proper distance for z=", z_input, " is ", d , " Mpc")

if s1=="dtoz":
    print("\n Distance to redshift converter: on \n")
    time.sleep(1)
    s2= input("\n Comoving distance: c \n Luminosity distance: l \n Angular-diameter distance: a \n Proper distance: p \n Please enter here: ")
    if s2=="c":
        print("\n Comoving distance to redshift calculator: on \n")
        d_input= input("\n Enter the comoving distance in Mpc: ")
        redshift = np.interp(d_input, d_c, z)
        print("\n The redshift corresponding to d_c =", d_input, "Mpc is z =", redshift )
    if s2=="l":
        print("\n Luminosity distance to redshift calculator: on \n")
        d_input= input("\n Enter the luminosity distance in Mpc: ")
        redshift = np.interp(d_input, d_l, z)
        print("\n The redshift corresponding to d_l =", d_input, "Mpc is z =", redshift )
    if s2=="a":
        print("\n Angular-diameter distance to redshift distance calculator: on \n")
        print("\n A bug in here, the function is multivalued, we recommend doing the vice versa for a nice picture! \n")
        d_input= input("\n Enter the angular-diameter distance in Mpc: ")
        redshift = np.interp(d_input, d_a, z)
        print("\n The redshift corresponding to d_a =", d_input, "Mpc is z =", redshift )
    if s2=="p":
        print("\n Proper distance to redshift calculator: on \n")
        d_input= input("\n Enter the proper distance in Mpc: ")
        redshift = np.interp(d_input, d_p, z)
        print("\n The redshift corresponding to d_p =", d_input, "Mpc is z =", redshift )



