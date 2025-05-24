from scipy.io import loadmat
import scipy.io as sio
from os.path import dirname, join as pjoin
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

data_directory = pjoin(dirname("C:\\Users\\limok\\OneDrive\\Documents\\MATLAB\\"))


ISE_current = pjoin(data_directory, 'ISE_current.mat')
ISE_current_time =  pjoin(data_directory, 'ISE_current_time.mat')


ISE_speed = pjoin(data_directory, 'ISE_speed.mat')
ISE_speed_time =  pjoin(data_directory, 'ISE_speed_time.mat')

torque = pjoin(data_directory, 'torque.mat')

current_data = loadmat(ISE_current, spmatrix=False)
current_time_data = loadmat(ISE_current_time, spmatrix=False)

speed_data = loadmat(ISE_speed, spmatrix=False)
speed_time_data = loadmat(ISE_speed_time, spmatrix=False)

torque_data = loadmat(torque, spmatrix=False)

def PrintCurrentData():
    print(sorted(current_data.keys()))
    print(current_data['current'])

def PrintSpeedData():
    print(sorted(speed_data.keys()))
    print(speed_data['speed'])

ISE_current_data = current_data['current'].tolist()
ISE_time_data = current_time_data['current_time'].tolist()

ISE_speed_data = speed_data['speed_data'].tolist()
ISE_speed_time_data = speed_time_data['speed_time'].tolist()

ISE_torque_data = torque_data['torque'].tolist()

df_torque = pd.DataFrame(data=ISE_torque_data, columns=['Torque'])

df_current = pd.DataFrame(data=ISE_current_data, columns=['ISE value'])
df_time_current = pd.DataFrame(data=ISE_time_data, columns=['Time'])
df_with_time_current = df_current.join(df_time_current)
data_current = df_with_time_current.join(df_torque)
print(f"Complete DataFrame for Current:\n{data_current}")


df_speed = pd.DataFrame(data=ISE_speed_data, columns=['ISE value'])
df_time_speed = pd.DataFrame(data=ISE_time_data, columns=['Time'])
df_with_time_speed = df_speed.join(df_time_speed)
data_speed = df_with_time_speed.join(df_torque)
print(f"Complete DataFrame for Speed:\n{data_speed}")


def PrintCurrentISE():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_trisurf(data_current['Torque'], data_current['Time'], data_current['ISE value'], cmap=cm.magma,
                       linewidth=2, antialiased=True)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def PrintSpeedISE():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_trisurf(data_speed['Torque'], data_speed['Time'], data_speed['ISE value'], cmap=cm.magma,
                           linewidth=2, antialiased=True)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def main():
    PrintCurrentISE()
    PrintSpeedISE()
main()



