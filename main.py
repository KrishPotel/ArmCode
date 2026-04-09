import pigpio
import time

pi = pigpio.pi()

def setAngle(angle,SERVO_PIN):
    plusewidth = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(SERVO_PIN,plusewidth)

try:
    while True:
        angle = int(input("Enter Servo 1 angle"))
        setAngle(angle,15)

except KeyboardInterrupt:
    pass

finally:
    pi.set_servo_pulsewidth(15,0)
    pi.stop()