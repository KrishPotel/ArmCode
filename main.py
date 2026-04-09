import RPi.GPIO as GIPO
import time

GIPO.setmode(GIPO.BCM)
GIPO.setup(14, GIPO.OUT)

pwm = GIPO.PWM(14,50)
pwm.start(0)

def set_angle(angle):
    duty = (0.05 * angle) + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5);
    pwm.ChangeDutyCycle(0);

try:
    while True:
        k = int(input())
        set_angle(k)

except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GIPO.cleanup()