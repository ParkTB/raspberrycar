
# import GPIO library
import RPi.GPIO as GPIO

import time

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

trig=33   # 초음파 센서의 trig핀(음파송신)은 Raspberry Pi의 GPIO 33번 핀과 연결됨
echo=31   # 초음파 센서의 echo핀(음파수신)은 Raspberry Pi의 GPIO 31번 핀과 연결됨

#ultrasonic sensor setting
GPIO.setup(trig,GPIO.OUT)    # Raspberry Pi의 GPIO 33핀을 OUT핀으로 설정하여 음파가 송신되도록하는 명령어를 Raspberry Pi에서 초음파센서에게 보낸다(out설정이유, trig)
GPIO.setup(echo,GPIO.IN)     # Raspberry Pi의 GPIO 31핀을 IN핀으로 설정하여 음파가 수신되도록한다.



# 모터 회전방향 설정
forward = True
backward = False


# =======================================================================
# declare the pins of 12, 11, 35 in the Rapberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
MotorLeft_pinA = 12
MotorLeft_pinB = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Rapberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
MotorRight_pinA = 15
MotorRight_pinB = 13
MotorRight_PWM = 37


# ========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
def Lmotor_turn_set(x):
    if x == True:        #forward를 입력받으면 왼쪽 모터가 앞쪽으로 회전하기 위해 설정
        GPIO.output(MotorLeft_pinA, GPIO.HIGH)
        GPIO.output(MotorLeft_pinB, GPIO.LOW)
    elif x == False:    #backward를 입력받으면 왼쪽 모터가 뒤쪽으로 회전하기 위해 설정
        GPIO.output(MotorLeft_pinA, GPIO.LOW)
        GPIO.output(MotorLeft_pinB, GPIO.HIGH)
    else:
        print
        'Config Error'
def Rmotor_turn_set(x):
    if x == True:        #forward를 입력받으면 오른쪽 모터가 앞쪽으로 회전하기 위해 설정(회전방향이 오른쪽과 달라 low high 위치 변경)
        GPIO.output(MotorRight_pinA, GPIO.LOW)
        GPIO.output(MotorRight_pinB, GPIO.HIGH)
    elif x == False:    #backward를 입력받으면 오른쪽 모터가 뒤쪽으로 회전하기 위해 설정
        GPIO.output(MotorRight_pinA, GPIO.HIGH)
        GPIO.output(MotorRight_pinB, GPIO.LOW)
    else:
        print
        'Config Error'




# =======================================================================
# because the connetions between motors (left motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
GPIO.setup(MotorLeft_pinA, GPIO.OUT)
GPIO.setup(MotorLeft_pinB, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)


# =======================================================================
# because the connetions between motors (right motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
GPIO.setup(MotorRight_pinA, GPIO.OUT)
GPIO.setup(MotorRight_pinB, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
def go_forward_any(speed):
    LeftPwm.ChangeDutyCycle(speed)      #왼쪽모터와 오른쪽모터의 속력 변경
    RightPwm.ChangeDutyCycle(speed)
    
    Lmotor_turn_set(forward)            #왼쪽모터와 오른쪽모터 회전방향 설정
    Rmotor_turn_set(forward)
    
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)  #변경된 속도와 방향(전진)으로 작동
    GPIO.output(MotorRight_PWM,GPIO.HIGH)



# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
def go_backward_any(speed):
    LeftPwm.ChangeDutyCycle(speed)   #왼쪽모터와 오른쪽모터의 속력 변경
    RightPwm.ChangeDutyCycle(speed)
    
    Lmotor_turn_set(backward)        #왼쪽모터와 오른쪽모터 회전방향 설정
    Rmotor_turn_set(backward)
    
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)  #변경된 속도와 방향(후진)으로 작동
    GPIO.output(MotorRight_PWM,GPIO.HIGH)





# =======================================================================
#  go_forward method has been generated for the three-wheeled moving
#  object to go forward with the limitation of running_time
def go_forward(speed, running_time):
    LeftPwm.ChangeDutyCycle(speed)       #왼쪽모터와 오른쪽모터의 속력 변경
    RightPwm.ChangeDutyCycle(speed)
    
    Lmotor_turn_set(forward)             #왼쪽모터와 오른쪽모터 회전방향 설정
    Rmotor_turn_set(forward)
    
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)  #변경된 속도와 방향(전진)으로 작동
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
  
    time.sleep(running_time)            #작동 시간 설정




# =======================================================================
#  go_backward method has been generated for the three-wheeled moving
#  objec to go backward with the limitation of running_time
def go_backward(speed, running_time):
    LeftPwm.ChangeDutyCycle(speed)      #왼쪽모터와 오른쪽모터의 속력 변경
    RightPwm.ChangeDutyCycle(speed)
    
    Lmotor_turn_set(backward)           #왼쪽모터와 오른쪽모터 회전방향 설정
    Rmotor_turn_set(backward)
    
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)   #변경된 속도와 방향(후진)으로 작동
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    time.sleep(running_time)           #작동 시간 설정




# =======================================================================
# define the stop module
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def pwm_setup():    #양쪽 모터의 pwm(==speed) 초기값 0으로 세팅
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)  # the speed of left motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW) # the speed of right motor will be set as LOW
    LeftPwm.ChangeDutyCycle(0)            # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)           # right motor will be stopped with function of ChangeDutyCycle(0)
    GPIO.cleanup()



# ======================================================================
#오른쪽으로 돌기 위해 왼쪽모터를 forward 시키고 오른쪽모터를 stop 시킨다
def rightSwingTurn(speed, running_time):
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
    
    # set the left motor to go fowrard
    Lmotor_turn_set(forward)

    # set the left motor pwm to be ready to go forward
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)

    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    
   
    # set the running time of the left motor to go fowrard
    time.sleep(running_time)



# =======================================================================
# 왼쪽으로 돌기 위해 오른쪽모터를 forward 시키고 왼쪽모터를 stop 시킨다
def leftSwingTurn(speed, running_time):
    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)

    # set the left motor pwm to be ready to stop
    # Turn Off Left PWM
    GPIO.output(MotorLeft_PWM,GPIO.LOW)  

    # set the right motor to go fowrard
    Rmotor_turn_set(forward)

    # set the right motor pwm to be ready to go forward   
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    
    # set the running time of the right motor to go fowrard
    time.sleep(running_time)


# =======================================================================
# 오른쪽으로 돌기 위해 왼쪽모터를 forward 시키고 오른쪽모터를 backward 시킨다
def rightPointTurn(speed, running_time):
    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)



    # set the right motor to go backward
    # set the left motor to go forward
    Rmotor_turn_set(backward)
    Lmotor_turn_set(forward)

    # set the right motor pwm to be ready to go backward
    # set the left motor pwm to be ready to go forward
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)


    # set the running time of the right motor to go fowrard
    time.sleep(running_time)

#=======================================================================
# 왼쪽으로 회전시키기 위해 오른쪽모터를 forward 시키고 왼쪽모터를 backward 시킨다
def leftPointTurn(speed, running_time):
# set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)


    # set the right motor to go fowrard
    # set the left motor to go backward
    Rmotor_turn_set(forward)
    Lmotor_turn_set(backward)

    # set the right motor pwm to be ready to go forward
    # set the left motor pwm to be ready to go backward
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    # set the running time of the right motor to go fowrard
    time.sleep(running_time)


def getDistance():               #거리를 구하기 위한 함수
    GPIO.output(trig,False)      #초음파센서 trig에 False신호를 0.5초간 주어 초음파센서를 초기화한다
    time.sleep(0.5)
    GPIO.output(trig,True)       #초음파센서 trig에 True신호를 0.00001초간 주어 초음파센서에서 초음파가 발사되도록 한다
    time.sleep(0.00001)
    GPIO.output(trig,False)      #초음파센서 trig에 False신호를 주어 초음파 발사를 마친다.
    while GPIO.input(echo)==0:
        pulse_start=time.time()  # trig가 끝난 바로 직후에는 반사(echo)되어오는 초음파 신호가 아직 도달하지 않았다.
        # 즉, trig를 금방 끝마친 상황이다. pulse_start, 이때부터 반사되어 echo가 올 때까지 시간을 계산해야한다.
    while GPIO.input(echo)==1:  # 반사되어 echo 신호가 도달한다. (pulse_end)
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start   # 왕복되어 온 시간은 pulse_end- pulse_start
    distance=pulse_duration*17000
    # 음속: 340m/1초, 34000cm/1초, (1m=100cm), 340000*pulse_duration/2 = 17000*pulse_duration
    # 왕복거리가 아니라 편도거리임로 왕복되어 온 시간을 나누기 2를 한다 (pulse_end- pulse_start)/2 :
    distance=round(distance,2)
    return distance





# =======================================================================
# setup and initilaize the left motor and right motor
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
dis = 30  # 멈출 거리 지정


try:
    while True:
        distance = getDistance()   #거리 측정
        print('distance= ', distance)
        go_forward_any(40)

        if (distance < dis): # distance가 dis보다 작으면 멈추고 rightSwingTurn을 실행하고 다음 반복문을 실행한다
            stop()
            time.sleep(1)
            rightSwingTurn(47,0.5)
            time.sleep(1)
            while True:
                distance2 = getDistance() # 새로운 거리 측정
                print('distance2= ', distance2)
                go_forward_any(40)
                if (distance2<dis):  # distance2가 dis보다 작아지면 멈추고 rightPointTurn 실행, 3초간 전진 후 종료한다
                    stop()
                    time.sleep(1)
                    rightPointTurn(42,0.5)
                    time.sleep(1)
                    go_forward(40,3)
                    quit()
            





# when the Ctrl+C key has been pressed,
# the moving object will be stopped
except KeyboardInterrupt:
    pwm_low()


