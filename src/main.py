import time
import busio
import board
import adafruit_amg88xx
import RPi.GPIO as GPIO

# Set up thermal AMG8833
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

# Set up PIR
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17

GPIO.setup(PIR_PIN, GPIO.IN)

print('Startup, give it 3 seconds')
time.sleep(3)
print('READY')

while True:
    if not GPIO.input(PIR_PIN):
        for row in amg.pixels:
            print(["{0:.3f}".format(temp) for temp in row])
        print("\n")
        time.sleep(4)
    else:
        print("Not doing, presence detected")
