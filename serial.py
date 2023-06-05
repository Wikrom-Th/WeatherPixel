from config import COM_PORT
import serial

arduino = serial.Serial(COM_PORT, baudrate=9600, timeout=.1)

while True:
    temp = input("What is the temperature? ")
    arduino.write(bytes(temp, 'utf-8'))
    print(arduino.readline())