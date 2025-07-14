import RPi.GPIO as GIPO
import time

GIPO.setmode(GIPO.BCM)
GIPO.setup(14, GIPO.OUT)

pwm = GIPO.PWM(17,50)
pwm.start()

def set_angle(angle):
    duty = (0.05 * angle) + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5);
    pwm.ChangeDutyCycle(0);

try:
    while True:
        set_angle(90)

except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GIPO.cleanup()