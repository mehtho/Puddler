import time
import busio
import board
import adafruit_amg88xx
import RPi.GPIO as GPIO
import mpu6050
import json

# Frequency
FREQ = 2

# Set up thermal AMG8833
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

mpu6050 = mpu6050.mpu6050(0x68)

def read_acc_temp():
    gyroscope_data = mpu6050.get_gyro_data()
    temperature = mpu6050.get_temp()

    return gyroscope_data, temperature

def Record():
    def __init__(self, therm, gyr, ambient_temp, has_motion):
        self.therm = therm
        self.gyr = gyr
        self.ambient_temp = ambient_temp
        self.has_motion = has_motion

# Set up PIR
GPIO.setmode(GPIO.BCM)
PIR_PIN = 27

GPIO.setup(PIR_PIN, GPIO.IN)

print('Startup, give it 3 seconds')
time.sleep(3)
print('READY')

while True:
    # if not GPIO.input(PIR_PIN):
    #     for row in amg.pixels:
    #         print(["{0:.3f}".format(temp) for temp in row])
    #     print("\n")
    # else:
    #     print("Not doing, presence detected")
    gyroscope, ambient = read_acc_temp()
    rec = Record(amg.pixels, gyroscope, ambient, GPIO.input(PIR_PIN))
    
    print(json.dumps(rec))
    
    time.sleep(FREQ)
