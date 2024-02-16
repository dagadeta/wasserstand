import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
clear = lambda: os.system("clear")

sensor_5 = 5
GPIO.setup(sensor_5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_4 = 6
GPIO.setup(sensor_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_3 = 13
GPIO.setup(sensor_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_2 = 19
GPIO.setup(sensor_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sensor_1 = 26
GPIO.setup(sensor_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        clear()
        if GPIO.input(sensor_5) == GPIO.LOW:
            print("sensor_5: Strom fließt")
        else:
            print("sensor_5: Kein Strom")
        if GPIO.input(sensor_4) == GPIO.LOW:
            print("sensor_4: Strom fließt")
        else:
            print("sensor_4: Kein Strom")
        if GPIO.input(sensor_3) == GPIO.LOW:
            print("sensor_3: Strom fließt")
        else:
            print("sensor_3: Kein Strom")
        if GPIO.input(sensor_2) == GPIO.LOW:
            print("sensor_2: Strom fließt")
        else:
            print("sensor_2: Kein Strom")
        if GPIO.input(sensor_1) == GPIO.LOW:
            print("sensor_1: Strom fließt")
        else:
            print("sensor_1: Kein Strom")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
