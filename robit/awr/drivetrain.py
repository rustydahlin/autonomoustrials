from robit.drivetrain import BaseDrivetrain
import RPi.GPIO as GPIO
import time

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN = 7
Motor_B_EN = 11

Motor_A_Pin1 = 8
Motor_A_Pin2 = 10
Motor_B_Pin1 = 13
Motor_B_Pin2 = 12

Dir_forward = 1
Dir_backward = 0

left_forward = 1
left_backward = 0

right_forward = 1
right_backward = 0

pwn_A = 0
pwm_B = 0


class AWR_Drivetrain(BaseDrivetrain):
    '''
    go - True/False
    direction - 1 = forward, 0 = backwards
    speed - 1-100 (100 = full speed)
    '''

    def motor_left(self, go, direction, speed):
        if go:
            print("direction: {0} speed: {1}".format(direction, speed))
            if direction == Dir_backward:
                GPIO.output(Motor_B_Pin1, GPIO.HIGH)
                GPIO.output(Motor_B_Pin2, GPIO.LOW)
                pwm_B.start(100)
                pwm_B.ChangeDutyCycle(speed)
            elif direction == Dir_forward:
                GPIO.output(Motor_B_Pin1, GPIO.LOW)
                GPIO.output(Motor_B_Pin2, GPIO.HIGH)
                pwm_B.start(0)
                pwm_B.ChangeDutyCycle(speed)
        else:
            print("stop")
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            GPIO.output(Motor_B_EN, GPIO.LOW)

    '''
    go - True/False
    direction - 1 = forward, 0 = backwards
    speed - 1-100 (100 = full speed)
    '''

    def motor_right(self, go, direction, speed):
        if go:
            print("direction: {0} speed: {1}".format(direction, speed))
            if direction == Dir_forward:
                GPIO.output(Motor_A_Pin1, GPIO.HIGH)
                GPIO.output(Motor_A_Pin2, GPIO.LOW)
                pwm_A.start(100)
                pwm_A.ChangeDutyCycle(speed)
            elif direction == Dir_backward:
                GPIO.output(Motor_A_Pin1, GPIO.LOW)
                GPIO.output(Motor_A_Pin2, GPIO.HIGH)
                pwm_A.start(0)
                pwm_A.ChangeDutyCycle(speed)
        else:
            print("stop")
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            GPIO.output(Motor_A_EN, GPIO.LOW)


def motor_Stop():  # Motor stops
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():  # Motor initialization
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    motor_Stop()
    try:
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass


def destroy():
    motor_Stop()
    GPIO.cleanup()             # Release resource


if __name__ == '__main__':
    try:
        speed_set = 50
        setup()
        test = AWR_Drivetrain()
        test.motor_left(1, 1, speed_set)
        test.motor_right(1, 1, speed_set)
        time.sleep(1)
        test.motor_left(1, 0, speed_set)
        test.motor_right(1, 0, speed_set)
        time.sleep(1)
        test.motor_left(1, 1, speed_set)
        test.motor_right(1, 1, speed_set)
        time.sleep(1)
        test.motor_left(1, 0, speed_set)
        test.motor_right(1, 0, speed_set)
        time.sleep(1)
    except KeyboardInterrupt:
        destroy()
