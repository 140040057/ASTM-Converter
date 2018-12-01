# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 13:00


import tkinter as tk
from tkinter import ttk
from GUI_Tab_Management import gui_tab, bridging_tab
from GUI_Tab_1 import tab_1
from GUI_Tab_2 import tab_2_1, tab_2_2
from GUI_functions import calc_density, calc_den_bridge


# Click/Return function to Calculate Density at 15 deg

def onclick_1():
    calc_density(output, input_density, input_temperature)


def onclick_2():
    calc_den_bridge(input_den, input_temp, output_den15, output_avg, compartment)


# Create a window
window = tk.Tk()
window.title("ASTM Convertor")

# # Image/Logo inserted
# logo_ioc = tk.PhotoImage(file = "iocl_logo.gif")
# tk.Label(window,image = logo_ioc).grid(row=0, column=0)

# Title of the Window
tk.Label(window, text="ASTM Density conversion to 15 Deg").grid(row=0, column=0, columnspan=4, padx=10, pady=5)
i = 1
# Insert a tabbed window
tab = gui_tab(window)

# Tab 1 for Inputs for Density and Temperature
output, input_density, input_temperature = tab_1(tab[0], onclick_1, i)

# Tab 2 for Inputs for Density and Temperature
sub_tab = bridging_tab(tab[1])
input_den, input_temp, output_den15, output_avg, compartment = tab_2_1(sub_tab[0], onclick_2, i)
input_den, input_temp, output_den15, output_avg, compartment = tab_2_2(sub_tab[1], onclick_2, i)

# Add About
pane = ttk.Panedwindow(window, orient=tk.VERTICAL)
pane.grid(row=4, column=0, columnspan=4)  # Pack to make visible
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(pane, text='About')
tk.Label(f1, text="v1.0.0").grid(row=0, column=0, padx=10, sticky="W")
tk.Label(f1, text=" ").grid(row=0, column=1, ipadx=85, sticky="W")
tk.Label(f1, text="Created by: Naman Gupta (00512693)").grid(row=0, column=2, padx=10, sticky="W")
pane.add(f1)

# End of the window loop
window.mainloop()
