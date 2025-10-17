## DC Motor Project

This project models and simulates a DC motor using MATLAB/Simulink.  
The report includes analysis of system dynamics, transfer function derivation, and speed control design.

📘 **Read the full report:** [DC_Motor_Report.pdf](./DCmotor.pdf)

## DC Motor Model

The transfer function of the DC motor is derived as:

$$
G(s) = \frac{K}{(J s + b)(L s + R) + K^2}
$$

where:

- \( J \) = moment of inertia  
- \( b \) = damping coefficient  
- \( K \) = motor constant  
- \( R \) = armature resistance  
- \( L \) = armature inductance

### Key Results
- Derived transfer function:  
  $$
  G(s) = \frac{K}{(Js + b)(Ls + R) + K^2}
  $$
- Implemented PI controller achievieng stable motor operation with a storng distrubance rejection.
- Implemented two control loops: current control loop and speed control loop
