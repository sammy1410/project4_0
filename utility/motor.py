import time
#import RPi.GPIO as GPIO
from utility.shared import usleep
import threading
from utility.fileHandler import write_error,write_mesg,SCADA_log
from utility.shared import this

motors = {
    "base_dir":2,
    "base_pulse":3,
    "shoulder_dir":17,
    "shoulder_pulse":27,
    "elbow_dir":5,
    "elbow_pulse":6,
    #"wrist_dir":25,
    #"wrist_pulse":16,
    "end_yaw_dir":23,
    "end_yaw_pulse":24,
    "end_pitch_dir":25,
    "end_pitch_pulse":16
}

base = None
shoulder = None
elbow = None
wrist_roll = None
end_yaw = None
end_pitch = None


step = {
    "1": 200,
    "2/A": 400,
    "2/B": 400,
    "4":800,
    "8":1600,
    "16":3200,
    "32":6400
}

class Motor():
    current_mode = 4
    step_mode = step["1"]
    exit_thread=False
    
    def __init__(self,pulsePin,dirPin,_step,func):
        self.step_mode=_step
        self.pulsePin = pulsePin
        self.dirPin=dirPin
        self.task=list()

        self.event=threading.Event()
        self.thread = threading.Thread(target=func)
        #self.thread.join()


    def start_thread(self):
        self.thread.start()

    def rotate_motor(self,angle,speed,dir):
        if (int(dir)==1):
            pass
            # GPIO.output(self.dirPin,GPIO.HIGH)
        else:
            pass
#            GPIO.output(self.dirPin,GPIO.LOW)
        steps = int((int(angle)*200)/360)
        self.send_pulse(speed,steps)
        time.sleep(1)

    def send_pulse(self,pulseWidth,pulseNo):
        for i in range(pulseNo):
            #GPIO.output(self.pulsePin,GPIO.HIGH)
            usleep(int(pulseWidth))
            #GPIO.output(self.pulsePin,GPIO.LOW)
            usleep(int(pulseWidth))
        
def motor_base():
    global base
    print("Base Motor Initialized")
    while not base.exit_thread:
        base.event.wait()
        #print(f"Base: {base.task}")#Do Task
        for tasks in base.task:
            #print(f"Base: {tasks}")
            base.rotate_motor(tasks,1000,1)
            SCADA_log(f"Base: {tasks}")
            #base.task.remove(tasks)
        base.task.clear()
        base.event.clear()
    del base
    print("Base Motor Disconnected")

def motor_shoulder():
    global shoulder
    print("Shoulder Motor Initialized")
    while not shoulder.exit_thread:
        shoulder.event.wait()
        #print(f"Shoulder: {shoulder.task}")
        for tasks in shoulder.task:
            print(f"Shoulder: {tasks}")
            SCADA_log(f"Shoulder: {tasks}")
            shoulder.rotate_motor(tasks,1000,1)
        shoulder.task.clear()
        shoulder.event.clear()
    del shoulder
    print("Shoulder Motor Disconnected")

def motor_elbow():
    global elbow
    print("Elbow Motor Initialized")
    while not elbow.exit_thread:  
        elbow.event.wait()
        for tasks in elbow.task:
            print(f"Elbow: {tasks}")
            SCADA_log(f"Elbow: {tasks}")
            elbow.rotate_motor(tasks,1000,1)
        elbow.task.clear()    
        elbow.event.clear()
    del elbow
    print("Elbow Motor Disconnected")

def motor_wrist():
    global wrist_roll
    print("Wrist Motor Initialized")
    while not wrist_roll.exit_thread:
        wrist_roll.event.wait()
        for tasks in wrist_roll.task:
            SCADA_log(f"Wrist Roll: {tasks}")
            wrist_roll.rotate_motor(tasks,1000,1)
        wrist_roll.task.clear()
        wrist_roll.event.clear()
    del wrist_roll
    print("Wrist Motor Disconnected")

def motor_end_pitch():
    global end_pitch
    print("End Pitch Motor Initialized")
    while not end_pitch.exit_thread:
        end_pitch.event.wait()
        for tasks in end_pitch.task:
            SCADA_log(f"End Pitch: {tasks}")
            end_pitch.rotate_motor(tasks,1000,1)
        end_pitch.task.clear()
        end_pitch.event.clear()
    del end_pitch
    print("End Pitch Motor Disconnected")

def motor_end_yaw():
    global end_yaw
    print("End Yaw Motor Initialized")
    while not end_yaw.exit_thread:
        end_yaw.event.wait()
        for tasks in end_yaw.task:
            SCADA_log(f"End Yaw: {tasks}")
            end_yaw.rotate_motor(tasks,1000,1)
        end_yaw.task.clear()
        end_yaw.event.clear()
    del end_yaw
    print("End Yaw Motor Disconnected")

def motors_init():
    global motors
    #GPIO.setmode(GPIO.BCM)
    #for i in motors.values():
        #GPIO.setup(i,GPIO.OUT)

    global base,shoulder,elbow,wrist_roll,end_yaw,end_pitch
    base=Motor(motors["base_pulse"],motors["base_dir"],200,motor_base)
    shoulder=Motor(motors["shoulder_pulse"],motors["shoulder_dir"],200,motor_shoulder)
    elbow=Motor(motors["elbow_pulse"],motors["elbow_dir"],200,motor_elbow)
    #wrist_roll=Motor(None,None,200,motor_wrist)
    end_yaw=Motor(motors["end_yaw_pulse"],motors["end_yaw_dir"],200,motor_end_yaw)
    end_pitch=Motor(motors["end_pitch_pulse"],motors["end_pitch_dir"],200,motor_end_pitch)

    base.start_thread()
    shoulder.start_thread()
    elbow.start_thread()
    end_yaw.start_thread()
    end_pitch.start_thread()