# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:49:34 2024

@author: Aniruddha
"""

import numpy as np
import pandas as pd
from scipy.integrate import simpson

omega_matter0 = 0.270
omega_lambda0 = 0.729
omega_radiation0 = 8.24e-5
omega_curvature0 = 1 - omega_matter0 - omega_radiation0 - omega_lambda0 

h0 = 0.70
H0 = 100*h0 *(1e3 /3.086e22) # km . s^-1 . Mpc^-1 converted to SI unit
c = 3e8 # m . s^-1

z_max_array=np.linspace(1e-2, 1e2, 10**4)
D_c = []
D_l = []
D_a = []
D_p = []

for z_max in z_max_array:
    z = np.linspace(0, z_max, 10**6)

    def H(x):
        # x denotes redshift
        Hubble = H0 * np.sqrt( (1+x)**3 * omega_matter0 + (1+x)**4 * omega_radiation0 
                              + (1+x)**2 * omega_curvature0 + omega_lambda0 )
        return Hubble

    H_z = H(z)

    d_c = c * simpson(1/H_z, z)
    #print(d_c/3.086e22, "Mpc")

    d_l = (1+z_max) * d_c
    #print(d_l/3.086e22, "Mpc")

    d_a = d_c / (1+ z_max)
    #print(d_a/3.086e22, "Mpc")

    d_p = c * simpson(1/(H_z*(1+z)), z)
    #print(d_p/3.086e22, "Mpc")
    
    D_c.append(d_c)
    D_l.append(d_l)
    D_a.append(d_a)
    D_p.append(d_p)
    print(z_max)
    
D_c = np.array(D_c)
D_l = np.array(D_l)
D_a = np.array(D_a)
D_p = np.array(D_p)

df = pd.DataFrame({"Redshift" : z_max_array, "Comoving distance" : D_c, "Luminosity distance" : D_l, "Angular-diameter distance" : D_a, "Proper distance" : D_p})
df.to_csv("cosmo_distance_in_Mpc_unit.csv", index=False)
