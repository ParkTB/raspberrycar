"""
Date : 2017/12/10
file name : miro.py
Purpose : 이 코드는 미로찾기를 위한 메인 모듈이다.
"""
import RPi.GPIO as GPIO
import going
import setting

try:
    # 초기 셋팅
    setting.LeftPwm.start(0)
    setting.RightPwm.start(0)
    while True:
        going.lineTrace(40)


except KeyboardInterrupt:
    # the speed of left motor will be set as LOW
    GPIO.output(setting.MotorLeft_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setting.LeftPwm.ChangeDutyCycle(0)
    # the speed of right motor will be set as LOW
    GPIO.output(setting.MotorRight_PWM, GPIO.LOW)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    setting.RightPwm.ChangeDutyCycle(0)
    # GPIO pin setup has been cleared
    GPIO.cleanup()
# =======================================================================
