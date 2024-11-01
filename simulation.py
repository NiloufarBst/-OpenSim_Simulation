import opensim as osim
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import csv
os.add_dll_directory("C:/OpenSim 4.4/bin")
model_path = "C:\OpenSim 4.4\Resources\Code\Python\Moco\project\Arm26/arm26_test.osim"
model = osim.Model(model_path)
model.setUseVisualizer(True)
state=model.initSystem()
muscle=model.getMuscles().get('BIClong')
current_angle = model.getCoordinateSet().get('r_elbow_flex').getValue(state)
time = 0
Integral=0
error=0
previousError=0
def update_position(time):
    # target_angle sin wave
    frequency = 0.25
    amplitude = np.deg2rad(110)# Amplitude
    time_values = []
    target_angles = []
    current_angles = []
    model = osim.Model(model_path)
    model.setUseVisualizer(True)
    # simulation
    state = model.initSystem()
    Coordinate_Set = model.getCoordinateSet()
    Coordinate_Set.get('r_shoulder_elev').setLocked(state, True)
    # refrence at 90 degrees
    #Coordinate_Set.get('r_elbow_flex').setValue(state, 0.5 * osim.SimTK_PI)
    manager = osim.Manager(model)
    state.setTime(0)
    manager.initialize(state)
    muscle = model.getMuscles().get('BIClong')
    # Perform the simulation
    time = 0
    current_angle = model.getCoordinateSet().get('r_elbow_flex').getValue(state)
    Integral = 0
    Kp = 0.18  # Proportional gain
    Ki = 0.3
    dt = 0.001  # Time step
    while time < 10:
        #target_angle = np.deg2rad(130)  # Step angle
        target_angle = abs(amplitude * math.sin(2 * math.pi * frequency * time))  #sinusoid angle
        error = target_angle - current_angle
        Integral += error * dt
        activation =Kp * error + Ki * Integral
        #activation =0.1445+Kp * error + Ki * Integral   #initial angle qgual to 90
        muscle.setActivation(state, activation)
        model.realizeDynamics(state)
        value = muscle.getActivation(state)
        current_angle = model.getCoordinateSet().get('r_elbow_flex').getValue(state)
        momarm = muscle.computeMomentArm(state, model.getCoordinateSet().get('r_elbow_flex'))
        time_values.append(time)
        target_angles.append(target_angle)
        current_angles.append(current_angle)
        activations.append(activation)
        moment_arms.append(momarm)
        errors.append(error)
        with open("sin_130_0.1_act.csv", 'a', newline='') as f:
             writer = csv.writer(f)
             writer.writerow(([value]))
        with open("sin_130_0.1_error.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(([error]))
        state = manager.integrate(time)
        time = time + dt
    fig, (ax1, ax2 ) = plt.subplots(2, 1, sharex=True)
    ax1.plot(time_values, target_angles, label='angle_target')
    ax1.plot(time_values, current_angles, label='angle_output')
    ax1.set_ylabel('angle(rad)')
    ax1.set_ylim([0, 2.5])
    ax1.set_xlim([0, 11])
    ax1.set_title('target vs output angle_0.25Hz')
    ax1.legend()
    ax1.grid(True)
    ax2.plot(time_values, errors, label='error')
    ax2.set_xlabel('time(s)')
    ax2.set_ylabel('error(rad)')
    ax2.set_ylim([0, 2.5])
    ax2.set_xlim([0, 11])
    ax2.legend()
    ax2.grid(True)
    plt.show()
time_values = []
target_angles = []
current_angles = []
activations = []
moment_arms = []
errors=[]
update_position(time)