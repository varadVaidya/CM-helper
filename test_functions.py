from functions import *

# # ## T matrix    
# # T = T_matrix(60)
# # print(T)

# # ## Q_Matrix

# Q = Q_matrix(148,10.5,5.61,0.3)
# print("Q_matirx: \n",Q,"\n")

# ## S_matrix

# # S = S_matrix(148,10.5,5.61,0.3)
# # print(S)


# # ## Q_Bar_test
# # T = T_matrix(30)
# # print("T_matrix \n",T,"\n")

# # Q_bar = Q_bar_matrix(Q, T)
# # print("Q_bar_matrix \n",Q_bar,"\n")



# ## S_Bar_test
# T = T_matrix(30)
# print("T_matrix \n",T,"\n")

# S_bar = S_bar_matrix(Q, T)
# print("S_bar_matrix \n",S_bar,"\n")




## laminate matrices test..

# theta_k = [45 , 0]
# h_k = [-4,-1,4]
# n_lamina = 2

# Q = [np.array([
#     [20,0.7,0],
#     [0.7,2,0],
#     [0,0,0.7]
# ])]

# A,B,D = laminate_matrices(n_lamina, h_k= h_k, theta_k= theta_k, Q= Q)
# print("A : \n",A,"\n")
# print("B : \n",B,"\n")
# print("D : \n",D,"\n")

# # different example
# theta_k = [45,0,45]
# h_k = [-6,-3,3,6]
# n_lamina = 3

# Q = np.array([
#     [20,0.7,0],
#     [0.7,2,0],
#     [0,0,0.7]
# ])
# Q = [Q]

# A,B,D = laminate_matrices(n_lamina, h_k= h_k, theta_k= theta_k, Q= Q)
# print("A : \n",A,"\n")
# print("B : \n",B,"\n")
# print("D : \n",D,"\n")

## isotropic test
A = np.array([[9.1425,3.0475,0],[3.0475,9.1425,0],[0,0,3.0475]])
E_R,G_R,V_R = quasi_isotropic_constants(A,1)

print("E_R : \n",E_R,"\n")
print("G_R : \n",G_R,"\n")
print("V_R : \n",V_R,"\n")


