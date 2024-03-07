# Fairing parameters
######################
C = .66 # paramètre de von Karman 
L = 500. # longueur en mm
R = 80. # rayon en mm

# Angular speed
################

# arbitrary_tan_speed_cst : vitesse linéaire tangentielle de référence (mm/s) 
# => v_cst = arbitrary_tan_speed_cst = omega*r => omega = arbitrary_tan_speed_cst / r

om_func = lambda r : arbitrary_tan_speed_cst/(r/r)
arbitrary_tan_speed_cst = .06
#om_func = lambda r : arbitrary_tan_speed_cst/r
#arbitrary_tan_speed_cst = 1 
#om_func = lambda r : arbitrary_tan_speed_cst/(r*r)
#arbitrary_tan_speed_cst = 30

top_margin = 30. # longueur en mm du cylindre devant coiffe (petit diam.)
bot_margin = 80. # longueur en mm du cylindre derrière coiffe (gros diam.)
step = 1 # in mm
#step_count = 

# x_speed = 30 # in mm/s aka x(t) (useless smh?)

# Plotting
############

plot_mode = '3d'
