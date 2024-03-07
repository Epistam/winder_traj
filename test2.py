import matplotlib.pyplot as plt
import numpy as np

global C, L, R # Fairing parameters
global ref_speed, x_speed, top_margin, bot_margin, step # Winding parameters

# Paramètres coiffe
C = .66 # paramètre de von Karman 
L = 500. # longueur en mm
R = 80. # rayon en mm

ref_speed = 500 # vitesse linéaire tangentielle de référence (mm/s) => v_cst = ref_speed = omega*r => omega = ref_speed / r 
top_margin = 50. # longueur en mm du cylindre devant coiffe (petit diam.)
bot_margin = 50. # longueur en mm du cylindre derrière coiffe (gros diam.)
step = .5 # in mm
x_speed = 30 # in mm/s aka x(t)

# Von Haack function
def von_haack(z) :
    
    rs = 3.14024202

    return rs

def test(z) :
    z_conditions = [z < top_margin, (top_margin < z) & (z < bot_margin), z >= L+top_margin]
    #z_func = [von_haack(top_margin), von_haack(z), von_haack(top_margin+L)]
    z_func = [von_haack(z), 42, 69]
    print('piecewise returned VH :' , np.piecewise(z, z_conditions, z_func))

print('actual VH : ', von_haack(3))
test(3.)
