import time
import RPi.GPIO as GPIO
import pigpio
import threading
from shared import this

from mathModule import smoothingfunc
    
def usleep(micro):
    start_time = time.perf_counter()
    while ( time.perf_counter()-start_time ) < (micro/1_000_000):
        pass

motors = {
    "base_pulse":2,
    "shoulder_pulse":3,
    "elbow_pulse":17,
    "wrist_pulse":22,
    "end_yaw_pulse":26,
    "end_pitch_pulse":27
}

base = None
shoulder = None
elbow = None
wrist_roll = None
end_yaw = None
end_pitch = None

class Motor():
    exit_thread=False
    
    def __init__(self,pulsePin,func,default_angle):
        self.pulsePin = pulsePin
        self.pwm=pigpio.pi()
        self.pwm.set_mode(self.pulsePin,pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.pulsePin,50)
        
        self.old_angle = default_angle
        self.task=list()

        self.event=threading.Event()
        self.thread = threading.Thread(target=func)
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0


    def start_thread(self):
        self.thread.start()
        self.send_pulse(self.old_angle,0.2)
    
    def getList(self,angle):
        angleList = self.getAngleList(angle)
        #print(angleList)
        points = len(angleList)
        smoothingPoints = smoothingfunc(points,self.a,self.b,self.c)
        combinedList = [(angleList[i],smoothingPoints[i]) for i in range(points)]
        #print(combinedList)
        return combinedList


    def getAngleList(self,angle):
        if self.old_angle < angle:
            x = list(range(self.old_angle,angle,1))
            if angle - x[-1] < 1:
                x[-1] = angle
        else:
            x = list(range(self.old_angle,angle,-1))
            if x[-1] - angle < 1:
                x[-1] = angle
        return x

    def rotate_motor(self,angle):
        if angle == self.old_angle:
            return
        for i,j in self.getList(angle):
            self.send_pulse(i,j)
        self.old_angle = angle
        
    def send_pulse(self,angle,delay):
        if delay< 0:
            delay = 0
        duty = 2500- (2000/180)*(180-angle)
        self.pwm.set_servo_pulsewidth(self.pulsePin,duty)
        time.sleep(delay/10)
        

def motor_base():
    global base
    print("Base Motor Initialized")
    while not base.exit_thread:
        base.event.wait()
        for tasks in base.task:
            #print(f"Base: {tasks}")
            base.rotate_motor(tasks)
        base.task.clear()
        base.event.clear()
    del base
    print("Base Motor Disconnected")

def motor_shoulder():
    global shoulder
    print("Shoulder Motor Initialized")
    while not shoulder.exit_thread:
        shoulder.event.wait()
        for tasks in shoulder.task:
            shoulder.rotate_motor(tasks)
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
            elbow.rotate_motor(tasks)
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
            wrist_roll.rotate_motor(tasks)
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
            end_pitch.rotate_motor(tasks)
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
            end_yaw.rotate_motor(tasks)
        end_yaw.task.clear()
        end_yaw.event.clear()
    del end_yaw
    print("End Yaw Motor Disconnected")

def motors_init():
    global motors
    GPIO.setmode(GPIO.BCM)
    for i in motors.values():
        GPIO.setup(i,GPIO.OUT)

    global base,shoulder,elbow,wrist_roll,end_yaw,end_pitch

    base=Motor(motors["base_pulse"],motor_base,0)
    shoulder=Motor(motors["shoulder_pulse"],motor_shoulder,35)
    elbow=Motor(motors["elbow_pulse"],motor_elbow,20)
    wrist_roll=Motor(motors["wrist_pulse"],motor_wrist,35)
    end_yaw=Motor(motors["end_yaw_pulse"],motor_end_yaw,0)
    end_pitch=Motor(motors["end_pitch_pulse"],motor_end_pitch,0)
    
    base.start_thread()
    shoulder.start_thread()
    wrist_roll.start_thread()
    elbow.start_thread()
    end_yaw.start_thread()
    end_pitch.start_thread()