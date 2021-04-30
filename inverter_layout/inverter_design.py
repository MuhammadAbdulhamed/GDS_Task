# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:57:23 2021

@author: muham
"""
import gdspy

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('Task_test')
######################
#Geometry of N_well
N_well = {"layer":15 , "datatype":15}
p1 = gdspy.Rectangle((4, -8), (26, 8), **N_well)
################Geometry of diffusion p+################
Diffusion_pplus = {"layer":9 , "datatype":9}
#Geometry of diffusion of pmos Tr
p2 = gdspy.Rectangle((6, -6), (18,6), **Diffusion_pplus)
#################################
#Geometry of p+ diffusion for nmos Tr to contact p-substrate with GND (sustrate Tap) 
p3 = gdspy.Rectangle((-24, 6), (-18,-6), **Diffusion_pplus)
#######################################################################
################Geometry of diffusion n+################
Diffusion_nplus = {"layer":25, "datatype":27}
#Geometry of diffusion of nmos Tr
p4 = gdspy.Rectangle((-6, -6), (-18,6), **Diffusion_nplus)
#################################
#Geometry of n+ diffusion for pmos Tr to contact n-well with VDD   (N-well Tap)
p5 = gdspy.Rectangle((18, -6), (24,6), **Diffusion_nplus)
#####################################################################
#Geometry of Gate poly silicon
Gate_poly={"layer":7 , "datatype":7}
points_1 = [(13, -10), (13, 11), (-13, 11), (-13, -10), (-11, -10), (-11, 9), (11, 9), (11,-10)]
p6 = gdspy.Polygon(points_1,**Gate_poly)
################Geometry of metal layers################
Metal_layer= {"layer":  11, "datatype":11}
#Geometry of metal layer between drains of the Trs
p7 = gdspy.Rectangle((10, -4), (-10,4), **Metal_layer)
########################################
#Geometry of VDD metal layer
points_2 = [(14, -4), (14, 4), (21, 4), (21, 16), (27, 16), (27, -16), (21, -16), (21,-4)]
p8 = gdspy.Polygon(points_2, **Metal_layer)
########################################
#Geometry of GND metal layer
points_3 = [(-14, -4), (-14, 4), (-21, 4), (-21, 16), (-27, 16), (-27, -16), (-21, -16), (-21,-4)]
p9 = gdspy.Polygon(points_3, **Metal_layer)
########################################
#Geometry of Contacts
Contacts={"layer":50,"datatype":50}
p10 = gdspy.Rectangle((22, -2), (20,2), **Contacts)
p11 = gdspy.Rectangle((17, -2), (15,2), **Contacts)
p12 = gdspy.Rectangle((9 , -2), (7,2), **Contacts)
p13 = gdspy.Rectangle((-7, -2), (-9,2), **Contacts)
p14 = gdspy.Rectangle((-15, -2), (-17,2), **Contacts)
p15 = gdspy.Rectangle((-20, -2), (-22,2), **Contacts)
#######################
cell.add(p1)
cell.add(p2)
cell.add(p3)
cell.add(p4)
cell.add(p5)
cell.add(p6)
cell.add(p7)
cell.add(p8)
cell.add(p9)
cell.add(p10)
cell.add(p11)
cell.add(p12)
cell.add(p13)
cell.add(p14)
cell.add(p15)

#######################




# Save the library in a file called 'Fixed_Dimensions_inverter.gds'.
lib.write_gds('Fixed_Dimensions_inverter.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('Fixed_Dimensions_inverter.svg')



