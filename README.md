## DC Motor Project

This project models and simulates a DC motor using MATLAB/Simulink.  
The report includes analysis of system dynamics, transfer function derivation, and speed control design.

📘 **Read the full report:** [DC_Motor_Report.pdf](./DCmotor.pdf)

## DC Motor Model

The transfer function of the DC motor is derived as:

$$
\frac{V_A(s)}{\Omega(s)} = \frac{s^2JLI(s) + JsRI(s) + Jsk_e\Omega(s)}{k_{\varphi}I(s) -T_L}
$$

where:
- \(I(s) \) = current
- $\(\Omega(s) \)$ = motor speed
- \( J \) = moment of inertia  
- \( b \) = damping coefficient  
- $\( k_{\varphi} \)$ = motor speed constant
- $\( k_e \)$ = electro-emechanical constant 
- \( R \) = armature resistance  
- \( L \) = armature inductance
- \(T_L \) = torque load

### Key Results
- Implemented PI controller achievieng stable motor operation with a storng distrubance rejection.
- Implemented two control loops: current control loop and speed control loop
