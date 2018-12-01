# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 13:01


import tkinter as tk
from ASTM_functions import density_15 as dc
from statistics import mean


def calc_density(output, input_density, input_temp):
    density = 0
    temp = 0
    density = input_density.get()
    temp = input_temp.get()
    if not density or not temp:
        result = "Error"
        output.configure(state='normal')
        output.delete(0.0, tk.END)
        output.insert(tk.END, result)
        output.configure(state='disabled')
    else:
        density = float(density)
        temp = float(temp)
        result = round(dc(density, temp), 2)
        if result == 9999:
            output.configure(state='normal')
            output.delete(0.0, tk.END)
            output.insert(tk.END, "Limit Error")
            output.configure(state='disabled')
        else:
            output.configure(state='normal')
            output.delete(0.0, tk.END)
            output.insert(tk.END, result)
            output.configure(state='disabled')


def calc_den_bridge(input_den, input_temp, output_den15, output_avg, compartment):
    dummy = list(range(0, compartment))
    avg_den = []
    avg_temp = []
    avg_den15 = []
    for i in dummy:
        density = input_den[i].get()
        temp = input_temp[i].get()
        if not density or not temp:
            result = "Error"
            output_den15[i].configure(state='normal')
            output_den15[i].delete(0.0, tk.END)
            output_den15[i].insert(tk.END, result)
            output_den15[i].configure(state='disabled')
        else:
            density = float(density)
            temp = float(temp)
            result = round(dc(density, temp), 2)
            if result == 9999:
                result = "Limit Error"
                output_den15[i].configure(state='normal')
                output_den15[i].delete(0.0, tk.END)
                output_den15[i].insert(tk.END, result)
                output_den15[i].configure(state='disabled')
                avg_den15.append(result)
            else:
                output_den15[i].configure(state='normal')
                output_den15[i].delete(0.0, tk.END)
                output_den15[i].insert(tk.END, result)
                output_den15[i].configure(state='disabled')
                avg_den.append(density)
                avg_temp.append(temp)
                avg_den15.append(result)

    if "Limit Error" in avg_den15:
        for i in [0, 1, 2]:
            output_avg[i].configure(state='normal')
            output_avg[i].delete(0.0, tk.END)
            output_avg[i].insert(tk.END, "Limit Error")
            output_avg[i].configure(state='disabled')
    else:
        for i in [0, 1, 2]:
            output_avg[i].configure(state='normal')
            output_avg[i].delete(0.0, tk.END)
        output_avg[0].insert(tk.END, round(mean(avg_den), 2))
        output_avg[1].insert(tk.END, round(mean(avg_temp), 2))
        output_avg[2].insert(tk.END, round(mean(avg_den15), 2))
        for i in [0, 1, 2]:
            output_avg[i].configure(state='disabled')
    return
