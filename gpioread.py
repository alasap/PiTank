import time
import Adafruit_PCA9685
import pigpio
pi = pigpio.pi()

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
#have to add 500 to pwm value and set the pulsewidth to be able to read
def test_1():
    while True:
        for i in range(100,300):
            pwm.set_pwm(15,0,i)
            pi.set_servo_pulsewidth(15,i+500)
            time.sleep(0.1)
            print(pi.get_servo_pulsewidth(15))
