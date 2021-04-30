# Get Started
GDS_task is simply a python code that use [gdspy package]:https://github.com/heitzmann/gdspy to create a layout design to Cmos Inverter.
in this task i did [inverter_layout folder]:https://bit.ly/2QGVoTT which contains two different python files 
1. [inverter_design.py]: https://bit.ly/3aQBpsE that's for generating an inverter with certain dimensions.
2. [Fn_of_layout_INV.py]:https://bit.ly/2RcbPr0 it's a general code for drawing layout of any inverter with different 
dimensions which are controlled through the parameters of the Function 

 `
def draw_inv(Wn, Wp, Lp, Ln, Wnd, Wpd):
 `
 
 # inverter_design.py
 this python code is for generating the layout of Cmos inverter with certain dimensions
* **Wn** : Width of the NMOS = 12 um
* **Wp** : Width of the PMOS = 12 um
* **Lp**: Length of the PMOS = 2  um
* **Ln**: Lenght of the NMOS = 2  um
* **Wnd** : Diffusion width of the NMOS = 12 um
* **Wpd** : Diffusion width of the PMOS = 12 um

In this code ***.gds*** and ***.svg*** files are generated to view the layout design  

`
lib.write_gds('Fixed_Dimensions_inverter.gds')

cell.write_svg('Fixed_Dimensions_inverter.svg')
 `


