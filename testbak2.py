import numpy as np
import matplotlib.pyplot as plt

def von_haack(C, L, R, x) :
    
    theta = np.arccos(1-(2*x)/L)
    expr1 = R/np.sqrt(np.pi)
    expr2 = theta - (np.sin(2*theta)/2) + C*(np.sin(theta))**3

    rs = (expr1*np.sqrt(expr2))

    return rs

# Returns a list of equally spaced positions for the x axi
def get_Lx(ref_speed, top_margin, bot_margin, step, L) :

    Lx = np.concatenate((
        np.arange(1,top_margin,step), 
        np.arange(top_margin,L,step),
        np.arange(L,L+bot_margin,step),
        ))

    return Lx

# A list of angular speeds for the spindle (basicaly ω(x))
def get_Lspeed(Lx, C, L, R, top_margin, bot_margin) :
    Lspeed = np.array(
        [von_haack(C, L, R, top_margin)]*(top_margin-1) + 
        [von_haack(C, L, R, x) for x in Lx[top_margin-1:L]] +
        [von_haack(C, L, R, L)]*(bot_margin-1)
        )

    print(Lspeed)

    return Lspeed

C = .66
L = 500
R = 80

ref_speed = 10000 # vitesse linéaire tangentielle de référence => v_cst = ref_speed = omega*r => omega = ref_speed / r 
top_margin = 50 # longueur en mm du cylindre devant coiffe (petit diam.)
bot_margin = 50 # longueur en mm du cylindre derrière coiffe (gros diam.)
step = 1 # in mm

# TODO divide margins by step or something

Lx = get_Lx(ref_speed, top_margin, bot_margin, step, L)
Lspeed = get_Lspeed(Lx, C, L, R, top_margin, bot_margin)

plt.plot(Lx, Lspeed, label='C = '+str(C), color='blue')
plt.plot(Lx, ref_speed / Lspeed, label='C = '+str(C)+', ω(RPM)', color='blue')
plt.axvline(x=top_margin, color='red')
plt.axvline(x=L, color='red')
plt.grid()

plt.axis('equal')
plt.legend()
plt.show()
