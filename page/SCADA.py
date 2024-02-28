import streamlit as st
import streamlit as st
from datetime import datetime
from utility.motor import motors_init
from utility.fileHandler import create_files
from utility.shared import this
#import RPi.GPIO as GPIO

def exit_threads():
    del this["motors"]
    for i in this.motors_list.values():
            i.exit_thread=True
            i.event.set()
            i.thread.join()
    this.pageName="Admin"
    print("Motors Exited")

def update_motors():
    if "motors" in this:
        #this.base.task.append(str(this.base_angle))
        #this.shoulder.task.append(str(this.shoulder_angle))
        #this.elbow.task.append(str(this.elbow_angle))
        #this.roll.task.append(str(this.roll_angle))
        #this.pitch.task.append(str(this.yaw_angle))
        #this.yaw.task.append(str(this.pitch_angle))
        
        this.base.task.append(this.base_angle)
        this.shoulder.task.append(this.shoulder_angle)
        this.elbow.task.append(this.elbow_angle)
        #this.roll.task.append(this.roll_angle)
        this.pitch.task.append(this.yaw_angle)
        this.yaw.task.append(this.pitch_angle)
        


        for i in this.motors_list.values():
            i.event.set()


def layout():
    st.write("SCADA System")

    if "motors" not in this:
        this.motors=True
    #   GPIO.cleanup()
    #  GPIO.setwarnings(False)
        motors_init()
        from utility.fileHandler import write_error,write_mesg,write_output
        this.output = write_output
        mesg="_________________________________"
        this.output(mesg)

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
            #"wrist":this.roll,
            "elbow":this.elbow,
            "pitch":this.pitch,
            "yaw":this.yaw
        }
        
    col1,col2,col3=st.columns(3)

    with col1:
        this.base_angle = st.slider("Base Angle",0,270)
        #st.write("Base Angle:", this.base_angle)

        this.roll_angle = st.slider("Roll Angle",0,270)
        #st.write("Roll Angle:", this.roll_angle)

    with col2:
        this.shoulder_angle = st.slider("Shoulder Angle",0,270)
        #st.write("Base Angle:", this.shoulder_angle)
        this.pitch_angle = st.slider("Pitch Angle",0,270)
        #st.write("Pitch Angle:", this.pitch_angle)

    with col3:
        this.elbow_angle = st.slider("Elbow Angle",0,270)
        #st.write("Elbow Angle:", this.elbow_angle)

        this.yaw_angle = st.slider("Yaw Angle",0,270)
        #st.write("Yaw Angle:", this.yaw_angle)

    send=st.button("Run Motors")
    st.button("Exit",on_click=exit_threads)

    if send:
        update_motors()
