import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    print("pigpio daemon not running!")
    exit()

SERVO_PIN = 14
SERVO_PIN_SMALL = 15
SERVO_PIN_GRIPPER = 18

WristOffset = 5
ArmOffset = -5

def setAngleBIG(angle):
    angle = max(30, min(150, angle+ArmOffset))  # clamp
    pulsewidth = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(SERVO_PIN, pulsewidth)

def setAngleSmall(angle):
    angle = max(0, min(180, angle+WristOffset))  # clamp
    pulsewidth = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(SERVO_PIN_SMALL, pulsewidth)

def setGripperOpenOrClose(open: bool):
    if open:
        angle = 0
    else:
        angle = 90

    pulsewidth = 500 + (angle / 180.0) * 1900
    pi.set_servo_pulsewidth(SERVO_PIN_GRIPPER, pulsewidth)


try:
    while True:

        angle2 = int(input("Enter servo angle (0-180): "))
        setAngleSmall(angle2)

        angle = int(input("Enter wrist angle (0-180): "))
        setAngleBIG(angle)

        openOrClose = int(input("Enter 1 for open and 2 for close"))
        setGripperOpenOrClose(1 if openOrClose == 1 else 0)


except KeyboardInterrupt:
    pass

finally:
    pi.set_servo_pulsewidth(SERVO_PIN, 0)  # stop signal
    pi.set_servo_pulsewdith(SERVO_PIN_GRIPPER, 0)
    pi.set_servo_pulsewdith(SERVO_PIN_SMALL, 0)

    pi.stop()