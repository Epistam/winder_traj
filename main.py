#####################
# General notations #
#####################

''' Reference frame
z (mm) : distance from home on main carriage sliding axis
r(z) (mm) : radius of the fairing for a given z
omega(z) : calculated angular speed of the fairing for a given z, 
           such that tangential linear speed remains the same all along the fairing
c(z) (deg) : fairing angle at a given z
'''

# Imports
##########

import cfg
import plotting
import curve_generation

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

# Global vars
##############

global current_theta
current_theta = 0

# Returns a list of equally spaced positions for the x axis (values are in mm)
def get_Lz() :

    Lz = np.concatenate((
        np.arange(1, cfg.top_margin, cfg.step), 
        np.arange(cfg.top_margin, cfg.L, cfg.step),
        np.arange(cfg.L, cfg.L + cfg.bot_margin, cfg.step),
        ))

    return np.array(Lz)

def omega(r) :

    return cfg.om_func(r)

## Get a list of Y speeds for each slice
#def get_LVr() :

# intégrer : ajouter theta(n) + (omega(n) - omega(n-1))
def get_theta(Lomega) :
    global current_theta

    #print(np.rad2deg(current_theta))

    theta = current_theta
    Ltheta = []
    for omega in Lomega :
        Ltheta.append(theta)
        theta += omega*cfg.step

    current_theta = Ltheta[-1]
        
    return np.array(Ltheta)


if __name__ == '__main__':
    # Get a list of z according to the cfg.step
    Lz = get_Lz()

    print(len(Lz))
    # Get a list of radii matching each z
    Lr = curve_generation.curve(Lz)

    # Get inverted values for return pass
    LzRev = list(reversed(Lz)) 
    LrRev = list(reversed(Lz)) 

    if(cfg.plot_mode == '2d') :
        '''2D plotting fairing curve'''
        plt.plot(Lz, Lr, label='r(mm)')

    # Get spindle angular speed
    Lomega = omega(Lr)

    if(cfg.plot_mode == '2d') :
        '''2D plotting angular speed'''
        plt.plot(Lz, Lomega*3000, label='ω(x) (rad/s)')

    else :
        '''3D preparing plot'''
        #ax = plt.axes(projection='3d')
        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        ax.set_xlim3d((-1.1*cfg.L/2, 1.1*cfg.L/2)) 
        ax.set_ylim3d((-1.1*cfg.L/2, 1.1*cfg.L/2)) 
        ax.set_zlim3d((0, 1.1*cfg.L))
        fig.tight_layout()

        plotting.plot_fairing(ax)
        plotting.plot_margin_limits(ax)
        # doesnt work
        #ax.set_box_aspect([ub - lb for lb, ub in (getattr(ax, f'get_{a}lim')() for a in 'xyz')])

    # Pass settings
    pass_shift = 1 # shift en degrès à la fin de chaque passe
    ######## current_shift = 0 # Gradually increasing shift

    # halfpass is a list of thetas matching z
    for i in range(4) :
        # First halfpass
        #################

        # Relevant coordinates : r, theta, z
        halfpass = get_theta(Lomega)
        plot_x = Lz
        plot_y = Lr*np.cos(halfpass)
        plot_z = Lr*np.sin(halfpass)
        
        plotting.plot_toolpath(plot_x, plot_y, plot_z, ax, i)
        #plotting.plot_toolpath_points(plot_x, plot_y, plot_z, ax, fig, i)
       
        current_theta += np.deg2rad(360+180)

        # Return halfpass
        #################

        # Relevant coordinates : TODO
        halfpass = list(reversed(get_theta(Lomega)))
        plot_x = Lz
        plot_y = Lr*np.cos(halfpass)
        plot_z = Lr*np.sin(halfpass)

        plotting.plot_toolpath(plot_x, plot_y, plot_z, ax, i)
#        plotting.plot_toolpath_points(plot_x, plot_y, plot_z, ax, fig, i)

        current_theta += np.deg2rad(360)

        # Preparing next pass
        ######################

        # Shifting for next pass
        #####current_shift += pass_shift
        # Updating theta
        current_theta += np.deg2rad(pass_shift)

    plt.axvline(x=cfg.top_margin, color='red', linestyle=':')
    plt.axvline(x=cfg.L, color='red', linestyle=':')

    if cfg.plot_mode == '2d' :
        plt.axis('equal')

    plt.legend()
    plt.grid()

    ani = matplotlib.animation.FuncAnimation(fig, plotting.toolpath_update, frames=len(plot_x), interval=5)

    plt.show()
