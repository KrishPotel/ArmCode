import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    print("pigpio daemon not running!")
    exit()

SERVO_PIN = 14

def setAngle(angle):
    angle = max(0, min(180, angle))  # clamp
    pulsewidth = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(SERVO_PIN, pulsewidth)

try:
    while True:
        angle = int(input("Enter servo angle (0–180): "))
        setAngle(angle)

except KeyboardInterrupt:
    pass

finally:
    pi.set_servo_pulsewidth(SERVO_PIN, 0)  # stop signal
    pi.stop()