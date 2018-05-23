import numpy as np
import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
import blensor


scanner = bpy.data.objects["Camera"]
drone = bpy.data.objects['done_body']

xpos = np.linspace(-50, 50, 20)
ypos = np.linspace(0, 100, 20)
zpos = np.linspace(0, 10, 20)
yaws = np.linspace(0, 90, 20) # 3rd euler angle

gen = [(x,y,z,yaw) for x in xpos for y in ypos for z in zpos for yaw in yaws]

i = 0
for (x,y,z,yaw) in gen:
    drone.location = (x,y,z)
    drone.rotation_euler = Euler((90, 0, yaw))
    blensor.blendodyne.scan_advanced(scanner, rotation_speed = 10.0, 
                                simulation_fps=24, angle_resolution = 0.1728, 
                                max_distance = 120, evd_file= None,
                                noise_mu=0.0, noise_sigma=0.3, start_angle = 0.0, 
                                end_angle = 360.0, evd_last_scan=True, 
                                add_blender_mesh = True, 
                                add_noisy_blender_mesh = False,
                                frame_time = (1.0 / 24.0),
                                simulation_time = 100.0,
                                world_transformation=scanner.matrix_world)    
    
    i += 1
