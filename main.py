from microbit import *
from utime import ticks_us, sleep_us

SONAR = pin15

def sonar( ):
    SONAR.write_digital(1) # Send 10us Ping pulse
    sleep_us(10)
    SONAR.write_digital(0)
    SONAR.set_pull(SONAR, NO_PULL)
    while SONAR.read_digital() == 0:
        pass
    start = ticks_us() # define starting time
    while SONAR.read_digital() == 1:
        pass
    end = ticks_us() # define ending time
    echo = end-start
    distance = int(0.01715 * echo) # Calculate cm distance
    return distance


x = 0
y = 0

def check():
    if 1 == sonar():
        return True
   

def mapping():

    if not check():
        bitbot.go(BBDirection.FORWARD, 60)
   
    else :
        bitbot.rotate(BBRobotDirection.LEFT, 60)
       
       
run = True
#main loop
while run:
    mapping()
