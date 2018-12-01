# Created by Naman Gupta (00512693)
# Created on 21-11-2018 at 12:59


# Import ASTM data file to array
import numpy as np

data_astm = np.genfromtxt('ASTM Datapoints.csv', delimiter=",")

data_density = data_astm[0, :]
data_temp = data_astm[:, 0]


def density_15(density, temp):
    if (density > 920 or density < 670 or temp < 0 or temp > 50):
        return 9999
    else:
        # Density Index
        density_floor = int(density)
        density_dec = density - density_floor
        density_roof = density_floor + 1
        index_den_floor = np.where(data_density == density_floor)[0][0]
        index_den_roof = np.where(data_density == density_roof)[0][0]
        # Temperature Index
        temp_floor = int(temp)
        temp_dec = temp - temp_floor
        if (temp_dec >= 0.8 and temp_dec <= 0.9):
            temp_mod = temp_floor + 1
        elif (temp_dec >= 0.3 and temp_dec <= 0.7):
            temp_mod = temp_floor + 0.5
        else:
            temp_mod = temp_floor
        index_temp = np.where(data_temp == temp_mod)[0][0]
        density_15_floor = data_astm[index_temp, index_den_floor]
        density_15_roof = data_astm[index_temp, index_den_roof]
        result = density_15_roof - (density_15_roof - density_15_floor) * (1 - density_dec)
        return (result)
