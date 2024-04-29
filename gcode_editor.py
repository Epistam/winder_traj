import cfg
import numpy as np

# Home all axes

# write coordinates arrays

def gcode_write_traj(Ltheta, Lz, Lr, Lomega) :
	assert len(Ltheta) == len(Lz) == len(Lr) == len(Lomega) , 'Bad coordinate list size'

	# creating Vz
	L_Vz = [s for s in [cfg.carriage_speed]*len(Lomega)]

	# scaling Lomega and converting to deg/s
	Lomega = [np.rad2deg(omega)*cfg.carriage_speed for omega in Lomega]

	#print(f'Z motion for a whole spin : {(360/Lomega[0])*cfg.carriage_speed}')

	with open(cfg.output_file, 'a') as f: 
		for (theta, Z, R, omega, Vz) in zip(Ltheta, Lz, Lr, Lomega, L_Vz) :
			f.write((f"G1 {cfg.gcode_axis_theta}{np.rad2deg(theta)} "
				f"{cfg.gcode_axis_Z}{Z} "
				f"{cfg.gcode_speed_omega}{omega} "
				f"{cfg.gcode_speed_carriage}{Vz}\n"))
	
def gcode_write_comment(comment) :
	with open(cfg.output_file, 'a') as f: 
		f.write(f';{comment}\n')

def gcode_clear() :
	with open(cfg.output_file, 'w') as f :

		cfg_vars = [item for item in dir(cfg) if not item.startswith("__")]

		for var in cfg_vars :
			f.write(f'; {var} = {getattr(cfg, var)} ')
		
		f.write(f';{cfg.gcode_axis_theta} (spindle angle) | {cfg.gcode_axis_Z} (carriage longitudinal position) | {cfg.gcode_axis_R} (carriage radial position) \n')
			

# write single array
