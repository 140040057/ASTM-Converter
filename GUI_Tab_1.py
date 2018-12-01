# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 13:03


import tkinter as tk


def tab_1(tab, onclick, i):
    # Density
    tk.Label(tab, text="Density:").grid(row=i + 1, column=0, padx=10, pady=5)
    input_density = tk.Entry(tab, width=20)
    input_density.grid(row=i + 1, column=1, padx=10, pady=5)
    # Temperature
    tk.Label(tab, text="Temperature:").grid(row=i + 1, column=2, padx=10, pady=5)
    input_temp = tk.Entry(tab, width=20)
    input_temp.grid(row=i + 1, column=3, padx=10, pady=5)

    # Calculate button to execute the command
    tk.Button(tab, text="Calculate Density", command=onclick).grid(row=i + 2, column=0, columnspan=4, padx=10, pady=5)

    # Output of the result
    tk.Label(tab, text="Density at 15 Deg:").grid(row=i + 3, column=0, columnspan=2)
    output = tk.Text(tab, state='disabled', width=20, height=1)
    output.grid(row=i + 3, column=2, columnspan=2, padx=10, pady=5)

    # # Add feedback
    # p = ttk.Panedwindow(tab, orient=tk.VERTICAL)
    # # first pane, which would get widgets gridded into it:
    # f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)  # second pane
    # p.add(f1)

    return output, input_density, input_temp
