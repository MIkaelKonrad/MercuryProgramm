
def scalar_prod(v_1,v_2):
    sol = v_1[0]*v_2[0] + v_1[1]*v_2[1]
    return sol

def Gram_Schmitt(v):
    v_1 = [v[0], v[1] ]
    v_2 = [v[2], v[3] ]
    print(len(v_1))
    print(len(v_2))
    coeff = scalar_prod(v_1,v_2) / scalar_prod(v_1,v_1)
    print(coeff)
    u=[0,0]
    for i in [0,1]:
        u[i] = v_2[i]- coeff*v_1[i]
    return u