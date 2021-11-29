from functions import *

# ## T matrix    
# T = T_matrix(60)
# print(T)

# ## Q_Matrix

Q = Q_matrix(148,10.5,5.61,0.3)
print("Q_matirx: \n",Q,"\n")

## S_matrix

# S = S_matrix(148,10.5,5.61,0.3)
# print(S)


# ## Q_Bar_test
# T = T_matrix(30)
# print("T_matrix \n",T,"\n")

# Q_bar = Q_bar_matrix(Q, T)
# print("Q_bar_matrix \n",Q_bar,"\n")



## S_Bar_test
T = T_matrix(30)
print("T_matrix \n",T,"\n")

S_bar = S_bar_matrix(Q, T)
print("S_bar_matrix \n",S_bar,"\n")