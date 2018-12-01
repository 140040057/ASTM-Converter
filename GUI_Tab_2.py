# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 13:03


import tkinter as tk
from tkinter import ttk


def tab_2_1(sub_tab, onclick, i):
    # Density and Temperature Labels
    tk.Label(sub_tab, text="Density").grid(row=i + 1, column=0, padx=10, pady=5)
    tk.Label(sub_tab, text="Temperature").grid(row=i + 1, column=1, padx=10, pady=5)
    tk.Label(sub_tab, text="Density @ 15 deg").grid(row=i + 1, column=2, padx=10, pady=5)

    input_den = [0, 0, 0, 0]
    input_temp = [0, 0, 0, 0]
    output_den15 = [0, 0, 0, 0]
    output_avg = [0, 0, 0]
    # Create Input fields
    # Density and Temperature
    input_den[0] = tk.Entry(sub_tab, width=20)
    input_den[0].grid(row=i + 2, column=0, padx=10, pady=5)
    input_temp[0] = tk.Entry(sub_tab, width=20)
    input_temp[0].grid(row=i + 2, column=1, padx=10, pady=5)
    input_den[1] = tk.Entry(sub_tab, width=20)
    input_den[1].grid(row=i + 3, column=0, padx=10, pady=5)
    input_temp[1] = tk.Entry(sub_tab, width=20)
    input_temp[1].grid(row=i + 3, column=1, padx=10, pady=5)
    input_den[2] = tk.Entry(sub_tab, width=20)
    input_den[2].grid(row=i + 4, column=0, padx=10, pady=5)
    input_temp[2] = tk.Entry(sub_tab, width=20)
    input_temp[2].grid(row=i + 4, column=1, padx=10, pady=5)
    input_den[3] = tk.Entry(sub_tab, width=20)
    input_den[3].grid(row=i + 5, column=0, padx=10, pady=5)
    input_temp[3] = tk.Entry(sub_tab, width=20)
    input_temp[3].grid(row=i + 5, column=1, padx=10, pady=5)

    # Calculate button to execute the command
    tk.Button(sub_tab, text="Calculate Density", command=onclick).grid(row=i + 7, column=0, columnspan=3, padx=10,
                                                                       pady=5)

    # Output fields
    output_den15[0] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[0].grid(row=i + 2, column=2, padx=10, pady=5)
    output_den15[1] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[1].grid(row=i + 3, column=2, padx=10, pady=5)
    output_den15[2] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[2].grid(row=i + 4, column=2, padx=10, pady=5)
    output_den15[3] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[3].grid(row=i + 5, column=2, padx=10, pady=5)

    # Add Average Values
    pane = ttk.Panedwindow(sub_tab, orient=tk.VERTICAL)
    pane.grid(row=i + 6, column=0, columnspan=3)  # Pack to make visible
    # first pane, which would get widgets gridded into it:
    f1 = ttk.Labelframe(pane, text='Average')
    output_avg[0] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[0].grid(row=0, column=0, padx=10, pady=5)
    output_avg[1] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[1].grid(row=0, column=1, padx=10, pady=5)
    output_avg[2] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[2].grid(row=0, column=2, padx=10, pady=5)
    pane.add(f1)

    return input_den, input_temp, output_den15, output_avg, 4


def tab_2_2(sub_tab, onclick, i):
    # Density and Temperature Labels
    tk.Label(sub_tab, text="Density").grid(row=i + 1, column=0, padx=10, pady=5)
    tk.Label(sub_tab, text="Temperature").grid(row=i + 1, column=1, padx=10, pady=5)
    tk.Label(sub_tab, text="Density @ 15 deg").grid(row=i + 1, column=2, padx=10, pady=5)

    input_den = [0, 0, 0, 0, 0]
    input_temp = [0, 0, 0, 0, 0]
    output_den15 = [0, 0, 0, 0, 0]
    output_avg = [0, 0, 0]
    # Create Input fields
    # Density and Temperature
    input_den[0] = tk.Entry(sub_tab, width=20)
    input_den[0].grid(row=i + 2, column=0, padx=10, pady=5)
    input_temp[0] = tk.Entry(sub_tab, width=20)
    input_temp[0].grid(row=i + 2, column=1, padx=10, pady=5)
    input_den[1] = tk.Entry(sub_tab, width=20)
    input_den[1].grid(row=i + 3, column=0, padx=10, pady=5)
    input_temp[1] = tk.Entry(sub_tab, width=20)
    input_temp[1].grid(row=i + 3, column=1, padx=10, pady=5)
    input_den[2] = tk.Entry(sub_tab, width=20)
    input_den[2].grid(row=i + 4, column=0, padx=10, pady=5)
    input_temp[2] = tk.Entry(sub_tab, width=20)
    input_temp[2].grid(row=i + 4, column=1, padx=10, pady=5)
    input_den[3] = tk.Entry(sub_tab, width=20)
    input_den[3].grid(row=i + 5, column=0, padx=10, pady=5)
    input_temp[3] = tk.Entry(sub_tab, width=20)
    input_temp[3].grid(row=i + 5, column=1, padx=10, pady=5)
    input_den[4] = tk.Entry(sub_tab, width=20)
    input_den[4].grid(row=i + 6, column=0, padx=10, pady=5)
    input_temp[4] = tk.Entry(sub_tab, width=20)
    input_temp[4].grid(row=i + 6, column=1, padx=10, pady=5)

    # Calculate button to execute the command
    tk.Button(sub_tab, text="Calculate Density", command=onclick).grid(row=i + 8, column=0, columnspan=3, padx=10,
                                                                       pady=5)

    # Output fields
    output_den15[0] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[0].grid(row=i + 2, column=2, padx=10, pady=5)
    output_den15[1] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[1].grid(row=i + 3, column=2, padx=10, pady=5)
    output_den15[2] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[2].grid(row=i + 4, column=2, padx=10, pady=5)
    output_den15[3] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[3].grid(row=i + 5, column=2, padx=10, pady=5)
    output_den15[4] = tk.Text(sub_tab, state='disabled', width=15, height=1)
    output_den15[4].grid(row=i + 6, column=2, padx=10, pady=5)

    # Add Average Values
    pane = ttk.Panedwindow(sub_tab, orient=tk.VERTICAL)
    pane.grid(row=i + 7, column=0, columnspan=3)  # Pack to make visible
    # first pane, which would get widgets gridded into it:
    f1 = ttk.Labelframe(pane, text='Average')
    output_avg[0] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[0].grid(row=0, column=0, padx=10, pady=5)
    output_avg[1] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[1].grid(row=0, column=1, padx=10, pady=5)
    output_avg[2] = tk.Text(f1, state='disabled', width=15, height=1)
    output_avg[2].grid(row=0, column=2, padx=10, pady=5)
    pane.add(f1)

    return input_den, input_temp, output_den15, output_avg, 5
