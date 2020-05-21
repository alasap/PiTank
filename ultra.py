import multiprocessing
import time
import Adafruit_PCA9685
import getch
import test_video
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
#test_video.stream()
def control():
    while True:
        #char = input()
        char = getch.getch()
        if char == 'd':
            down()
        if char == 's':
            straight()
        if char  == 'u':
            up()


v1=multiprocessing.Process(target=test_video.stream)
v1.start()
c1 = multiprocessing.Process(target = control)
c1.start()
