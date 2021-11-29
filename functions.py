# write all the helper functions here
import numpy as np

def test_helper():
    print("helper function is working")
    
def T_matrix(theta):
    theta =  np.deg2rad(theta)
    c = np.cos(theta)
    s = np.sin(theta)
    
    T = np.array([
    [c**2 ,s**2 , 2*c*s],
    [s**2 ,c**2 , -2*c*s],
    [-s*c ,c*s , c**2 - s**2]    
    ])
    
    return T

def Q_matrix(E_L,E_T,G_LT,V_LT):
    
    V_TL = E_T * V_LT / E_L
    
    Q_11 = E_L/(1-V_TL * V_LT)
    Q_22 = E_T/(1-V_TL * V_LT)
    Q_12 = (V_LT * E_T)/(1-V_TL * V_LT)
    Q_66 = G_LT
    
    Q = np.array([
        [Q_11,Q_12,0],
        [Q_12,Q_22,0],
        [0,0,Q_66]
    ])
    
    return Q

def S_matrix(E_L,E_T,G_LT,V_LT):
    
    Q = Q_matrix(E_L,E_T,G_LT,V_LT)
    
    S = np.linalg.inv(Q)
    
    return S

R_MATRIX = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,2]
])

def Q_bar_matrix(Q,T):
    
    R = R_MATRIX
    T_inv = np.linalg.inv(T)
    R_inv = np.linalg.inv(R)
    
    Q_bar = np.linalg.multi_dot(
        (T_inv,Q,R,T,R_inv)
    )
    
    return Q_bar

def S_bar_matrix(Q,T):
    
    Q_bar = Q_bar_matrix(Q,T)
    
    S_bar = np.linalg.inv(Q_bar)
    
    return S_bar


## laminate functions...

def laminate_matrices(n_lamina,h_k,theta_k,Q):
    """
    n_lamina: number of lamina
    
    h_k: z_coordinate list of the lamina.. 
        used in A,B,C,D calc..
        ie. A = sum(Qbar * (h_k - h_k-1))
        h_k will go from top to bottom
        
    theta_k: angle of lamina
    
    Q = Q matrix for the lamina, if all ply are same material..
        provide list of Q matrices of size n_lamina if not.
    
    """
    ### make A,B,C,D numpy matrix filled with zeroes of size 3*3
    A = np.zeros((3,3))
    B = np.zeros((3,3))
    D = np.zeros((3,3))
    
    ## make a list of Q_matrices
    
    if len(Q) == 1:
        Q_matrices = Q * n_lamina
    elif len(Q) == n_lamina:
        Q_matrices = Q
    else:
        raise ValueError("Q matrix list is not of size n_lamina")
    
    for i in range(n_lamina):
        
        T = T_matrix(theta_k[i])
        Q_bar = Q_bar_matrix(Q_matrices[i], T)
        
        diffh_k = h_k[i+1] - h_k[i]
        square_diffh_k = h_k[i+1]**2 - h_k[i]**2
        cube_diffh_k = h_k[i+1]**3 - h_k[i]**3
        
        A = A + Q_bar * diffh_k
        B = B + Q_bar * square_diffh_k
        D = D + Q_bar * cube_diffh_k
        
    B = B/2
    D = D/3
    
    return A,B,D


        
    
        
        
        
        
        
        
        
    

    
