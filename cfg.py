import numpy as np

# Tube / fairing parameters
######################
# Mandrel settings
L = 2000. # longueur en mm
R = 80. # rayon en mm
# Fairing settings (if applicable)
C = .66 # paramètre de von Karman 

top_margin = 0. # useless for cylinders
bot_margin = 0. # distance from Z origin
cyl_Z_offset = 100.

# Fiber orientation
####################
# Orientation setting
#orient = 45 # fiber orientation in degrees
# OR step setting
filament_step = 503 # in mm
orient = np.rad2deg(np.deg2rad(90)-np.arctan((2*np.pi*R)/filament_step))

# Speeds / feeds
################
carriage_speed = 10 # carriage speed acts a speed multiplicator applied to both omega and Vz, not changing their ratio
om_func = lambda r : Vtan/r
Vtan = np.tan(np.deg2rad(90-orient)) # Vtan(z) ; implicitely, Vz = 1mm/s

# personal gibberish, keeping it just in case
# arbitrary_tan_speed_cst : vitesse linéaire tangentielle de référence (mm/s) 
# => v_cst = arbitrary_tan_speed_cst = omega*r => omega = arbitrary_tan_speed_cst / r
# fonction omega : donne la vitesse angulaire du tube
#om_func = lambda r : arbitrary_tan_speed_cst/(r/r)
#arbitrary_tan_speed_cst = .06
#om_func = lambda r : Vtan/r
#Vtan = np.tan(np.deg2rad(90-orient)) # Vtan(z) ; implicitely, Vz = 1mm/s
#om_func = lambda r : arbitrary_tan_speed_cst/(r*r)
#arbitrary_tan_speed_cst = 30

# Winding parameters
#####################
halfpass_shift = 180 # shift (deg) between halfpass FWD and halfpass BWD
pass_shift = 45 # shift en degrès à la fin de chaque passe
pass_count = 1 # number of passes to do. For optimal hoop results, use pass_count = int(360/pass_shift).
#pass_count = int(360/pass_shift) #automated calculation for rendering all passes

# Point density
################
step = 20 # Z step between points in mm

# Gcode generation
###################
output_file = 'test.gcode'
gcode_axis_theta = 'A'
gcode_axis_Z = 'B'
gcode_axis_R = 'C'
gcode_speed_omega = 'E'
gcode_speed_carriage = 'F'

# Misc / irrelevant
#######
plot_mode = '3d'
spindle_speed = np.rad2deg(((carriage_speed*np.tan(np.deg2rad(90-orient)))/R))# in deg/s
# LEGACY
# use THIS for fairing
#top_margin = 30. # longueur en mm du cylindre devant coiffe (petit diam.)
#bot_margin = 80. # longueur en mm du cylindre derrière coiffe (gros diam.)
#step_count = 
