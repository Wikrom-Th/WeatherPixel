from time import sleep
from config import COM_PORT

from src.serial_com import WeatherSerial

myserial = WeatherSerial(COM_PORT)

for i in range(0,41,5):
    myserial.write_temp(i)
    print(i)
    sleep(0.5)

sleep(5)
myserial.write_temp(25, 1)