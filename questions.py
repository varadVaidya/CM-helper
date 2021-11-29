from functions import *

## given stress in global axes, find stress in local axes, find strains as well..
## given values:
theta = 60
sigma = [2,-3,4] ## MPa

sigma = np.array(sigma)
T = T_matrix(60)
E_L,E_T,G_LT,V_LT = 181,10.3,7.17,0.28  # GPa

Q = Q_matrix(E_L, E_T, G_LT, V_LT)
Qbar = Q_bar_matrix(Q, T) *1e3 ## GPa to MPa
strain_global = np.linalg.inv(Qbar).dot(sigma)

strain_local = np.linalg.multi_dot(
    (R_MATRIX,T,np.linalg.inv(R_MATRIX),strain_global))
stress_local = T.dot(sigma)
print("Qbar: \n", Qbar, "\n")
print("strain_global: \n", strain_global, "\n")
print("strain_local: \n", strain_local, "\n")
print("stress_local: \n", stress_local, "\n") # MPa
