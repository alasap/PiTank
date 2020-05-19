import time
import Adafruit_PCA9685
import getch

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


down=335
straight=320
up=180

def down():
    pwm.set_pwm(11,0,335)
    time.sleep(0.2)
def straight():
    pwm.set_pwm(11,0,320)
    time.sleep(0.2)
def up():
    pwm.set_pwm(11,0,180)
    time.sleep(0.2)

while True:
    char = getch.getch()
    if char == 'd':
        down()
    if char == 's':
        straight()
    if char  == 'u':
        up()
