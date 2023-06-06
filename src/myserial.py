from config import COM_PORT
import serial

class WeatherSerial():
    def __init__(self):
        self.arduino = serial.Serial(COM_PORT, baudrate=9600, timeout=.1)
    
    def write(self, input):
        self.arduino.write(bytes(input, 'utf-8'))
        print(self.arduino.readline())