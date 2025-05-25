%close all;clear;clc;

V=100;R=5;

TL=2;
kphi=1.5;
OM=50;

L=0.05;
J=0.05;

T_p = 0.01

Kb = 18
Tii= L/R
Kpi = Tii/(2*(1/R)*T_p)
Kii = Kpi/Tii

Tiw = 4*2*T_p
Kpw = J/(2*kphi*2*T_p)
Kiw = Kpw/Tiw


current_time = out.ISE_current.Time
current_data = out.ISE_current.Data
speed_time = out.ISE_speed.Time
speed_data = out.ISE_speed.Data
torque = out.torque.Data





