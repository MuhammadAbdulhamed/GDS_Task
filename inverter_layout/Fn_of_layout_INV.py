# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:20:48 2021

@author: muham
"""

def draw_inv(Wn, Wp, Lp, Ln, Wnd, Wpd):
    
    import gdspy
# The GDSII file is called a library, which contains multiple cells.
    lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
    cell = lib.new_cell("Layout_INV")
    
    #Geometry of N_well
    N_well = {"layer":15 , "datatype":15}
    p1 = gdspy.Rectangle((3, -9), (9+(1.5*Wpd),-3+Wp), **N_well)

################Geometry of diffusion p+################
    Diffusion_pplus = {"layer":9 , "datatype":9}
#Geometry of diffusion of pmos Tr
    p2 = gdspy.Rectangle((6, -6), (6+Wpd,-6+Wp), **Diffusion_pplus)
#################################
#Geometry of p+ diffusion for nmos Tr to contact p-substrate with GND (sustrate Tap) 
    p3 = gdspy.Rectangle((-6-(1.5*Wnd), -6+Wn), (-6-Wnd,-6), **Diffusion_pplus)
#######################################################################
################Geometry of diffusion n+################
    Diffusion_nplus = {"layer":25, "datatype":27}
#Geometry of diffusion of nmos Tr
    p4 = gdspy.Rectangle((-6, -6), (-6-Wnd,-6+Wn), **Diffusion_nplus)
#################################
#Geometry of n+ diffusion for pmos Tr to contact n-well with VDD   (N-well Tap)
    p5 = gdspy.Rectangle((6+Wpd, -6), (6+(1.5*Wpd),-6+Wp), **Diffusion_nplus) 
#####################################################################
#Geometry of Gate poly silicon
    Gate_poly={"layer":7 , "datatype":7}
    points_1 = [(6+(Wpd/2)+(Lp/2), -11), (6+(Wpd/2)+(Lp/2), Wp+1), (-6-(Wnd/2)-(Ln/2), Wp+1), (-6-(Wnd/2)-(Ln/2), -11), (-6-(Wnd/2)+(Ln/2), -11), (-6-(Wnd/2)+(Ln/2), Wp-1), (6+(Wpd/2)-(Lp/2), Wp-1), (6+(Wpd/2)-(Lp/2),-11)]
    p6 = gdspy.Polygon(points_1,**Gate_poly)
################Geometry of metal layers################
    Metal_layer= {"layer":  11, "datatype":11}
#Geometry of metal layer between drains of the Trs
    if Wp>=Wn:
        y=-6+(Wn*2/3)
        p7 = gdspy.Rectangle((6+(Wpd/4), -6), (-6-(Wnd/4),y), **Metal_layer)
    elif Wp<Wn:
        y= -6+(Wp*2/3)
        p7 = gdspy.Rectangle((6+(Wpd/4), -6), (-6-(Wnd/4),y), **Metal_layer)
########################################
#Geometry of VDD metal layer
    points_2 = [(6+(2*Wpd/3), -6), (6+(2*Wpd/3), -6+(Wp*2/3)), (6+1.25*Wpd, -6+(Wp*2/3)), (6+1.25*Wpd, 4+Wp), (10+1.5*Wpd, 4+Wp), (10+1.5*Wpd, -16), (6+1.25*Wpd, -16), (6+1.25*Wpd,-6)]
    p8 = gdspy.Polygon(points_2, **Metal_layer)
########################################
#Geometry of GND metal layer
    points_3 = [(-6-(2*Wnd/3), -6), (-6-(2*Wnd/3), -6+(Wn*2/3)), (-6-1.25*Wnd, -6+(Wn*2/3)), (-6-1.25*Wnd, 4+Wn), (-10-1.5*Wnd, 4+Wn), (-10-1.5*Wnd, -16), (-6-1.25*Wnd, -16), (-6-1.25*Wnd,-6)]
    p9 = gdspy.Polygon(points_3, **Metal_layer)
########################################
#Geometry of Contacts
    Contacts={"layer":50,"datatype":50}
 #Geometry of Vdd Contacts
    p10 = gdspy.Rectangle((6+Wpd*1.375, -5.3), (6+Wpd*1.125,-6+(Wp/2)), **Contacts)
    p11 = gdspy.Rectangle((6+(0.92*Wpd), -5.3), (6+(0.75*Wpd),-6+(Wp/2)), **Contacts)
 #Geometry of contacts bet 2 Tr   
    p12 = gdspy.Rectangle((6+(3*Wpd/16) , -5.3), (6+(Wpd/16),y-0.7), **Contacts)
    p13 = gdspy.Rectangle((-6-(Wnd/16), -5.3), (-6-(3*Wnd/16),y-0.7), **Contacts)
#Geometry of GND Contacts    
    p14 = gdspy.Rectangle((-6-Wnd*1.375, -5.3), (-6-Wnd*1.125,-6+(Wn/2)), **Contacts)
    p15 = gdspy.Rectangle((-6-(0.92*Wnd), -5.3), (-6-(0.75*Wnd),-6+(Wn/2)), **Contacts)
###################################################
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

# Save the library in a file called 'FN_of_layout_INV.gds'.
    lib.write_gds('FN_of_layout_INV.gds')

# Optionally, save an image of the cell as SVG.
    cell.write_svg('FN_of_layout_INV.svg')
##############################################################################
draw_inv(6, 8, 2, 2, 10, 10)












