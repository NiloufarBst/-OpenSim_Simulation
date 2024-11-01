import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
step_error= pd.read_csv('step.csv')
step_ini90_error=pd.read_csv('step_ini90.csv')
sin01_error=pd.read_csv('sin_01.csv')
sin025_error=pd.read_csv('sin_025.csv')
sin08_error=pd.read_csv('sin_08.csv')
threshold=0.1
# Compute RMSE for each column of
for col in range(step_error.shape[1]):
    error1 = step_error.iloc[:, col]  #replacing the data
    settle_smap1= np.argmax(error1 < threshold)
    settle1 = (settle_smap1 + 1)/1000
    actual = abs(step_error.iloc[9999, col])
    print(f"step setle time , column {col+ 1}: {settle1}")
def plot_activation_step() :
    x = np.linspace(0, 10, 10000, endpoint=True)
    step_act = pd.read_csv('activation_step.csv')
    columns = step_act.columns[:4]
    lines = []
    for col in columns:
        line, = plt.plot(x,step_act[col],linewidth=0.8)
        lines.append(line)
    plt.xlabel('time(s)')
    plt.ylabel('Muscle activation')
    plt.title('Muscle activation for step target_initial angle 0rad (0deg)')
    plt.legend(lines, ['1.31rad (75deg)', '1.57rad (90deg)', '1.92rad (110deg)','2.27rad (130)'])
    plt.grid(True)
    plt.show()
def plot_activation_step_initial90() :
    x = np.linspace(0, 10, 10000, endpoint=True)
    step_ini90_act = pd.read_csv('activation_step_ini90.csv')
    columns = step_ini90_act.columns[:4]
    lines = []
    for col in columns:
        line, = plt.plot(x,step_ini90_act[col],linewidth=0.8)
        lines.append(line)
    plt.xlabel('time(s)')
    plt.ylabel('Muscle activation')
    plt.title('Muscle activation for step target_initial angle 1.57rad (90deg)')
    plt.legend(lines, ['1.31rad (75deg)', '1.92rad (110deg)','2.27rad (130)'])
    plt.grid(True)
    plt.show()
def plot_activation_sin1() :
    x = np.linspace(0, 10, 10000, endpoint=True)
    sin01_act = pd.read_csv('activation_sin_01.csv')
    columns = sin01_act.columns[:4]
    lines = []
    for col in columns:
        line, = plt.plot(x,sin01_act[col],linewidth=0.8)
        lines.append(line)
    plt.xlabel('time(s)')
    plt.ylabel('Muscle activation')
    plt.title('Muscle activation for sinusoid(0.1Hz) target ')
    plt.legend(lines, ['1.31rad (75deg)', '1.57rad (90deg)', '1.92rad (110deg)','2.27rad (130)'])
    plt.grid(True)
    plt.show()
def plot_activation_sin2():
    x = np.linspace(0, 10, 10000, endpoint=True)
    sin025_act = pd.read_csv('activation_sin_025.csv')
    columns = sin025_act.columns[:4]
    lines = []
    for col in columns:
        line, = plt.plot(x,sin025_act[col],linewidth=0.8)
        lines.append(line)
    plt.xlabel('time(s)')
    plt.ylabel('Muscle activation')
    plt.title('Muscle activation for sinusoid(0.25Hz) target ')
    plt.legend(lines, ['1.31rad (75deg)', '1.57rad (90deg)', '1.92rad (110deg)','2.27rad (130deg)'])
    plt.grid(True)
    plt.show()
def plot_activation_sin8():
    x = np.linspace(0, 10, 10000, endpoint=True)
    sin08_act = pd.read_csv('activationsin_sin_08.csv')
    columns = sin08_act.columns[:4]
    lines = []
    for col in columns:
        line, = plt.plot(x,sin08_act[col],linewidth=0.8)
        lines.append(line)
    plt.xlabel('time(s)')
    plt.ylabel('Muscle activation')
    plt.title('Muscle activation for sinusoid(0.8Hz) target ')
    plt.legend(lines,['1.31rad (75deg)', '1.57rad (90deg)', '1.92rad (110deg)','2.27rad (130)'])
    plt.grid(True)
    plt.show()
plot_activation_step()
plot_activation_step_initial90()
plot_activation_sin1()
plot_activation_sin2()
plot_activation_sin8()