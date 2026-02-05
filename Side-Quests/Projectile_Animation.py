#Projectile Motion Simulation With Air Resistance
#Importing Modules

import numpy as np, pandas as pd, tkinter as tk
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from tkinter import ttk

#State Vectors

class Projectile:

    def __init__(self,mass=1.0,drag=0.05,g=9.81): #Standard Quantities
        self.m=mass
        self.drag=drag
        self.g=g

    def state_eqn(self,t,state):
        x,y,vx,vy=state
        v=np.hypot(vx,vy)
        ax=-(self.drag/self.m)*v*vx
        ay=-self.g-(self.drag/self.m)*v*vy
        return [vx,vy,ax,ay]

    @staticmethod
    def hit_ground(t,state):
        return state[1]

    hit_ground.terminal=True
    hit_ground.direction=-1

#Simulation

class Simulator:

    def __init__(self,model):
        self.model=model
        self.data=None

    def run(self,v0,deg):
        angle=np.deg2rad(deg)
        vx0=v0*np.cos(angle)
        vy0=v0*np.sin(angle)
        sol=solve_ivp(
            self.model.state_eqn,
            (0,100),
            [0,0,vx0,vy0],
            events=self.model.hit_ground,
            max_step=0.05
        )
        t=sol.t
        x,y,vx,vy=sol.y
        self.data=pd.DataFrame({
            "time":t,
            "x":x,
            "y":y,
            "vx":vx,
            "vy":vy
        })
        return self.data

#Visualization & Animation

class Animator:

    def __init__(self,df):
        self.df=df
        self.fig,self.ax=plt.subplots()
        self.ax.set_xlabel("Distance (m)")
        self.ax.set_ylabel("Height (m)")
        self.ax.set_title("Projectile Motion With Air Resistance")
        self.ax.grid(True)
        self.line,=self.ax.plot([],[],lw=2)
        self.point,=self.ax.plot([],[],'ro')
        self.ax.set_xlim(0,df['x'].max()*1.1)
        self.ax.set_ylim(0,df['y'].max()*1.2)

    def animate(self):
        def update(frame):
            self.line.set_data(self.df['x'][:frame],self.df['y'][:frame])
            self.point.set_data([self.df['x'].iloc[frame]],[self.df['y'].iloc[frame]])
            return self.line,self.point

        ani=FuncAnimation(
            self.fig,
            update,
            frames=len(self.df),
            interval=30,
            blit=True
        )
        plt.show()

#Physics GUI

class PhysicsApp:

    def __init__(self,root):
        self.root=root
        self.root.title("Projectile Motion Physics Lab")
        self.building_ui()

    def building_ui(self):
        frame=ttk.Frame(self.root,padding=12)
        frame.grid(row=0,column=0)
        self.inputs={}
        fields =[
            ("Initial Velocity (m/s)","50"),
            ("Launch Angle (deg)","45"),
            ("Mass (kg)","1"),
            ("Drag Coefficient","0.05")
        ]
        for i,(label,default) in enumerate(fields):
            ttk.Label(frame,text=label).grid(row=i,column=0,sticky="W")
            entry=ttk.Entry(frame)
            entry.insert(0,default)
            entry.grid(row=i,column=1)
            self.inputs[label]=entry
        ttk.Button(frame,text="Run Experiment",command=self.run_sim).grid(
            row=len(fields),column=0,columnspan=2,pady=10
        )
        self.result=ttk.Label(frame,text="")
        self.result.grid(row=len(fields)+1,column=0,columnspan=2)

    def run_sim(self):
        v0=float(self.inputs["Initial Velocity (m/s)"].get())
        angle=float(self.inputs["Launch Angle (deg)"].get())
        mass=float(self.inputs["Mass (kg)"].get())
        drag=float(self.inputs["Drag Coefficient"].get())
        model=Projectile(mass,drag)
        simulator=Simulator(model)
        df=simulator.run(v0,angle)
        max_height=df['y'].max()
        r=df['x'].iloc[-1]
        self.result.config(
            text=f"Max Height:{max_height:.2f} m | Range:{r:.2f} m"
        )
        animator=Animator(df)
        animator.animate()

#Main
if __name__=='__main__':
    root=tk.Tk()
    app=PhysicsApp(root)
    root.mainloop()
