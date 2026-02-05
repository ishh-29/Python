#Projectile Motion Simulation With Air Resistance
#Importing Modules

import numpy as np, pandas as pd
import matplotlib.pyplot as plt, tkinter as tk
from scipy.integrate import solve_ivp
from tkinter import ttk

#Function For State Vectors

def state_vecs(t,state,m,g,air_res):
    x,y,vx,vy=state
    v=np.sqrt(vx**2+vy**2)
    #Air Resistance (Opposite To Velocity v)
    ax=-(air_res/m)*v*vx
    ay=-g-(air_res/m)*v*vy
    return [vx,vy,ax,ay]

def hit_ground(t,state,*args):
    #Stopping Integration When y=0 (Hitting The Ground)
    return state[1]

hit_ground.terminal=True
hit_ground.direction=-1

#Function For Simulation

def run_sim(v0,deg,mass,drag):
    g=9.81
    angle=np.deg2rad(deg)
    vx0=v0*np.cos(angle)
    vy0=v0*np.sin(angle)
    initial_state=[0.0,0.0,vx0,vy0]
    sol=solve_ivp(
        state_vecs,
        t_span=(0,100),
        y0=initial_state,
        args=(mass,g,drag),
        events=hit_ground,
        max_step=0.05
    )
    t=sol.t
    x,y,vx,vy=sol.y
    #Storing Results In Dataframe
    df=pd.DataFrame({
        "Time (s)":t,
        "x (m)":x,
        "y (m)": y,
        "vx (m/s)":vx,
        "vy (m/s)":vy
    })
    return df

#Function For Plotting

def trajectory_plot(df):
    plt.figure(figsize=(8,4))
    plt.plot(df["x (m)"], df["y (m)"])
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("Projectile Motion with Air Resistance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Function For Tkinter GUI

def start_sim():
    v0=float(v0_entry.get())
    angle=float(angle_entry.get())
    mass=float(mass_entry.get())
    drag=float(drag_entry.get())
    df=run_sim(v0,angle,mass,drag)
    #Showing Results In The GUI
    max_h=df["y (m)"].max()
    r=df["x (m)"].iloc[-1]
    res.config(
        text=f"Maximum Height:{max_h:.2f} m\nRange:{r:.2f} m")
    trajectory_plot(df)


#Stagging The GUI 
root=tk.Tk()
root.title("Projectile Motion")
main_f=ttk.Frame(root,padding=1)
main_f.grid(row=0,column=0,sticky='NSEW') #Grid Layout

#Input Feilds

ttk.Label(main_f,text="Initial Velocity (m/s)").grid(row=0,column=0,sticky="W")
v0_entry=ttk.Entry(main_f)
v0_entry.insert(0,"50")
v0_entry.grid(row=0,column=1)

ttk.Label(main_f,text="Angle (degrees)").grid(row=1,column=0,sticky="W")
angle_entry=ttk.Entry(main_f)
angle_entry.insert(0,"45")
angle_entry.grid(row=1,column=1)

ttk.Label(main_f,text="Mass (kg)").grid(row=2,column=0,sticky="W")
mass_entry=ttk.Entry(main_f)
mass_entry.insert(0,"1")
mass_entry.grid(row=2,column=1)

ttk.Label(main_f,text="Drag Coefficient").grid(row=3,column=0,sticky="W")
drag_entry=ttk.Entry(main_f)
drag_entry.insert(0,"0.05")
drag_entry.grid(row=3,column=1)

#Buttons

sim_button=ttk.Button(main_f,text="Simulate",command=start_sim)
sim_button.grid(row=4,column=0,columnspan=2,pady=10)

#Results Label

res=ttk.Label(main_f,text="")
res.grid(row=5,column=0,columnspan=2)

#Starting 

root.mainloop()