#!/usr/bin/env python3
# File name   : init
# Description : Control Servos
# Author      : William
# Date        : 2019/02/23
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def home():
        pwm.set_pwm(15,0,300)
        time.sleep(0.01)
        pwm.set_pwm(12,0, 530)
        time.sleep(0.01)
        pwm.set_pwm(13,0,520)
        time.sleep(0.01)
def extend_up():
        pwm.set_pwm(15,0,300)
        time.sleep(0.01)
        pwm.set_pwm(12,0, 355)
        time.sleep(0.01)
        pwm.set_pwm(13,0,190)
        time.sleep(0.01)
def extend_out():
        pwm.set_pwm(15,0,300)
        time.sleep(0.01)
        pwm.set_pwm(12,0, 165)
        time.sleep(0.01)
        pwm.set_pwm(13,0,185)
        time.sleep(0.01)
def rot():
        pwm.set_pwm(14,0,100)
        time.sleep(1.3)
        pwm.set_pwm(14,0, 200)
        time.sleep(0.3)
        pwm.set_pwm(14,0,300)
        time.sleep(0.3)
        pwm.set_pwm(14,0, 400)
        time.sleep(0.3)
        pwm.set_pwm(14,0,500)
        time.sleep(1.3)
        
home()
time.sleep(1)
while True:
    pwm.set_pwm(15,0,100)
    time.sleep(0.50)
    pwm.set_pwm(15,0,300)
    time.sleep(0.50)
    rot()
    pwm.set_pwm(15,0,100)
    time.sleep(0.50)
    pwm.set_pwm(15,0,300)
    time.sleep(0.50)
#extend_out()