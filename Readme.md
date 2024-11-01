# Muscle Activation Control Using Arm Position Feedback Simulation with OpenSim

This project simulates the control of arm muscle activation, specifically targeting the `BIClong` muscle, using position feedback for the elbow joint in the `arm26_test.osim` model. The simulation uses OpenSim and Python to explore feedback-based control for achieving specific arm positions through muscle activation.

## Contents

1. [Requirements](#requirements)
2. [File Structure](#file-structure)
3. [Project Overview](#project-overview)
4. [Simulation Code Details](#simulation-code-details)
5. [Evaluation Code Details](#evaluation-code-details)
6. [Usage Instructions](#usage-instructions)
7. [Results and Visualization](#results-and-visualization)

---

### Requirements

To run this simulation, you’ll need the following:

- **OpenSim 4.4** installed on your machine.
- **Python 3.8+** with the following packages:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `opensim` (Python API for OpenSim)

 ### Evaluation 
  This code will read the logged data from CSV files generated during the simulation and calculate metrics such as RMSE and settling time, as well as plot muscle activation and error trends over time.