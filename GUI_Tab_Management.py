# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 13:04


from tkinter import ttk


def gui_tab(window):
    # Insert a tabbed window
    tabControl = ttk.Notebook(window)  # Create Tab Control
    tabControl.grid(row=1, column=0, columnspan=4, sticky="W")  # Pack to make visible
    # Density Conversion Tab
    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Density Conversion')  # Add the tab
    # Bridging Vehicle Table Tab
    tab2 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab2, text='Bridging Table')  # Add the tab
    return (tab1, tab2)


def bridging_tab(tab):
    # Insert a tabbed window
    tabControl = ttk.Notebook(tab)  # Create Tab Control
    tabControl.grid(row=1, column=0, columnspan=3)  # Pack to make visible
    # Density Conversion Tab
    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='4 Compartment')  # Add the tab
    # Bridging Vehicle Table Tab
    tab2 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab2, text='5 Compartment')  # Add the tab
    return (tab1, tab2)
