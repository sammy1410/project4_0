import streamlit as st
import pandas as pd
from datetime import datetime
from utility.motor import motors_init
import RPi.GPIO as GPIO
from utility.shared import this
import time

from utility.mathModule import smoothingfunc
import numpy as np

def clearList():
    this.rotationList.clear()


def appendList():
    this.rotationList.append({
        "base": this.base_angle,
        "shoulder": this.shoulder_angle,
        "elbow": this.elbow_angle,
        "wrist": this.roll_angle,
        "pitch": this.pitch_angle,
        "yaw": this.yaw_angle,
        "time": this.timeStall
    })

def exit_threads():
    del this.motors
    for i in this.motors_list.values():
            i.exit_thread=True
            i.event.set()
            i.thread.join()
            i.pwm.stop()
    
    GPIO.cleanup()
    this.pageName="Admin"
    print("Motors Exited")

def rotate_list():
    if "motors" in this:
        #with open('move.txt', 'r') as file:
        #    lines = file.readlines()
        for value in this.rotationList:
            this.base.task.append(value["base"])
            #print(f'Base {value["base"]}')
            this.shoulder.task.append(value["shoulder"])
            #print(f'Shoulder {value["shoulder"]}')
            this.elbow.task.append(value["elbow"])
            #print(f'Elbow {value["elbow"]}')
            this.roll.task.append(value["wrist"])
            #print(f'Wrist {value["wrist"]}')
            this.pitch.task.append(value["pitch"])
            #print(f'Pitch {value["pitch"]}')
            this.yaw.task.append(value["yaw"])
            #print(f'Yaw {value["yaw"]}')

            for i in this.motors_list.values():
                i.event.set()

            time.sleep(this.timeStall)   
        
def update_motors():
    if "motors" in this:      
        this.base.task.append(this.base_angle)
        this.shoulder.task.append(this.shoulder_angle)
        this.elbow.task.append(this.elbow_angle)
        this.roll.task.append(this.roll_angle)
        this.pitch.task.append(this.pitch_angle)
        this.yaw.task.append(this.yaw_angle)
        
        for i in this.motors_list.values():
            i.a = this.a
            i.b = this.b
            i.c = this.c
            i.event.set()

def layout():
    coltit,colbut = st.columns(2)
    with coltit:
        st.write("SCADA System")
    with colbut:
        live = st.toggle("Live Mode")

    if "motors" not in this:
        this.a = 0
        this.b = 0
        this.c = 0.5
        
        this.motors=True
        this.rotationList = []
        GPIO.setwarnings(False)
        GPIO.cleanup()
        motors_init()
        
        from utility.motor import base,shoulder,wrist_roll,end_pitch,end_yaw,elbow
        this.base=base
        this.shoulder=shoulder
        this.roll=wrist_roll
        this.pitch=end_pitch
        this.yaw=end_yaw
        this.elbow=elbow
        base.exit_thread = False

        this.motors_list = {
            "base" :this.base,
            "shoulder":this.shoulder,
            "wrist":this.roll,
            "elbow":this.elbow,
            "pitch":this.pitch,
            "yaw":this.yaw
        }
        
    col1,col2,col3=st.columns(3)

    with col1:
        this.base_angle = st.slider("Base Angle",0,180,value=this.base.old_angle)
        this.roll_angle = st.slider("Roll Angle",0,180,value=this.roll.old_angle)

    with col2:
        this.shoulder_angle = st.slider("Shoulder Angle",0,180,value=this.shoulder.old_angle)
        this.pitch_angle = st.slider("Pitch Angle",0,180,value=this.pitch.old_angle)

    with col3:
        this.elbow_angle = st.slider("Elbow Angle",0,180,value=this.elbow.old_angle)
        this.yaw_angle = st.slider("Yaw Angle",0,180,value=this.yaw.old_angle)

    st.divider()

    cola,colb,colc,cold =st.columns(4)

    if live:
        update_motors()
        with colc:
            st.button("Run List",on_click=rotate_list)
    else:
        with cola:
            st.button("Run Motors",on_click=update_motors)
        with colc:
            st.button("Run List",on_click=rotate_list)
    with colb:
        st.button("Add to Rotation List",on_click=appendList)
    with cold:
        st.button("Clear List",on_click=clearList)

    st.button("Exit SCADA",on_click=exit_threads)


    df = pd.DataFrame(this.rotationList,columns=["base","shoulder","elbow","wrist","pitch","yaw"])
    st.dataframe(df,hide_index=True)

    st.number_input("Time",key="timeStall")

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.number_input("A",key="a")
    with col2:
        st.number_input("B",key="b")
    with col3:
        st.number_input("C",key="c")
    with col4:
        pass

    st.write('<div style="display: flex; justify-content: center;">y=A*sin(x)+B*cos(x)+C</div>',unsafe_allow_html=True)

    import matplotlib.pyplot as plt

    x_values = np.linspace(0, 2*np.pi, 100)
    y_values = smoothingfunc(100,this.a,this.b,this.c)

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, 'o')

    ax.set_xlabel('Angle in radians')
    ax.set_ylabel('Delay between pulses')


    st.pyplot(fig)
