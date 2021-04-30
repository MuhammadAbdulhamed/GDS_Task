# Get Started
GDS_task is simply a python code that use [gdspy package]:https://github.com/heitzmann/gdspy to create a layout design to Cmos Inverter.
in this task i did [inverter_layout folder]:https://bit.ly/2QGVoTT which contains two different python files:- 
1. [inverter_design.py]: https://bit.ly/3aQBpsE that's for generating an inverter with certain dimensions.
2. [Fn_of_layout_INV.py]:https://bit.ly/2RcbPr0 it's a general code for drawing layout of any inverter with different 
dimensions which are controlled through the parameters of the Function. 
 
 # inverter_design.py
 this python code is for generating the layout of Cmos inverter with certain dimensions. 
* **Wn** : Width of the NMOS = 12 um
* **Wp** : Width of the PMOS = 12 um
* **Lp**: Length of the PMOS = 2  um
* **Ln**: Lenght of the NMOS = 2  um
* **Wnd** : Diffusion width of the NMOS = 12 um
* **Wpd** : Diffusion width of the PMOS = 12 um

In this code ***.gds*** and ***.svg*** files are generated to view the layout design.  

`
lib.write_gds('Fixed_Dimensions_inverter.gds')
`

`
cell.write_svg('Fixed_Dimensions_inverter.svg')
 `

The GDS file can be opened in a number of viewers and editors, such as [KLayout]: https://klayout.de/ .

# Fn_of_layout_INV.py
This python code is for generating the layout of Cmos inverter with general dimensions which are specified by the designer 

### The function which is defined in the code:- 

 `
def draw_inv(Wn, Wp, Lp, Ln, Wnd, Wpd):
 `
 whereas :
 
* **Wn** : Width of the NMOS 
* **Wp** : Width of the PMOS 
* **Lp**: Length of the PMOS 
* **Ln**: Lenght of the NMOS 
* **Wnd** : Diffusion width of the NMOS 
* **Wpd** : Diffusion width of the PMOS 
 
You can check the layout design through [FN_of_layout_INV.gds]:https://bit.ly/3t9o3hw using [KLayout]: https://klayout.de/ , 
or through [FN_of_layout_INV.svg]:https://bit.ly/2QBpoRc .
# Conclusion
As known that generating GDS files is a very important stage in the flow of  digital electronic design specially in **ASIC** design flow so **gdspy** is a good and significant EDA tool.

The future work of this task is to use the package for check the design rules of the implemented inverter and implement more circuits.  
